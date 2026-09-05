# Sistema de Gerenciamento de Biblioteca em Python

Aplicação de terminal desenvolvida em Python para gerenciar livros, usuários, empréstimos, devoluções e relatórios de uma biblioteca.

O projeto foi desenvolvido como atividade acadêmica para aplicar conceitos de lógica de programação, estruturas de dados, funções, validação de entradas e manipulação de arquivos CSV.

## Funcionalidades

- Cadastro de livros e usuários;
- Bloqueio de códigos e matrículas duplicados;
- Registro de empréstimos e devoluções;
- Verificação da disponibilidade dos livros;
- Relatórios de livros disponíveis e emprestados;
- Exportação de relatórios em formato CSV;
- Menu interativo executado no terminal.

## Tecnologias utilizadas

- Python 3.14;
- Biblioteca padrão `csv`;
- PyCharm;
- Git e GitHub.

O projeto não utiliza dependências externas.

## Como executar

É necessário ter o Python 3.12 ou superior instalado.

Clone ou baixe este repositório, abra o terminal na pasta do projeto e execute:

```bash
python3 sistema_biblioteca.py
```

O menu principal será exibido:

```text
1. Cadastrar Livro
2. Cadastrar Usuário
3. Realizar Empréstimo
4. Realizar Devolução
5. Gerar Relatórios
6. Salvar Relatórios CSV
7. Sair
```

## Conceitos aplicados

- Funções e reutilização de código;
- Dicionários;
- Estruturas condicionais e de repetição;
- Validação de entradas;
- Manipulação de strings;
- Alteração do estado dos registros;
- Entrada de dados pelo terminal;
- Escrita e exportação de arquivos CSV.

## Armazenamento dos dados

Os livros e usuários permanecem armazenados em memória durante a execução do programa. Ao encerrar a aplicação, esses dados são descartados.

Os relatórios podem ser exportados para arquivos CSV.

## Possíveis melhorias

- Validar as datas de devolução;
- Armazenar os dados permanentemente;
- Integrar o sistema a um banco de dados;
- Registrar atrasos e multas;
- Implementar testes automatizados;
- Separar as funcionalidades em módulos;
- Desenvolver uma interface gráfica ou web.

## Observação

Os dados utilizados nas demonstrações são fictícios e destinados exclusivamente a fins acadêmicos.

## Autoria

Desenvolvido por **Larissa da Silva Santos** como atividade acadêmica da disciplina de Lógica, Algoritmo e Programação de Computadores.