import os
import shutil
"Utilidade"
def separar_pessoas_validas(diretorio_origem, diretorio_destino, min_imagens=2):

    if not os.path.exists(diretorio_destino):
        os.makedirs(diretorio_destino)
    
    pessoas_validas = 0
    pessoas_invalidas = 0
    
    for pessoa in os.listdir(diretorio_origem):
        caminho_pessoa_origem = os.path.join(diretorio_origem, pessoa)
        
      
        if os.path.isdir(caminho_pessoa_origem):
            imagens = [f for f in os.listdir(caminho_pessoa_origem) 
                      if f.endswith(('.jpg', '.png', '.jpeg'))]
            
            if len(imagens) >= min_imagens:
                # Criar pasta no destino
                caminho_pessoa_destino = os.path.join(diretorio_destino, pessoa)
                os.makedirs(caminho_pessoa_destino, exist_ok=True)
                
                # Copiar todas as imagens
                for img in imagens:
                    origem_img = os.path.join(caminho_pessoa_origem, img)
                    destino_img = os.path.join(caminho_pessoa_destino, img)
                    shutil.copy2(origem_img, destino_img)
                
                pessoas_validas += 1
                print(f" {pessoa}: {len(imagens)} imagens")
            else:
                pessoas_invalidas += 1
                print(f" {pessoa}: apenas {len(imagens)} imagem(ns)")
    
    print(f"\n--- RESULTADO FINAL ---")
    print(f"Pessoas válidas (≥{min_imagens} imagens): {pessoas_validas}")
    print(f"Pessoas inválidas: {pessoas_invalidas}")
    print(f"Total processado: {pessoas_validas + pessoas_invalidas}")

separar_pessoas_validas(
    diretorio_origem=r"D:\Desktop\IA3\Dataset", 
    diretorio_destino=r"D:\Desktop\new_data_set", 
    min_imagens=2
)