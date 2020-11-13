## 📚  Descrição 

API REST com CRUD de usuários utilizando o framework Flask com SQLAlchemy e Marshmallow com autenticação JWT e testes de rotas básico utilizando Banco de Dados MySQL.

## 📢 Como executar

Requisitos:

Python 3.8.0<br>

Clonar a pasta do projeto

Criar uma virtual env para a instalação das dependências do projeto. No console, dentro da pasta do projeto, executar:

```bash 
pip install -m venv ./venv  # Cria a pasta da virtual env dentro da pasta do projeto
 ```  

Ativar a venv com o comando:

```bash 
. venv/Scripts/activate  # Windows
. venv/bin/activate  # Linux
 ```  

Instalar todas as dependências do python usando o arquivo requirements.txt que está no projeto:  

```bash 
pip install -r requirements.txt
 ```  
Ao executar o comando acima, será feita a instalação das seguintes bibliotecas:

```
atomicwrites==1.4.0
attrs==20.3.0
click==7.1.2
colorama==0.4.4
Flask==1.1.2
flask-marshmallow==0.14.0
Flask-SQLAlchemy==2.4.4
iniconfig==1.1.1
itsdangerous==1.1.0
Jinja2==2.11.2
MarkupSafe==1.1.1
marshmallow==3.9.1
marshmallow-sqlalchemy==0.24.0
packaging==20.4
pluggy==0.13.1
py==1.9.0
PyJWT==1.7.1
PyMySQL==0.10.1
pyparsing==2.4.7
pytest==6.1.2
six==1.15.0
SQLAlchemy==1.3.20
toml==0.10.2
Werkzeug==1.0.1
```

Com o MySQL Workbench instalado em sua máquina, crie uma conexão e um schema para utilizar com este projeto, após criado o banco de dados, alterar no arquivo config.py a seguinte linha para as configurações do seu banco:

```bash 
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost:3306/apirest'
```  

Esta versão do Python não é compatível com o MySQLdb, portanto é necessário executar os comandos a seguir em sequência, para conectar com o MySQL utilizando o PyMySQL, no terminal digite:

```bash
python
>>> import pymysql
>>> pymysql.install_as_MySQLdb()
>>> import MySQLdb
>>> from app import db
>>> db.create_all()
>>> exit()
```  

Isso criará a conexão com o MySQL e a tabela users de acordo com o arquivo em "app/models/users.py"
Executar o run.py no cmd com o comando:

```bash 
python run.py
```  
Ao executar o comando, deverá aparecer a seguinte mensagem: Running on http://127.0.0.1:5000/ (Press CTRL+C to quit), conforme imagem abaixo.

<img src="https://user-images.githubusercontent.com/64918635/99022865-2f813c00-2542-11eb-85a3-4af761a95c42.png">

Acessando o link com o endpoint http://127.0.0.1:5000/, deverá aparecer a tela com a mensagem de token inválido, isso acontece pois não validamos o usuário ainda. Vamos criar um usuário administrador para realizarmos as operações de CRUD.

<img src="https://user-images.githubusercontent.com/64918635/99023324-188f1980-2543-11eb-892a-eb3c690f3c04.png">

Para isso iremos enviar um JSON ao banco de dados via POST.<br>
Importar o arquivo collection.JSON utilizando um programa de requisições REST, como o <a href="https://insomnia.rest/download/">Insomnia</a> ou o <a href="https://www.postman.com/downloads/">Postman<a> e rodar o Endpoint post_user ou criar um Endpoint do tipo POST e informar o IP: http://127.0.0.1:5000/users, preenchendo o body no formato JSON, conforme abaixo:

```
{
	"name":"admin",
	"username":"admin",
	"password":"admin",
	"email":"admin@gmail.com"
}
```
  
<img src="https://user-images.githubusercontent.com/64918635/99023250-ee3d5c00-2542-11eb-9100-8ef136e47705.png">

## Autenticação do token com servidor JWT

`POST /auth`

Com o usuário admin criado, podemos autenticar enviando uma requisição POST com autenticação do formato "BASIC" para o IP: http://127.0.0.1:5000/auth, preenchendo o "USERNAME" e "PASSWORD", conforme abaixo:

<img src="https://user-images.githubusercontent.com/64918635/99024438-5a20c400-2545-11eb-854d-cb125c9b2d5a.png">

Agora, acessando o link com http://127.0.0.1:5000/?token=<token_gerado_aqui>, informando o token gerado para o usuário, poderá verificar se o token é válido, onde aparecerá a mensagem "Hello <nome_do_usuário>"

<img src="https://user-images.githubusercontent.com/64918635/99024884-50e42700-2546-11eb-9122-7834da999320.png">

Para que todas as rotas exijam a autenticação via token, basta alterar o código em "app/routes/routes.py", inserindo abaixo de cada rota o decorator @helper.token_required, exigindo assim o uso do complemento "?token=<token_gerado_aqui>" ao final de cada rota, para fins de teste não inclui o decorator nas demais rotas:

```
@app.route('/', methods=['GET'])
@helper.token_required
def root(current_user):
    return jsonify({'message': f'Hello {current_user.name}'})
```

Segue abaixo lista dos Endpoints de usuários:

### Listar todos usuários

**Definição/Request**

`GET /users`

**Response**

- `200 OK` ao ter sucesso

```json
{
  "data": [
    {
      "created_on": "2020-11-11T14:06:40",
      "email": "antoniocarlos@gmail.com",
      "id": 8,
      "name": "Antônio Carlos Magalhães",
      "password": "pbkdf2:sha256:150000$VmcvuOZZ$a9885cee87e9a0cfa521bc51e5b79fbf0a2fb27cd006f105a45e34e7cb459456",
      "username": "userantonio"
    },
    {
      "created_on": "2020-11-11T19:35:39",
      "email": "jorge@gmail.com",
      "id": 10,
      "name": "Jorge",
      "password": "pbkdf2:sha256:150000$4kpfKkjd$28bb4fa3e78bcaf277b2fffeee0781e299ab754d3aa6f759766d1f03077c99c2",
      "username": "userjorge"
    },
    {
      "created_on": "2020-11-12T22:47:28",
      "email": "admin@gmail.com",
      "id": 30,
      "name": "admin",
      "password": "pbkdf2:sha256:150000$5pFo5YMo$800314f21d82f43e3e161206b242c83d3c6803ae73e80c41344c188f92fde8ff",
      "username": "admin"
    }
  ],
  "message": "successfully fetched"
}
```
### Listar usuários filtrando por nome

**Definição/Request**

`GET /users?name=Carlos`

**Response**

- `200 OK` ao ter sucesso

```json
{
  "data": [
    {
      "created_on": "2020-11-11T14:06:40",
      "email": "antoniocarlos@gmail.com",
      "id": 8,
      "name": "Antônio Carlos Magalhães",
      "password": "pbkdf2:sha256:150000$VmcvuOZZ$a9885cee87e9a0cfa521bc51e5b79fbf0a2fb27cd006f105a45e34e7cb459456",
      "username": "userantonio"
    }
  ],
  "message": "successfully fetched"
}
```

## Retornar um usuário especifico

`GET /users/<id>`

**Response**

- `404 Not Found` usuário não existe

```json
{
    "data": {},
    "message": "user don't exist"
}
```

- `200 OK` ao ter sucesso

```json
{
  "data": {
    "created_on": "2020-11-11T19:35:39",
    "email": "jorge@gmail.com",
    "id": 10,
    "name": "Jorge",
    "password": "pbkdf2:sha256:150000$4kpfKkjd$28bb4fa3e78bcaf277b2fffeee0781e299ab754d3aa6f759766d1f03077c99c2",
    "username": "userjorge"
  },
  "message": "successfully fetched"
}
```

### Registrando novo usuário

**Definição/Request**

`POST /users`

**Argumentos**

- `"username":string` usuário que será mostrado e feito para usar a api
- `"password":string` senha que será encriptada antes de ir para o banco
- `"name":string` nome do usuário
- `"email":string` email que será usado para comunicação

**Response**

- `201 Created` ao ter sucesso

```json
{
  "data": {
    "created_on": "2020-11-12T23:49:57",
    "email": "admin@gmail.com",
    "id": 32,
    "name": "admin",
    "password": "pbkdf2:sha256:150000$QIxCvAcu$7d23673f55fa04450f028e8decae88ca7b80ceb2857fbac2e4b68759dee47951",
    "username": "admin"
  },
  "message": "successfully registered"
}
```

- `200 Created` ao ter erro com usuário ou email existente

```json
{
    "data": {
        },
    "message": "user already exists"
}
```

- `500 Internal error` ao ter erro com o servidor ou sistema

```json
{
    "data": {},
    "message": "unable to create"
}
```

### Atualizando usuário

**Definição/Request**

`PUT /users/<id>`

**Argumentos**

- `"username":string` usuário que será mostrado e feito para usar a api(eventualmente)
- `"password":string` senha que será encriptada antes de ir para o banco(eventualmente)
- `"name":string` nome do usuário
- `"email":string` email que será usado para comunicação(caso necessário)

**Response**

- `201 Created` ao ter sucesso

```json
{
  "data": {
    "created_on": "2020-11-11T14:06:40",
    "email": "antoniocarlos@gmail.com",
    "id": 8,
    "name": "Antônio Carlos Magalhães Junior",
    "password": "pbkdf2:sha256:150000$LnL8AENV$160d396b664a4817d3757e953ea98e5de6c0ddde9aebcd96ee8a39e6d3519180",
    "username": "userantonio"
  },
  "message": "successfully updated"
}
```

- `404 Not Found` usuário não existe

```json
{
    "data": {},
    "message": "user don't exist"
}
```

- `500 Internal error` ao ter erro com servidor ou sistema

```json
{
    "data": {},
    "message": "unable to update"
}
```

## Deletar usuário

**Definição**

`DELETE /users/<id>`

**Response**

- `200 No Content` ao ter sucesso

```json
{
  "data": {
    "created_on": "2020-11-11T19:35:39",
    "email": "jorge@gmail.com",
    "id": 10,
    "name": "Jorge",
    "password": "pbkdf2:sha256:150000$4kpfKkjd$28bb4fa3e78bcaf277b2fffeee0781e299ab754d3aa6f759766d1f03077c99c2",
    "username": "userjorge"
  },
  "message": "successfully deleted"
}
```

- `404 Not Found` usuário não existente

```json
{
    "data": {},
    "message": "user don't exist"
}
```

- `500 Internal error` erro com servidor ou sistema

```json
{
    "data": {},
    "message": "unable to delete"
}
```

## Dados armazenados no banco de dados

As senhas são gravadas criptografadas no banco de dados MySQL:

<img src="https://user-images.githubusercontent.com/64918635/99026710-5e031500-254a-11eb-87fe-0a85d5d4a95c.png">

## Testes unitários

Os testes unitários de rotas foram criados utilizando o pytest, basta rodar o comando:

```
python -m pytest -v
```

<img src="https://user-images.githubusercontent.com/64918635/99028089-af60d380-254d-11eb-87dd-d93e5b358b9a.png">

## 🚀 Tecnologias Usadas 

<img src="https://user-images.githubusercontent.com/18649504/66262823-725cd600-e7be-11e9-9cea-ea14305079db.png" width = "100">

<img src="https://user-images.githubusercontent.com/64918635/93954857-ddcbea80-fd24-11ea-89a8-213950b038ca.png" width = "150">

<img src="https://user-images.githubusercontent.com/64918635/97925563-62585280-1d40-11eb-82e6-7178c59fc19d.png" width = "150">

Desenvolvido em Python 3.8.0 <br>
SO utilizado: Windows 10 <br>
IDE utilizada: VSCode <br>

## 📌 Estrutura do Projeto 
    |-- app
       |-- models
          |-- users.py
       |-- routes
          |-- routes.py
       |-- views
          |-- helper.py
          |-- users.py
       |-- __init__.py
    |-- tests
       |-- conftest.py
       |-- test_routes.py
    |-- collection.json
    |-- README.md
    |-- config.py    
    |-- instructionsdb.txt    
    |-- requirements.txt    
    |-- run.py

pasta app -> pasta contendo os arquivos da aplicação Flask, separados por models, routes e views, no modelo de oganização do Django, visto que o Flask não possui um padrão de organização de arquivos.

pasta test -> contém os arquivos necessários para configuração e execução dos testes.

collection.json -> Arquivo contendo o exemplo da requisição à ser importado em um programa de requisições como o POSTMAN ou INSOMNIA.

README.md -> Descrição e instruções de utilização do projeto. 

config.py -> Configurações de geração de chave aleatória e configurações de banco de dados. 

instructionsdb.txt -> Instruções a serem executadas para conexão e criação de tabela no banco de dados.

requirements.txt -> Bibliotecas utilizadas no python.

run.py -> Arquivo principal que contém a execução do projeto.

## 🔓 Licença 
MIT © [Matheus Muller](https://www.linkedin.com/in/matheus-herrera-bezerra-muller/)
