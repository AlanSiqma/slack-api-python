import requests
import json
import os
import dotenv

dotenv.load_dotenv()

mensagem = {"text": "Ola, bem vindo"}
webhook = os.getenv('webhook')

requests.post(webhook, data=json.dumps(mensagem))
