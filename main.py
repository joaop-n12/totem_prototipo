# Totem FlexMedia - Sprint 3
# Autor: João Pedro de Souza Nunes

from functions import (
    cadastrar_informacao,
    listar_informacoes,
    pesquisar_por_tipo,
    iniciar_quiz,
    perguntar_com_tempo,
    limpar_tela,
    carregar_dados,        # NOVO
    editar_informacao,     # NOVO
    excluir_informacao,    # NOVO
    VERDE,
    VERMELHO,
    AMARELO,
    CIANO,
    RESET
)

import time

informacoes = carregar_dados()


def menu():
    while True:
        limpar_tela()
        print(CIANO + '='*40)
        print('           TOTEM FLEXMEDIA')
        print('='*40 + RESET)

        print(AMARELO + '1 - Cadastrar informação' + RESET)
        print(AMARELO + '2 - Listar informações cadastradas' + RESET)
        print(AMARELO + '3 - Pesquisar informações por tipo' + RESET)
        print(AMARELO + '4 - Editar informação' + RESET)     # NOVO
        print(AMARELO + '5 - Excluir informação' + RESET)    # NOVO
        print(AMARELO + '0 - Sair' + RESET)

        print(CIANO + '='*40 + RESET)

        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            cadastrar_informacao(informacoes)

        elif opcao == '2':
            listar_informacoes(informacoes)

        elif opcao == '3':
            pesquisar_por_tipo(informacoes)

        elif opcao == '4':
            editar_informacao(informacoes)
            input('\nPressione Enter para continuar...')

        elif opcao == '5': 
            excluir_informacao(informacoes)
            input('\nPressione Enter para continuar...')

        elif opcao == '0':
            resposta = perguntar_com_tempo(
                AMARELO + '\nAntes de encerrar, gostaria de fazer o quiz?\nResponda "sim" ou "não" (encerra em 7s): ' + RESET
            )

            if resposta in ['s', 'sim']:
                iniciar_quiz()

            limpar_tela()
            print(VERDE + '\n👋 Encerrando o programa... Até logo!\n' + RESET)
            time.sleep(1)
            break

        else:
            print(VERMELHO + '\n⚠️ Opção inválida! Tente novamente.\n' + RESET)
            time.sleep(1)


if __name__ == '__main__':
    menu()
