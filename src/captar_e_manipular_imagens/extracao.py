import zipfile
"utilidade"

def extrair_zip(caminho_zip, pasta_destino):
   
    with zipfile.ZipFile(caminho_zip, 'r') as zip_ref:
        zip_ref.extractall(pasta_destino)
    print(f"ZIP extraído para: {pasta_destino}")


extrair_zip(
    caminho_zip=r"D:\Downloads\archive.zip",
    pasta_destino=r"D:\Desktop\oi"
)


