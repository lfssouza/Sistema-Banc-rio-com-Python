# 🛠️ Sistema Bancário em Python
---
Projeto desenvolvido como parte do desafio da plataforma DIO. O objetivo é simular um sistema bancário simples com as funcionalidades de **depósito**, **saque** e **visualização de extrato**.

---

## 🧭 Tabela de Conteúdos
- [📘 Contexto](#-contexto)
- [🎯 Objetivo](#-objetivo)
- [🧱 Estrutura do Modelo](#-estrutura-do-modelo)
- [🗂️ Arquivos do Projeto](#-arquivos-do-projeto)
- [💡 Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [📊 Exemplo de Caso de Uso](#-exemplo-de-caso-de-uso)
- [🧑‍💻 Autor](#-autor)

---

## 📘 Contexto
Este projeto foi desenvolvido para atender a um desafio da DIO (Digital Innovation One), no qual fomos contratados por um banco fictício para criar um sistema simples de controle de conta bancária utilizando a linguagem Python.

---

## 🎯 Objetivo
Criar um sistema bancário básico que permita:
- Depósitos de valores positivos.
- Até 3 saques diários com limite de R$500 por saque.
- Consulta de extrato (listagem das movimentações e saldo atual)

---

## 🧱 Estrutura do Modelo
- ✅ **Depósito**:
  - Permite depositar valores positivos.
  - Confirmação manual do usuário antes de efetivar o depósito.
  - Registro da movimentação no extrato.

- ✅ **Saque**:
  - Limite de 3 saques diários.
  - Valor máximo por saque: R$ 500,00.
  - Verificação de saldo suficiente.
  - Confirmação manual do usuário.
  - Registro da movimentação no extrato.

- ✅ **Extrato**:
  - Exibe todas as movimentações realizadas.
  - Exibe o saldo atual da conta.
  - Se não houver movimentações, exibe uma mensagem adequada.

- ✅ **Validações**:
  - Tratamento de valores inválidos.
  - Opções de menu com controle de erros.
  - Mensagens claras ao usuário.

---

## 🗂️ Arquivos do Projeto
- `Criando um Sistema Bancário.py`: Arquivo principal com a lógica do sistema bancário.
- `README.md`: Este arquivo de documentação.

---

## 💡 Tecnologias Utilizadas
- Python 3.10+
- Visual Studio Code

---

## 📊 Exemplo de Caso de Uso

```bash
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> 1
Valor a ser depositado: 1000
Deseja depositar o valor: R$1000.00? (S/N) 
s
Valor de 1000.00, foi depósitado com sucesso!


[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> 2
Valor que deseja sacar: 400
Deseja sacar o valor: R$400.00? (S/N) 
s
Valor de R$ 400.00, foi sacado com sucesso!


[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> 3
Seu extrato é:

Depósito: R$ 1000.00
Saque: R$400.00

O saldo atual da conta: R$ 600.00
```

🧑‍💻 Autor
**Luis Fernando Sosnoski de Souza**
Curso: Santander 2025 - Back-End com Python
