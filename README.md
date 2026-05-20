# 📘 Totem_Prototipo

## 🎯 Objetivo

Criar um protótipo de **totem inteligente interativo** em Python que oferece informações **educativas**, **culturais** e de **lazer**, permitindo o **cadastro**, **listagem**, **pesquisa**, **edição** e **exclusão** dessas informações diretamente no terminal.

A partir desta Sprint, o sistema passa a contar com **persistência de dados em JSON**, garantindo que as informações não sejam perdidas ao encerrar o programa, tornando-o mais próximo de um sistema real.

---

## 📦 Entrega da Sprint 3: Funcionalidades

### 🧩 Organização e Modularização

O projeto está dividido em múltiplos arquivos:

* `main.py`: menu principal e fluxo do programa
* `funcoes.py`: lógica do sistema (cadastro, persistência, edição, exclusão, etc.)
* `quiz_flexmedia.py`: quiz interativo com Streamlit
* `dados.json`: armazenamento permanente das informações
* `logo_flexmedia.png`: logo do quiz
* `README.md`: documentação do projeto

---

### 💾 Persistência de Dados (NOVO)

* Os dados são salvos automaticamente no arquivo `dados.json`.
* Ao iniciar o sistema:

  * Os dados são carregados automaticamente.
* Ao cadastrar, editar ou excluir:

  * O arquivo é atualizado automaticamente.
* Tratamento de erros:

  * Caso o arquivo não exista ou esteja corrompido, o sistema recria os dados.

---

### 📝 Cadastro de Informações

* Permite registrar:

  * **Título**
  * **Tipo** (validação: educativo, cultural ou lazer)
  * **Descrição**
* Validação impede campos vazios ou tipos inválidos.
* Feedback visual com animação de carregamento.

---

### 📋 Listagem Estilizada

* Exibe todas as informações cadastradas.
* Formatação com cores ANSI para melhor visualização.
* Caso não haja dados, informa o usuário.

---

### 🔍 Pesquisa por Tipo

* Permite filtrar informações por:

  * educativo
  * cultural
  * lazer
* Exibe apenas os resultados correspondentes.

---

### ✏️ Edição de Informações (NOVO)

* O usuário pode selecionar um registro pelo índice.
* O sistema exibe os dados atuais.
* Permite:

  * alterar os campos
  * ou manter os valores pressionando Enter
* Mantém todas as validações da Sprint anterior.

---

### 🗑️ Exclusão de Informações (NOVO)

* Lista os registros disponíveis.
* Permite escolher qual excluir.
* Solicita confirmação antes da exclusão.
* Atualiza automaticamente o arquivo JSON.

---

### 🎮 Quiz Interativo – Totem FlexMedia

* Ao sair, o sistema oferece um quiz interativo.
* Executado via **Streamlit** no navegador.
* Feedback visual e interativo.
* Cria o arquivo `quiz_finalizado.txt` ao terminar.

---

## 🧠 Menu Principal

```
1 - Cadastrar informação
2 - Listar informações cadastradas
3 - Pesquisar informações por tipo
4 - Editar informação
5 - Excluir informação
0 - Sair
```

---

## 🛠 Tecnologias Utilizadas

* **Linguagem:** Python 3.x
* **Bibliotecas:**

  * Streamlit
  * Pillow
  * JSON (nativo do Python)
* **Estilização:** ANSI (cores no terminal)

---

## ⚙️ Como Executar o Projeto

### 🪄 Pré-requisitos

Instale as dependências:

```bash
pip install streamlit pillow
```

---

### ▶️ Executar o Totem

```bash
python main.py
```

---

### 🧩 Executar o Quiz Separadamente

```bash
streamlit run quiz_flexmedia.py
```

---

## 📊 Exemplo de Uso

```bash
========================================
           TOTEM FLEXMEDIA
========================================
1 - Cadastrar informação
2 - Listar informações cadastradas
3 - Pesquisar informações por tipo
4 - Editar informação
5 - Excluir informação
0 - Sair
========================================
Escolha uma opção: 1
```

---

## 🚀 Evolução do Projeto

* ✅ Sprint 1: Cadastro e listagem
* ✅ Sprint 2: Pesquisa, modularização e quiz
* ✅ Sprint 3: Persistência, edição e exclusão (CRUD completo)

---

## 👨‍💻 Desenvolvido

**João Pedro de Souza Nunes**
