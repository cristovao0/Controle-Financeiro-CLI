# 💰 Controle Financeiro CLI em Python

Projeto de linha de comando (CLI) desenvolvido em Python para controle financeiro pessoal, permitindo registrar movimentações financeiras, visualizar relatórios e calcular saldos de forma simples e organizada.

---

## 🎯 Objetivo do Projeto

Criar um sistema de controle financeiro utilizando:
- Python puro
- Persistência de dados em JSON
- Boas práticas de organização de código
- Separação entre lógica, apresentação e persistência

O projeto foi pensado como exercício prático para consolidar fundamentos de Python e evoluir para conceitos mais modernos.

---

## ⚙️ Funcionalidades

- ➕ Adicionar movimentações financeiras (entrada ou saída)
- 📋 Listar todas as movimentações cadastradas
- 📈 Calcular total de entradas
- 📉 Calcular total de saídas
- 💵 Calcular saldo atual
- 📊 Exibir resumo financeiro consolidado
- 💾 Persistência de dados em arquivo JSON
- 🎨 Interface no terminal com formatação e cores

---

## 🗂 Estrutura do Projeto

Controle-Financeiro-CLI/
│
├── main.py # Menu principal e interação com o usuário
├── funcoes.py # Regras de negócio e cálculos financeiros
├── formatacao.py # Funções de formatação visual do terminal
├── movimentos.json # Arquivo de persistência de dados
└── README.md # Documentação do projeto

---

## ▶️ Como Executar

1. Clone o repositório

```
	bash
git clone https://github.com/seu-usuario/controle-financeiro-cli.git
```

2. Acesse a pasta do projeto:

```
	bash
cd controle-financeiro-CLI
```

3. Execute o programa:

```
	bash
	python main.py
```

---

🚀 Possíveis Melhorias Futuras

-> Exportar dados para CSV

-> Gráficos financeiros

-> Filtros por data ou tipo

-> Interface gráfica (GUI)

-> Integração com banco de dados

---

👨‍💻 Autor

Cristovão Cavalcante

Projeto desenvolvido como parte de estudos em Python e lógica de programação.