# Wallet
## Описание:
Приложение, которое по REST принимает запросы на получение информации о кошельке,
пополении или снятии денег со счета.
Через миграцию добавлены несколько кошельков для наглядности.

## Примеры запросов  

**Получение информации о кошельке по uuid**
``` 
GET /api/v1/wallets/{uuid}/
Права доступа: Доступно без токена.
Response:
{
    "uuid": "7dafb1b0-94eb-432e-8653-dc9defec0108",
    "balance": 5700.0
}
``` 

**Получение информации о кошельках**
``` 
GET /api/v1/wallets/
Права доступа: Доступно без токена.
Response:
[
    {
        "uuid": "7dafb1b0-94eb-432e-8653-dc9defec0108",
        "balance": 5700.0
    },
    {
        "uuid": "dce7ec93-dea0-403b-9076-daeb9d64f366",
        "balance": 233.345
    }
]

``` 


**Снятие денег**
``` 
POST /api/v1/wallets/{uuid}/operation/
Права доступа: Доступно без токена.

Request:

{
"operation_type": "WITHDRAW",
"amount": 100
}

Response:
"Баланс обновлен, текущий баланс на кошельке 7dafb1b0-94eb-432e-8653-dc9defec0108               составляет 5600.0"

``` 


**Пополнение счета**

``` 
POST /api/v1/wallets/{uuid}/operation/
Права доступа: Доступно без токена.

Request:

{
"operation_type": "DEPOSIT",
"amount": 100
}

Response:
"Баланс обновлен, текущий баланс на кошельке 7dafb1b0-94eb-432e-8653-dc9defec0108               составляет 5800.0"

``` 


##  Запуск проекта

### Запуск в контейнерах

1. Убедиться, что установлен Docker
2. Клонировать репозиторий
3. Перейти в него в командной строке:  
4. Создать .env и заполнить по образцу .env.example
5. Запустить docker-compose.yml, выполнить миграции и собрать статику
```
git clone https://github.com/Anastasia289/wallet_test.git
cd wallet_test
docker compose up
docker compose exec backend python manage.py migrate
docker compose exec backend python manage.py collectstatic
docker compose exec backend cp -r /app/collected_static/. /static/

``` 

## Технологии: 
- Backend: Django, Django Rest Framework
- База данных: PostgreSQL
- Контейнеризация: Docker

[![My Skills](https://skillicons.dev/icons?i=py,docker,postgres,django,)](https://skillicons.dev)

## Автор:  

[Анастасия Богданова](https://github.com/Anastasia289/)  