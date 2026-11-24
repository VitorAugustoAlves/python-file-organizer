#Organizador de Arquivos em python
#Feito por Vitor A. A. Teodósio em 2026
#Projeto com foco de aprendizado

from pathlib import Path
import sys

print("========== ORGANIZADOR DE ARQUIVOS ==========")
print("")
caminhoUsuario = input("Digite o caminho da pasta matriz para ser organizada: ")
caminho = Path(caminhoUsuario)
if(caminho.exists()==False):
    print("Pasta não encontrada. Verifique o caminho digitado.")
    sys.exit(1)
print("Pasta encontrada!")
