import time
import os
import sys
import subprocess
import threading
import webbrowser
import json  # NOVO

ARQUIVO = "dados.json"  # NOVO

VERDE = '\033[32m'
VERMELHO = '\033[31m'
AMARELO = '\033[33m'
CIANO = '\033[36m'
RESET = '\033[0m'


# -------------------------
# PERSISTÊNCIA (NOVO)
# -------------------------

def carregar_dados():
    if not os.path.exists(ARQUIVO):
        return []

    try:
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        print("Erro ao carregar dados. Criando novo arquivo...")
        return []


def salvar_dados(lista):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(lista, f, indent=4, ensure_ascii=False)


# -------------------------
# FUNÇÕES EXISTENTES
# -------------------------

def limpar_tela():
    os.system('cls' if sys.platform == 'win32' else 'clear')


def carregando(mensagem='Carregando'):
    print(AMARELO + mensagem, end='', flush=True)
    for _ in range(3):
        time.sleep(0.5)
        print('.', end='', flush=True)
    print(RESET)
    time.sleep(0.5)


def perguntar_com_tempo(pergunta, tempo_limite=7):
    resposta = [None]

    def ler_input():
        resposta[0] = input(pergunta).strip().lower()

    thread = threading.Thread(target=ler_input)
    thread.start()
    thread.join(timeout=tempo_limite)
    return resposta[0]


def iniciar_quiz():
    caminho_arquivo = "quiz_flexmedia.py"
    marcador = "quiz_finalizado.txt"

    if os.path.exists(marcador):
        os.remove(marcador)

    limpar_tela()
    print(AMARELO + "Abrindo quiz interativo no navegador..." + RESET)
    time.sleep(1)

    processo = subprocess.Popen(
        ["streamlit", "run", caminho_arquivo, "--server.headless", "true"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    webbrowser.open("http://localhost:8501", new=2)

    print(CIANO + "Aguardando finalização do quiz..." + RESET)
    while not os.path.exists(marcador):
        time.sleep(1)

    processo.terminate()
    time.sleep(0.5)
    limpar_tela()
    print(VERDE + "\n✅ Quiz finalizado com sucesso!\n" + RESET)
    print("👋 Encerrando o programa... Até logo!\n")
    time.sleep(1)


def cadastrar_informacao(lista):
    while True:
        limpar_tela()
        print(CIANO + '='*40)
        print('       CADASTRO DE INFORMAÇÃO')
        print('='*40 + RESET + '\n')

        while True:
            titulo = input('Digite o título da informação: ').strip()
            if titulo:
                break
            else:
                print(VERMELHO + '⚠️ O título não pode estar vazio!\n' + RESET)

        tipos_permitidos = ['educativo', 'cultural', 'lazer']
        print('\nTipos disponíveis:', ', '.join(tipos_permitidos))

        while True:
            tipo_input = input('Digite o tipo: ').strip().lower()
            if tipo_input in tipos_permitidos:
                tipo = tipo_input.capitalize()
                break
            else:
                print(VERMELHO + f'\n⚠️ Tipo inválido! Use: {", ".join(tipos_permitidos)}.' + RESET)

        descricao = input('\nDigite uma breve descrição: ').strip()

        info = {'Título': titulo, 'Tipo': tipo, 'Descrição': descricao}
        lista.append(info)

        salvar_dados(lista)  # 🔥 IMPORTANTE

        carregando('\nSalvando informação')
        print(VERDE + f'\n✅ Informação cadastrada com sucesso! Total: {len(lista)}\n' + RESET)

        continuar = input('Deseja cadastrar outra informação? (S/N): ').strip().lower()
        if continuar not in ['s', 'sim']:
            break


def listar_informacoes(lista):
    limpar_tela()
    print(CIANO + '='*40)
    print('       INFORMAÇÕES CADASTRADAS')
    print('='*40 + RESET + '\n')

    if not lista:
        print(AMARELO + 'Nenhuma informação cadastrada ainda.\n' + RESET)
    else:
        for i, info in enumerate(lista, 1):
            print(f'{i}. {info["Título"]} ({info["Tipo"]})')
            print(f'   Descrição: {info["Descrição"]}\n')
            time.sleep(0.2)
    input('Pressione Enter para voltar ao menu...')


def pesquisar_por_tipo(lista):
    limpar_tela()
    print(CIANO + '='*40)
    print('       PESQUISA POR TIPO')
    print('='*40 + RESET + '\n')

    tipos_permitidos = ['educativo', 'cultural', 'lazer']
    tipo_busca = input('Digite o tipo que deseja buscar: ').strip().lower()

    if tipo_busca not in tipos_permitidos:
        print(VERMELHO + f'\n⚠️ Tipo inválido! Use: {", ".join(tipos_permitidos)}.' + RESET)
        input('\nPressione Enter para voltar ao menu...')
        return

    resultados = [i for i in lista if i["Tipo"].lower() == tipo_busca]

    if not resultados:
        print(AMARELO + f'\nNenhuma informação encontrada para "{tipo_busca}".\n' + RESET)
    else:
        print(VERDE + f'\nResultados para "{tipo_busca}":\n' + RESET)
        for i, info in enumerate(resultados, 1):
            print(f'{i}. {info["Título"]} - {info["Descrição"]}')
    input('\nPressione Enter para voltar ao menu...')


# -------------------------
# EDIÇÃO (NOVO)
# -------------------------

def editar_informacao(lista):
    if not lista:
        print("Nenhuma informação cadastrada.")
        return

    for i, item in enumerate(lista):
        print(f"{i} - {item['Título']}")

    try:
        indice = int(input("Escolha o índice para editar: "))
        if indice < 0 or indice >= len(lista):
            print("Índice inválido.")
            return
    except ValueError:
        print("Entrada inválida.")
        return

    info = lista[indice]

    print(f"\nTítulo atual: {info['Título']}")
    novo_titulo = input("Novo título (Enter para manter): ")
    if novo_titulo:
        info['Título'] = novo_titulo

    print(f"Tipo atual: {info['Tipo']}")
    novo_tipo = input("Novo tipo: ")
    if novo_tipo.lower() in ['educativo', 'cultural', 'lazer']:
        info['Tipo'] = novo_tipo.capitalize()

    print(f"Descrição atual: {info['Descrição']}")
    nova_desc = input("Nova descrição: ")
    if nova_desc:
        info['Descrição'] = nova_desc

    salvar_dados(lista)
    print("✅ Informação atualizada!")


# -------------------------
# EXCLUSÃO (NOVO)
# -------------------------

def excluir_informacao(lista):
    if not lista:
        print("Nenhuma informação cadastrada.")
        return

    for i, item in enumerate(lista):
        print(f"{i} - {item['Título']}")

    try:
        indice = int(input("Escolha o índice para excluir: "))
        if indice < 0 or indice >= len(lista):
            print("Índice inválido.")
            return
    except ValueError:
        print("Entrada inválida.")
        return

    confirmacao = input("Tem certeza? (s/n): ")

    if confirmacao.lower() == "s":
        lista.pop(indice)
        salvar_dados(lista)
        print("🗑️ Excluído com sucesso!")
    else:
        print("Cancelado.")
