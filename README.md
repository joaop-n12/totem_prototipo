# 📘 Totem FlexMedia

## 🎯 Objetivo
Criar um protótipo de **totem inteligente interativo** em Python para oferecer informações educativas, culturais e de lazer, permitindo o cadastro e listagem dessas informações diretamente no terminal, com cores e efeitos simples para melhorar a experiência do usuário.

---

## 📦 Entrega da Sprint 1: Funcionalidades

Nesta primeira etapa, o programa em Python (`totemflexmedia.py`) possui as seguintes funcionalidades:

* 🏠 **Menu Interativo:** Navegação simples entre as opções.
* 📝 **Cadastro de Informações:** Permite registrar dados de `Título`, `Tipo` (com validação de tipos permitidos) e `Descrição`, armazenados em uma lista de dicionários. Após cada cadastro, é perguntado se deseja adicionar mais informações.
* 📄 **Listagem Estilizada:** Exibe todas as informações cadastradas de forma organizada, utilizando cores para destaque de acordo com o tipo:
  - Educativo: 🔵 Azul  
  - Cultural: 💜 Magenta  
  - Lazer: 🟡 Amarelo  
  - Esportivo: 🟢 Verde  
  - Informativo: 🔹 Ciano  
  - Tecnológico: 💜 Magenta
* 🔁 **Fluxo Contínuo:** Permite cadastrar ou listar informações consecutivamente através de laços `while`.
* 📊 **Controle de Dados:** Implementa um contador que mostra o número total de informações registradas.
* 🎨 **Efeito de Carregamento:** Mensagens animadas de "Carregando..." ao salvar informações.
* ⌨️ **Interatividade:** O usuário pode voltar ao menu principal após listar informações.

---

## 🛠 Tecnologias Utilizadas
* **Linguagem:** Python 3.x  
* **Estilização:** Códigos ANSI para cores no terminal  
* **Terminal:** Windows, Linux ou macOS  

---

## ⚙️ Como Executar

Para rodar o projeto, siga os passos abaixo no seu terminal:

1. Baixe ou clone este repositório.  
2. Navegue até a pasta do projeto.  
3. Execute o arquivo principal com o comando:

```bash
python totemflexmedia.py
```

Siga as instruções do menu interativo:
1 para cadastrar informação  
2 para listar informações  
0 para sair

---

##📌 Exemplo de Uso
```bash
========================================
           TOTEM FLEXMEDIA
========================================
1 - Cadastrar informação
2 - Listar informações cadastradas
0 - Sair
========================================
Escolha uma opção: 1

       CADASTRO DE INFORMAÇÃO
========================================
Digite o título da informação: Aula de Python
Tipos disponíveis: educativo, cultural, lazer, esportivo, informativo, tecnológico
Digite o tipo: educativo
Digite uma breve descrição: Aprender conceitos básicos de Python

Salvando informação...
✅ Informação cadastrada com sucesso! Total de cadastros: 1

Deseja cadastrar outra informação? (S/N): N
