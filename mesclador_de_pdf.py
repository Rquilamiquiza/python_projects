import PyPDF2
import os

merger = PyPDF2.PdfMerger()
listar_arquivos = os.listdir('a pasta onde estão os pdfs')
listar_arquivos.sort()

for arquivo in listar_arquivos:
    if ".pdf" in arquivo:
        merger.append(f"endereço dos pdfs/{arquivo}")
merger.write("PDF mesclado.pdf")