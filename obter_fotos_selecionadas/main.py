import re
import csv
import os

diretorio_atual = os.getcwd()

def obter_fotos(texto):
    padrao = r'TTF_\d+'
    correspondencias = re.findall(padrao, texto)
    return correspondencias
    
def gerar_arquivo(nome_arquivo, correspondencias):
    with open(nome_arquivo, 'w', newline='') as arquivo_csv:
        escritor_csv = csv.writer(arquivo_csv)
        for correspondencia in correspondencias:
            escritor_csv.writerow([correspondencia])

    print(f"Arquivo CSV '{nome_arquivo}' ")
    

def ler_arquivo(nome_arquivo_entrada):
    with open(nome_arquivo_entrada, 'r') as arquivo_entrada:
        texto = arquivo_entrada.read()
        
    return texto


def main():
    nome_arquivo_entrada = os.path.join(diretorio_atual, 'obter_fotos_selecionadas', 'fotos_selecionadas.txt')
    nome_arquivo_saida = os.path.join(diretorio_atual, 'obter_fotos_selecionadas', 'fotos_selecionadas.csv')
    
    fotos_selecionadas = ler_arquivo(nome_arquivo_entrada)
    fotos = obter_fotos(fotos_selecionadas)
    gerar_arquivo(nome_arquivo_saida, fotos)

if __name__ == "__main__":
    main()
    