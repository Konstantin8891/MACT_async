# MACT_async

## Парсинг музейных сайтов

### Стек

FastAPI

PostgreSQL

SQLAlchemy

Alembic

Aiohttp

Docker

### Инструкции по запуску проекта

git clone git@github.com:Konstantin8891/MACT_async.git

cd infra

docker-compose up --build

docker-compose exec web python fullfill_db_correct.py

Время выполнения около 5 минут

Лог ошибок находится в code/errors.txt

Лог обработанные проектов находится в code/nec-urls.txt

localhost:8000/docs

### Содержимое файла с переменными окружения

SQLALCHEMY_DATABASE_URL - например, postgresql://postgres:postgres@db/postgres
