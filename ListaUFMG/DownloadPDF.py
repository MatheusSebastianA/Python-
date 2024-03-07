import wget, PyPDF2, sys
from subprocess import run

ExcluirListaAnterior = ["rm", "lista.pdf"]
run(ExcluirListaAnterior)

link = sys.argv[1]
wget.download(link, "lista.pdf")

arquivoPDF = open("lista.pdf", "rb")
pdf = PyPDF2.PdfReader(arquivoPDF)
num_paginas = len(pdf.pages)


arquivo = open("lista.txt", "w")
for i in range(num_paginas):
    pagina = pdf.pages[i]
    conteudo_pagina = pagina.extract_text()
    arquivo.write(conteudo_pagina)

comando = ["./listagemUFMG.sh", "lista.txt", "Convocados.txt"]
run(comando)
