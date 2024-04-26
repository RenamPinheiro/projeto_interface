Projeto Interface 
=======================

Este é um aplicativo simples de análise de investimento que utiliza a biblioteca yfinance para obter dados de mercado e tkinter para criar a interface gráfica.

Requisitos
----------

*   Bibliotecas: requests, tkinter, yfinance

Instalação das Bibliotecas
--------------------------

Você pode instalar as bibliotecas necessárias executando o seguinte comando:

```
pip install requests 
pip install tkinter 
pip install yfinance
```

Utilização
----------

1.  Execute o script Python.
2.  Insira o ticker da ação que deseja analisar no campo "Ticker".
3.  Selecione o período desejado clicando nos botões com os períodos disponíveis (1d, 5d, 3m, 6m, 1a, 5a).
4.  Clique no botão "Confirmar" para visualizar as informações sobre o investimento.

Funcionamento do Código
-----------------------

O código consiste em uma aplicação GUI que permite ao usuário inserir o ticker de uma ação e escolher o período desejado para análise. Após confirmar a seleção, o programa utiliza a biblioteca yfinance para obter os dados históricos da ação e exibe as informações relevantes, como a cotação máxima, mínima e atual.

Estrutura do Código
-------------------

*   `analise_investimento()`: Função que realiza a análise do investimento com base no ticker inserido e no período selecionado.
*   `definir_tempo(periodo)`: Função que define o período de análise com base no botão clicado pelo usuário.
*   Interface GUI utilizando a biblioteca tkinter para criar janelas, frames, labels, entry e botões.

Captura de Tela da Interface
----------------------------

Aqui está uma captura de tela da interface do aplicativo de análise de investimento:

![image](https://github.com/RenamPinheiro/projeto_interface/assets/118815226/77498ffb-8a8e-4910-85e2-6cd44c0fedf8)

Esta captura de tela mostra a interface gráfica do programa, onde os usuários podem inserir o ticker (um código único usado para identificar uma empresa listada na bolsa de valores) da ação, selecionar o período desejado e visualizar as informações de análise de investimento.
