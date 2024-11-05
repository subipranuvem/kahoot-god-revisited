# Kahoot God - Revisited

## Descrição do Projeto

Este projeto é uma releitura inspirada no vídeo ["Using AI to NEVER LOSE in KAHOOT"](https://www.youtube.com/watch?v=G0i_xx-6G-4) do canal: [The Coding Sloth](https://www.youtube.com/@TheCodingSloth) no YouTube.

Essa versão traz algumas melhorias e adaptações:

- **Uso do Selenium**: Em vez de [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/) + [Tesseract](https://pypi.org/project/pytesseract/) para obter questões e alternativas, o Selenium foi utilizado. Isso democratiza o acesso ao código, permitindo que funcione em qualquer resolução de tela, diferentemente da versão original que era limitada a telas 1440p.

- **API Gemini**: Substituída a API paga do ChatGPT pela API gratuita do Gemini. Você pode obter uma chave seguindo este [passo-a-passo](https://ai.google.dev/gemini-api/docs/api-key?hl=pt-br).

- **Automação com Selenium**: Para selecionar as alternativas corretas, o Selenium foi utilizado em vez de PyAutoGUI, proporcionando maior precisão e confiabilidade.

**Nota**: Devido ao uso do Selenium, este código **não pode ser executado em servidores sem interface gráfica**.

## Instalando Dependências com pip e requirements.txt

Para instalar todas as dependências listadas no arquivo `requirements.txt` de uma só vez, você pode usar o comando: `python -m pip install -r requirements.txt`. Este é um método bem eficiente e simples para configurar ambientes de desenvolvimento Python.

1. Certifique-se de que você está no diretório do projeto onde o arquivo `requirements.txt` está localizado.
1. Crie um ambiente virtual (pasta `.venv`) com o seguinte comando no terminal:
    ```shell
    python -m venv .venv
    ```
1. Ative seu ambiente virtual (se estiver usando um):
    - Windows
        ```shell
        .\.venv\Scripts\activate.ps1
        ```
    - Ubuntu
        ```shell
        source .venv/bin/activate
        ```
1. Execute o seguinte comando no terminal:
    ```
    python -m pip install -r requirements.txt
    ```
1. O pip lerá o arquivo `requirements.txt` e instalará todas as dependências listadas nele.


## Variáveis de Ambiente

As variáveis de ambiente podem ser configuradas via arquivo `.env` ou diretamente no sistema operacional.

| Nome da Variável | Descrição | Obrigatoriedade |
|------------------|-----------|-----------------|
| GEMINI_API_KEY   | Chave de API do Gemini | Obrigatório |

## Opções de Execução

O programa aceita 0 ou 1 argumento, sendo este a URL opcional do Quiz do Kahoot.

### Com URL fornecida:

```shell
python app.py https://kahoot.it/challenge/?quiz-id=70cf378f-8c24-4d5d-9426-5718ae4b432c&single-player=true
```

### Sem URL fornecida:

```shell
python app.py
```

Neste caso, um prompt solicitará a URL:

```shell
Enter the quiz URL:
```

## Instruções de Uso

1. Quando a questão aparecer no Kahoot com todas as alternativas na tela, pressione `Ctrl + Shift + Z` com o foco no terminal.

2. Para sair do programa, pressione `Ctrl + C` ou `Ctrl + V`.
