**Структура проекта:**

core - хранится конфигурация бд

core.models - таблицы проекта

core.shema - схемы для моделей

core.database - настройки для подключения к БД

routers - хранятся все url

services - все сервисы, необходимые для функционирования проекта

tests - тесты проекта

---

**Команды для запуска проекта**

1. Создание образов через Dockerfile
```
docker build --pull --rm -f "Dockerfile" -t libraryfastapi:latest "." 
```
2. Создание контейнеров проекта
```
docker compose -f "docker-compose.yaml" up -d --build
```

**Запуск тестов проекта**
1. Зайти в контейнер проекта
```
docker exec -it library_fast_api-app-1 sh
```
2. Запуск тестов
```
pytest
```

