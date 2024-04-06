# Sistema de Gerenciamento de Placas - DETRAN

Este repositório contém um sistema de gerenciamento de placas de veículos que segue o padrão Mercosul. O sistema foi desenvolvido como parte de um projeto para a disciplina de Linguagens Formais, Autômatos e Teoria da Computabilidade. O objetivo é fornecer um exemplo prático de como as expressões regulares podem ser aplicadas em programas reais, como a validação de formatos de placas de veículos.

## Contexto

O Departamento Estadual de Trânsito (DETRAN) necessita de uma ferramenta para validar as placas de veículos registradas no padrão Mercosul. Este sistema permite adicionar, remover, consultar e validar as placas de veículos dentro de um repositório centralizado.

## Estrutura do Código

O sistema é composto por várias funções integradas em uma interface de linha de comando simples:

- `validar_placas(placas)`: Valida uma lista de placas de veículos de acordo com a expressão regular definida para o padrão Mercosul.

- `adicionar_placa(placa)`: Adiciona uma nova placa ao conjunto de placas caso ela não exista.

- `remover_placa(placa)`: Remove uma placa existente do conjunto.

- `consultar_placas()`: Retorna uma lista de todas as placas atualmente armazenadas no sistema.

- `validar_cadastro()`: Realiza a validação de todas as placas cadastradas, removendo automaticamente as que são inválidas.

- `menu()`: Fornece uma interface de linha de comando para o usuário interagir com o sistema.

O sistema opera através de um menu principal onde o usuário pode escolher entre adicionar, remover, consultar placas ou validar o cadastro de placas.

## Expressão Regular

A expressão regular utilizada para a validação das placas no padrão Mercosul é `^[A-Za-z]{3}\d[A-Za-z]\d{2}$`. Isso garante que a placa comece com três letras (maiúsculas ou minúsculas), seguida por um dígito, mais uma letra (maiúscula ou minúscula) e terminando com dois dígitos. 

## Como Executar

Para executar este sistema, você precisa ter Python instalado em sua máquina. Não são necessárias dependências externas além do módulo `re`, que é parte da biblioteca padrão do Python.

1. Clone o repositório ou baixe os arquivos para sua máquina local.
2. Navegue até o diretório contendo o script.
3. Execute o comando `python nome_do_arquivo.py` no terminal.

## Conclusão

Este projeto demonstra a aplicabilidade das expressões regulares e conceitos da teoria da computabilidade na implementação de sistemas reais. Através deste sistema, estudantes e profissionais podem entender como linguagens formais e autômatos são essenciais no desenvolvimento de soluções computacionais para problemas do mundo real.


