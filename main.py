# Totem FlexMedia - Sprint 1
# Autor: João Pedro de Souza Nunes
# Protótipo de totem interativo com cadastro e listagem de informações

import time
import os
import sys

VERDE = '\033[32m'
VERMELHO = '\033[31m'
AZUL = '\033[34m'
AMARELO = '\033[33m'
MAGENTA = '\033[35m'
CIANO = '\033[36m'
RESET = '\033[0m'

informacoes = []

def limpar_tela():
    if sys.platform == 'win32':
        os.system('cls')
    else:
        os.system('clear')
    print('\n' * 5)

def carregando(mensagem='Carregando'):
    print(AMARELO + mensagem, end='', flush=True)
    for _ in range(3):
        time.sleep(0.5)
        print('.', end='', flush=True)
    time.sleep(0.5)
    print(RESET)

def cadastrar_informacao(lista):
    while True:
        limpar_tela()
        print(CIANO + '='*40)
        print('       CADASTRO DE INFORMAÇÃO')
        print('='*40 + RESET + '\n')
        
        titulo = input('Digite o título da informação: ').strip()

        tipos_permitidos = ['educativo', 'cultural', 'lazer', 'esportivo', 'informativo', 'tecnológico']
        print('\nTipos disponíveis:', ', '.join(tipos_permitidos))

        while True:
            tipo_input = input('Digite o tipo: ').strip().lower()
            if tipo_input in tipos_permitidos:
                tipo = tipo_input.capitalize()
                break
            else:
                print(VERMELHO + f'\n⚠️ Tipo inválido! Digite uma das opções: {", ".join(tipos_permitidos)}.' + RESET)

        descricao = input('\nDigite uma breve descrição: ').strip()

        info = {'Título': titulo, 'Tipo': tipo, 'Descrição': descricao}
        lista.append(info)

        carregando('\nSalvando informação')

        total = len(lista)
        print(VERDE + f'\n✅ Informação cadastrada com sucesso! Total de cadastros: {total}\n' + RESET)
        time.sleep(0.5)

        while True:
            continuar = input('Deseja cadastrar outra informação? (S/N): ').strip().lower()
            if continuar in ['s', 'sim']:
                repetir = True
                break
            elif continuar in ['n', 'nao', 'não']:
                repetir = False
                break
            else:
                print(VERMELHO + '\n⚠️ Resposta inválida! Digite S/N ou Sim/Não.' + RESET)
        
        if not repetir:
            break

def listar_informacoes(lista):
    limpar_tela()
    print(CIANO + '='*40)
    print('       INFORMAÇÕES CADASTRADAS')
    print('='*40 + RESET + '\n')

    if len(lista) == 0:
        print(AMARELO + 'Nenhuma informação cadastrada ainda.\n' + RESET)
    else:
        for i, info in enumerate(lista, start=1):
            cor = {
                'Educativo': AZUL,
                'Cultural': MAGENTA,
                'Lazer': AMARELO,
                'Esportivo': VERDE,
                'Informativo': CIANO,
                'Tecnológico': MAGENTA
            }.get(info['Tipo'], RESET)

            print(cor + f'{i}. {info["Título"]} ({info["Tipo"]})' + RESET)
            print(f'   Descrição: {info["Descrição"]}\n')
            time.sleep(0.2)

    input('Pressione Enter para voltar ao menu...')

def menu():
    while True:
        limpar_tela()
        print(CIANO + '='*40)
        print('           TOTEM FLEXMEDIA')
        print('='*40 + RESET)
        print(AMARELO + '1 - Cadastrar informação' + RESET)
        print(AMARELO + '2 - Listar informações cadastradas' + RESET)
        print(AMARELO + '0 - Sair' + RESET)
        print(CIANO + '='*40 + RESET)

        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            cadastrar_informacao(informacoes)
        elif opcao == '2':
            listar_informacoes(informacoes)
        elif opcao == '0':
            print(VERDE + '\n👋 Encerrando o programa... Até logo!' + RESET)
            break
        else:
            print(VERMELHO + '\n⚠️ Opção inválida! Tente novamente.\n' + RESET)
            time.sleep(1)

if __name__ == '__main__':
    menu()
