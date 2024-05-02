import os
from tkinter.filedialog import askdirectory

caminho = askdirectory(title="Selecione a pasta")

listar_arq = os.listdir(caminho)

locais = {
    "Imagens":[".png",".jpg"],
    "Documentos":[".pdf",".xlsx"],
    "Video":[".mp4"]
}

for arquivo in listar_arq:
    nome, extensao = os.path.splitext(f"{caminho}/{arquivo}")
    for pasta in locais:
        if extensao in locais[pasta]:
            if not os.path.exists(f"{caminho}/{pasta}"):
                os.mkdir(f"{caminho}/{pasta}")
            os.rename(f"{caminho}/{arquivo}", f"{caminho}/{pasta}/{arquivo}")
