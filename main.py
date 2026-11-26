#Organizador de Arquivos em python
#Feito por Vitor A. A. Teodósio em 2026
#Projeto com foco de aprendizado

from pathlib import Path
import sys

print("========== ORGANIZADOR DE ARQUIVOS ==========")
print("")
caminhoUsuario = input("Digite o caminho da pasta matriz para ser organizada: ")
caminho = Path(caminhoUsuario)

if caminho.exists()==False: #verificando a pasta
    print("Pasta não encontrada. Verifique o caminho digitado.")
    sys.exit(1)

if caminho.is_dir()==False: #verificando o caminho
    print("O caminho selecionado não é uma pasta. Selecione outro caminho que seje uma.")
    sys.exit(1)

arquivos = [arquivo for arquivo in caminho.iterdir() if arquivo.is_file()] #lista que remove as subpastas

if not arquivos: #verificando se a pasta está vazia
    print("A pasta não contém arquivos para serem organizados.")
    sys.exit(1) 

print("")
print("Pasta encontrada!")
print("")


print("Arquivos identificados: ")
print("")


for i, arquivo in enumerate(arquivos, start=1): #numerando os arquivos da lista
    extensao = arquivo.suffix
    if extensao == "":
        extensao = "Arquivo sem extenção."
    
    print(f"{i}. {arquivo.name} ----- Extenção: {extensao}")

qtd = len(arquivos)
print("")
print(f"Quantidade de arquivos encontrados: {qtd}")
print("")

print("===========================================")