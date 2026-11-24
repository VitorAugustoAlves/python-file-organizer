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

if(caminho.is_dir()==False):
    print("O caminho selecionado não é uma pasta. Selecione outro caminho que seje uma.")
    sys.exit(1)
print("Arquivos identificados: ")

for i, arquivo in enumerate(caminho.iterdir(), start=1):
    if(arquivo.is_dir()):
        continue
    print(f"{i}. {arquivo.name}")
