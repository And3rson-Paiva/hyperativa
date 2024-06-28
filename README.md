# Card API

## Descrição
Card API é uma aplicação Django projetada para lidar com operações envolvendo números de cartões, incluindo verificação de existência e cadastro de novos números.

## Configuração Inicial

### Ambiente Virtual
Para configurar o ambiente virtual e instalar as dependências, no terminal execute:

python -m venv venv
source venv/bin/activate  # No Windows use `venv\Scripts\activate`
pip install -r requirements.txt

## Configuração do Banco de Dados
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nome_do_banco',
        'USER': 'usuario',
        'PASSWORD': 'senha',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

## Migrações
Para criar as tabelas no banco de dados, execute:
python manage.py makemigrations
python manage.py migrate

## Criar usuário

Para criar usuário que será solicitado posteriormente:
python manage.py createsuperuser

## Rodar o Servidor
Para iniciar o servidor Django, utilize:
python manage.py runserver


## Fazer Requisições

Para gerar o token de aceso:

curl -X POST http://localhost:8000/api/token/      
     -H "Content-Type: application/json"      
     -d '{"username": "seu_usuario", "password": "sua_senha"}'

Para enviar uma requisição POST para adicionar um número de cartão:

curl -X POST 'http://localhost:8000/api/cards/' \
     -H 'Content-Type: application/json' \
     -H 'Authorization: Bearer seu_token' \
     -d '{"card_number": "1234567890123456"}'

Para verificar se um número de cartão existe:

curl -X GET 'http://localhost:8000/api/cards/check/1234567890123456/' \
     -H 'Authorization: Bearer seu_token'









