# 💰 Controle Financeiro CLI em Python (POO)

Projeto de linha de comando (CLI) desenvolvido em Python para controle financeiro pessoal,
refatorado utilizando **Programação Orientada a Objetos (POO)** para melhor organização,
manutenção e reutilização do código.

---

## 🎯 Objetivo do Projeto

Criar um sistema simples de controle financeiro que permita:
- registrar entradas e saídas
- armazenar dados em arquivo JSON
- calcular totais e saldo
- exibir relatórios financeiros

O projeto foi desenvolvido com foco em **boas práticas de programação** e **aprendizado progressivo de POO**.

---

## ⚙️ Funcionalidades

- ➕ Adicionar movimentações financeiras (entrada ou saída)
- 📋 Listar todas as movimentações
- 📈 Calcular total de entradas
- 📉 Calcular total de saídas
- 💵 Calcular saldo atual
- 📊 Exibir resumo financeiro consolidado
- 💾 Persistência de dados em arquivo JSON
- 🎨 Interface no terminal com formatação e cores

---

## 🧠 Conceitos Aplicados

- Programação Orientada a Objetos (POO)
- Encapsulamento
- Responsabilidade única
- Leitura e escrita de arquivos JSON
- Tratamento de erros (`try/except`)
- Separação entre lógica de negócio e interface
- Código reutilizável e modular

---

## 🗂 Estrutura do Projeto

Controle-Financeiro-CLI/
│
├── main.py # Menu e interação com o usuário
├── ControleFinanceiro.py # Classe principal (lógica financeira e persistência)
├── formatacao.py # Funções de formatação do terminal
├── movimentos.json # Arquivo de dados
└── README.md # Documentação do projeto


---

## ▶️ Como Executar

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/controle-financeiro-cli.git
```
2. Acesse a pasta:
``` bash
cd Controle-Financeiro-CLI
```
3. Execute o programa:
``` bash
python main.py
```
🚀 Aprendizados:

Este projeto foi inicialmente desenvolvido de forma procedural e,
posteriormente, refatorado para POO, permitindo:

-> redução de código repetido

-> melhor organização

-> maior clareza das responsabilidades

-> facilidade de manutenção e expansão

👨‍💻 Autor
Cristovão Cavalcante
Projeto desenvolvido como parte dos estudos em Python e Programação Orientada a Objetos.