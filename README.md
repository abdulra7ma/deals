# deals

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

### Project ###
Целью этого проекта является создание веб-службы, предоставляющей RESTful API для управления клиентскими транзакциями и обработки данных из файлов Deals.csv. Сервис реализован с использованием Django — популярного веб-фреймворка для создания веб-приложений с использованием языка программирования Python. Служба хранит данные в реляционной базе данных и использует Django ORM для взаимодействия с данными. Сервис способен обрабатывать типичные файлы Deals.csv и сохранять извлеченные данные в базе данных проекта. У службы есть конечные точки, которые соответствуют заданным требованиям и возвращают обработанные данные в ответ на запрос GET. Сервис также включает в себя функцию, которая позволяет пользователям загружать файлы Deals.csv для обработки с помощью POST-запроса. Служба контейнеризирована с помощью Docker, и проект не использует глобальные зависимости, кроме Python, Docker и Docker Compose. В проект также включен подробный файл README, в котором описан весь процесс установки, запуска и работы с сервисом. К внешнему интерфейсу требований нет, а взаимодействие с интерфейсом осуществляется через RESTful API. Проект можно запустить одной командой и он готов к использованию.

### List of services: ###

* Dev server: [http://127.0.0.1:8000/](http://127.0.0.1:8000//)
* Nginx server: [http://127.0.0.1/](http://127.0.0.1/)

### API documentation (DEV): ###

* ReDoc web UI: [http://127.0.0.1:8000/_platform/docs/v1/redoc/](http://127.0.0.1:8000/_platform/docs/v1/redoc/)
* Swagger web UI: [http://127.0.0.1:8000/_platform/docs/v1/swagger/](http://127.0.0.1:8000/_platform/docs/v1/swagger/)
* Swagger JSON: [http://127.0.0.1:8000/_platform/docs/v1/swagger.json](http://127.0.0.1:8000/_platform/docs/v1/swagger.json)
* Swagger YAML: [http://127.0.0.1:8000/_platform/docs/v1/swagger.yaml](http://127.0.0.1:8000/_platform/docs/v1/swagger.yaml)

### API documentation (Nginx): ###

* ReDoc web UI: [http://127.0.0.1/_platform/docs/v1/redoc/](http://127.0.0.1/_platform/docs/v1/redoc/)
* Swagger web UI: [http://127.0.0.1/_platform/docs/v1/swagger/](http://127.0.0.1/_platform/docs/v1/swagger/)
* Swagger JSON: [http://127.0.0.1/_platform/docs/v1/swagger.json](http://127.0.0.1/_platform/docs/v1/swagger.json)
* Swagger YAML: [http://127.0.0.1/_platform/docs/v1/swagger.yaml](http://127.0.0.1/_platform/docs/v1/swagger.yaml)

### First run: (Local) ###

Install Python 3.10 & setup virtual environment. We recommend to use [pyenv](https://github.com/pyenv/pyenv) & [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv):

```bash
pyenv install 3.10
pyenv virtualenv 3.10 deals
pyenv activate deals
```

Update `pip` & `setuptools`, install `fabric`, `invoke` & `pip-tools`:

```bash
pip install -U fabric invoke pip pip-tools setuptools
```

Install Python requirements:

```bash
fab pip.sync
```

Copy initial settings for Django project:

```bash
cp ./api/.env.example ./api/.env
```

Generate `SECRET_KEY`:

```bash
./api/manage.py generate_secret_key
```

and write it to `./api/.env`:

```
CORE_SECRET_KEY=<your-generated-key>
```

Run backing services (require Docker):

```bash
fab compose.up -d
```

Run migrations:

```bash
./api/manage.py migrate
```

Run Django server:

```bash
fab run
```

Run project' tests
```bash
fab test
```

### Docker in development: (Local) ###

#### 1. copy .env files ####
```shell
cat compose/development/django/.env.example > compose/development/django/.env
cat compose/development/postgres/.env.example > compose/development/postgres/.env
cat compose/development/redis/.env.example > compose/development/redis/.env
```

#### 2. build image ####
```shell
 docker-compose -f docker-compose-local.yml build
```

#### 3. run project ####
```shell
 docker-compose -f docker-compose-local.yml up
```


### Docker in production: (Nginx) ###

#### 1. copy .env files ####
```shell
cat compose/production/django/.env.example > compose/production/django/.env
cat compose/production/postgres/.env.example > compose/production/postgres/.env
cat compose/production/redis/.env.example > compose/production/redis/.env
```

#### 2. build image ####
```shell
 docker-compose -f docker-compose-prod.yml build
```

#### 3. run project ####
```shell
 docker-compose -f docker-compose-prod.yml up
```

#### 4. access API (swagger) ####
- [http://127.0.0.1/_platform/docs/v1/swagger/](http://127.0.0.1/_platform/docs/v1/swagger/)
