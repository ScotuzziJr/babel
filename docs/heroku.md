# Deploy Heroku Config

*Passo a passo de como realizar o deploy do projeto Django no Heroku*

**Pré requisitos**
- Possuir uma conta no Heroku
- Ter o Heroku CLI instalado na máquina

### Configurações dentro do projeto
Dentro do projeto Django, as configurações necessárias são:
- O arquivo *Procfile*, que configura o gunicorn e serve de "ponto de partida" para o Heroku na hora do deploy, com a seguinte linha:
 > web: gunicorn {nome-do-projeto}.wsgi

*Obs: Para saber o nome correto que está configurado no projeto, basta acessar o arquivo settings.py e procurar pela variável ROOT_URLCONF. O que deverá ser usado é o que vem antes do .extensao*

- Instalar o *gunicorn* usando o *pip install gunicorn*

- Instalar o *django_on_heroku* com *pip install django-on-heroku*

- Importar o módulo *django_on_heroku* no arquivo settings.py com *import django_on_heroku*

- Adicionar a linha *django_on_heroku.settings(locals())* no final do arquivo settings.py

- Gerar um arquivo de *requirements.txt* usando *pip freeze > requirements.txt*

*Obs: é importante que o projeto tenha sido desenvolvido dentro de um ambiente virtual para conter apenas as dependências que realmente foram usadas no projeto, porque o Heroku vai usar o arquivo requirements para instalar as dependências no servidor.*

- Gerar um arquivo *runtime.txt* contendo a versão do Python utilizada no ambiente virtual da aplicação, caso contrário o Heroku vai pegar a versão 3.10 do Python e o deploy pode falhar. Exemplo: *python-3.8.10*

- Commite as mudanças antes de continuar

## Step by step usando Heroku CLI
- Depois de configurado o projeto, é só iniciar o Heroku CLI (dentro da venv do projeto) com o comando:
> heroku login

Se for a primeira vez usando o Heroku CLI, uma aba do navegador irá abrir pedindo para você logar com email e senha do Heroku (por isso é importante criar a conta antes)

- Depois de logado, é preciso criar o projeto:
> heroku create {nome-do-projeto}

- Para fazer o deploy, basta dar um push no servidor do Heroku:
> git push heroku master

- Se o deploy der certo, você vai ver uma mensagem de sucesso e o link para acessar a aplicação

## Migration do banco
Da mesma forma que é preciso dar o *migrate* para commitar as mudanças do banco de dados localmente no projeto Django, quando o projeto estiver no servidor do Heroku o *migrate* também precisa ser feito. A primeira etapa para isso é criar um banco de dados no Heroku:
> heroku addons:create heroku-{nome-do-SGBD}:hobby-dev

O *addons* é um conjunto de ferramentas e serviços para desenvolver, estender e gerenciar o projeto no Heroku e nesse caso estamos usando ele para criarmos um banco de dados no servidor. O SGBD usado no Heroku não precisa ser o mesmo usado localmente. Por exemplo, foi usado *sqlite3* no Babel, mas no heroku o SGBD escolhido foi o *postgresql* (*heroku addons:create heroku-postgresql:hobby-dev*). O *hobby-dev* é o plano de assinatura gratuito do Heroku (caso sua conta usa outro, é só substituir)

*Obs: essa etapa seria o equivalente ao makemigration do Django*

- Agora é só rodar o *migrate*:
> heroku run python manage.py migrate

- Para acessar o banco de dados, basta rodar:
> heroku config --app {nome-do-projeto}

Esse comando vai retornar a url do banco e nela estão contidos o host, usuario, senha e nome do banco de dados (o que permite usar algum programa para acessar o banco)
