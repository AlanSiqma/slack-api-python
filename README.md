# Envio mensagens Slack Python 🐍
## O que é ?
O envio de mensagens para o Slack usando Python é um processo de automatização no qual você pode programar um script em Python para enviar mensagens para canais específicos no Slack. 

## E esse bot o que faz? 
Responsavel por mandar mensagens para o grupo

## Configurações

### 1- Criar um Webhook no Slack::

1. Acesse o painel de configurações de webhooks do Slack.
2. Selecione para qual canal do Slack você deseja enviar as mensagens e clique em "Adicionar Webhook para Canal".
3. Copie o URL do webhook gerado.

### 2- Instale o Python

[Clique aqui](https://www.python.org/downloads/), e você será redirecionado para a instalação do Python.

### 3- Baixe alguns pacotes

No CMD, digite os comandos:
```
pip install requests
```
```
pip install python-dotenv
```

### 4- Crie as variaveis de ambientes

Na raiz do projeto crie um arquivo .env
nele você ira adicionar:
```
webhook = "a URL que você pegou no passo 1"
```