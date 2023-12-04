import re
import csv
import os
import argparse

diretorio_atual = os.getcwd()

def obter_fotos(texto, padrao):
    padrao = r'\b' + re.escape(padrao) + r'_\d+\b'
    correspondencias = re.findall(padrao, texto)
    return correspondencias
    
def gerar_arquivo(nome_arquivo, correspondencias):
    linha_csv = ','.join(correspondencias)
    with open(nome_arquivo, 'w', newline='') as arquivo_csv:
        arquivo_csv.write(linha_csv)

    print(f"Arquivo CSV '{nome_arquivo}' ")
    

def ler_arquivo(nome_arquivo_entrada):
    with open(nome_arquivo_entrada, 'r') as arquivo_entrada:
        texto = arquivo_entrada.read()
        
    return texto


def main():
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    nome_arquivo_entrada = os.path.join(diretorio_atual, 'fotos_selecionadas.txt')
    nome_arquivo_saida = os.path.join(diretorio_atual, 'lightroom.csv')
    parser = argparse.ArgumentParser(description='Script para buscar correspondências em um arquivo de texto.')
    parser.add_argument('padrao', type=str, help='Padrão para buscar correspondências')

    args = parser.parse_args()
    
    fotos_selecionadas = ler_arquivo(nome_arquivo_entrada)
    fotos = obter_fotos(fotos_selecionadas, args.padrao)
    gerar_arquivo(nome_arquivo_saida, fotos)

if __name__ == "__main__":
    main()
    