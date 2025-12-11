import cv2
from insightface.app import FaceAnalysis
import os

class CapturarImagem: #O enquadraemento está ajustado para captar as imagens o mais aproximado ao enquaddramento das imagens do dataset
    def __init__(self):
        self.app = FaceAnalysis()
        self.app.prepare(ctx_id=0, det_size=(640, 640))
        self.caminho = r"D:\Desktop\IA3\Dataset\Imagens_para_uso_rapido"

    def medir_blur(self, imagem):
        return cv2.Laplacian(imagem, cv2.CV_64F).var()

    def capturar_imagens(self, quantidade):
        pasta = self.caminho
        os.makedirs(pasta, exist_ok=True)

        cap = cv2.VideoCapture(0)

        fotos = 0
        frames_estaveis = 0
        FRAMES_PARA_CONFIAR = 4

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            faces = self.app.get(frame)

            if len(faces) == 0:
                frames_estaveis = 0
                cv2.imshow("Captura", frame)
                if cv2.waitKey(1) == 27:
                    break
                continue

            face = faces[0]
            x1, y1, x2, y2 = face.bbox.astype(int)
            w, h = x2 - x1, y2 - y1



            if face.det_score < 0.85:
                frames_estaveis = 0
                cv2.putText(frame, "Face ruim", (10, 40),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,300), 2)
                cv2.imshow("Captura", frame)
                if cv2.waitKey(1) == 27:
                    break
                continue

            if w < 120 or h < 120:
                frames_estaveis = 0
                cv2.putText(frame, "Não se acanhe, chegue mais próximo! Sem-vergonha!", (10, 80),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,300), 2)
                cv2.imshow("Captura", frame)
                if cv2.waitKey(1) == 27:
                    break
                continue



            pad = int(0.25 * w)
            x1 = max(0, x1 - pad)
            y1 = max(0, y1 - pad)
            x2 = min(frame.shape[1], x2 + pad)
            y2 = min(frame.shape[0], y2 + pad)


            frame_limpo = frame.copy()

            face_cortada = frame_limpo[y1:y2, x1:x2]
            blur = self.medir_blur(face_cortada)

            

            if blur < 0: #Estava dando conflito com a webcam
                frames_estaveis = 0
                cv2.putText(frame, "Imagem borrada", (10, 120),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,300), 2)
                cv2.imshow("Captura", frame)
                if cv2.waitKey(1) == 27:
                    break
                continue



            frames_estaveis += 1

            cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)
            cv2.putText(frame, "FIQUE QUIETO...", (10, 40),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
            cv2.imshow("Captura", frame)

            if frames_estaveis >= FRAMES_PARA_CONFIAR:
                fotos += 1


                face_final = cv2.resize(face_cortada, (250, 250))

                caminho_foto = os.path.join(pasta, f"face_{fotos}.jpg")
                cv2.imwrite(caminho_foto, face_final)

                print(f"Salva: {caminho_foto}")

                frames_estaveis = 0

            if fotos >= quantidade:
                break

            if cv2.waitKey(1) == 27:
                break

        cap.release()
        cv2.destroyAllWindows()
