# 📘 Totem_Prototico

## 🎯 Objetivo
Criar um protótipo de **totem inteligente interativo** em Python que oferece informações **educativo**, **cultural** e de **lazer**, permitindo o **cadastro**, **listagem** e **pesquisa** dessas informações diretamente no terminal, com cores e efeitos simples para melhorar a experiência do usuário.  
Nesta Sprint, o sistema também foi **modularizado** e ganhou um **quiz interativo** desenvolvido com **Streamlit**.

---

## 📦 Entrega da Sprint 2: Funcionalidades

### 🧩 Organização e Modularização
O projeto foi dividido em múltiplos arquivos:
- `main.py`: menu principal e fluxo do programa  
- `funcoes.py`: funções de cadastro, listagem, pesquisa e integração com o quiz  
- `quiz_flexmedia.py`: quiz interativo com perguntas sobre o Totem FlexMedia  
- `logo_flexmedia.png`: logo exibida no quiz  
- `README.md`: documentação do projeto

---

### 📝 Cadastro de Informações
- Permite registrar dados de:
  - **Título**
  - **Tipo** (com validação — aceita apenas `educativo`, `cultural` ou `lazer`)
  - **Descrição**
- Após cada cadastro, o sistema pergunta se o usuário deseja cadastrar outra informação.
- Mostra mensagens animadas de **“Salvando informação...”** com efeito de carregamento.

---

### 📋 Listagem Estilizada
- Exibe todas as informações cadastradas com cores e formatação organizada.
- Caso não existam cadastros, informa que a lista está vazia.
- O usuário pode pressionar **Enter** para retornar ao menu principal.

---

### 🔍 Pesquisa por Tipo
- Nova funcionalidade da Sprint 2.  
- Permite buscar informações cadastradas filtrando por **educativo**, **cultural** ou **lazer**.  
- Exibe apenas os resultados correspondentes ao tipo informado.

---

### 🎮 Quiz Interativo – Totem FlexMedia
- Ao escolher a opção **Sair**, o sistema pergunta se o usuário deseja fazer um **quiz interativo**.  
- O quiz é aberto automaticamente no navegador com **Streamlit**.  
- Possui perguntas sobre o projeto Totem FlexMedia e fornece feedback visual e sonoro.  
- Ao finalizar, é criado um arquivo `quiz_finalizado.txt` que indica a conclusão.

---

## 🧠 Menu Principal

```
1 - Cadastrar informação
2 - Listar informações cadastradas
3 - Pesquisar informações por tipo
0 - Sair
```

O programa só é encerrado quando a opção **0 – Sair** é selecionada.

---

## 🛠 Tecnologias Utilizadas
- **Linguagem:** Python 3.x  
- **Bibliotecas:** Streamlit, Pillow (para a logo do quiz)  
- **Estilização:** Códigos ANSI para cores no terminal  
- **Terminal:** Windows, Linux ou macOS  

---

## ⚙️ Como Executar o Projeto

### 🪄 Pré-requisitos
Instale as dependências:
```bash
pip install streamlit pillow
```

---

### ▶️ Executar o Totem
No terminal, dentro da pasta do projeto:
```bash
python main.py
```

---

### 🧩 Executar o Quiz Separadamente
Se quiser abrir o quiz diretamente:
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
0 - Sair
========================================
Escolha uma opção: 1

       CADASTRO DE INFORMAÇÃO
========================================
Digite o título da informação: Aula de Python
Tipos disponíveis: educativo, cultural, lazer
Digite o tipo: educativo
Digite uma breve descrição: Aprender conceitos básicos de Python

Salvando informação...
✅ Informação cadastrada com sucesso! Total de cadastros: 1

Deseja cadastrar outra informação? (S/N): N
```

---

## 👨‍💻 Autor
**João Pedro de Souza Nunes**  
📚 Projeto desenvolvido para a **Sprint 2 – FIAP | Machine Learning e Python**.
