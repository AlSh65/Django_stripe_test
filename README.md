# Django_stripe_test
## Задача
- Реализовать Django + Stripe API бэкенд со следующим функционалом и условиями:
    
- Django Модель Item с полями (name, description, price) 

- API с двумя методами:

- GET /buy/{id}, c помощью которого можно получить Stripe Session Id для оплаты выбранного Item. При выполнении этого метода c бэкенда с помощью python библиотеки stripe должен выполняться запрос stripe.checkout.Session.create(...) и полученный session.id выдаваться в результате запроса

- GET /item/{id}, c помощью которого можно получить простейшую HTML страницу, на которой будет информация о выбранном Item и кнопка Buy. По нажатию на кнопку Buy должен происходить запрос на /buy/{id}, получение session_id и далее  с помощью JS библиотеки Stripe происходить редирект на Checkout форму stripe.redirectToCheckout(sessionId=session_id)

# Бонусные задачи
- Запуск используя Docker

- Использование environment variables

- Просмотр Django Моделей в Django Admin панели

- Запуск приложения на удаленном сервере, доступном для тестирования

- Модель Order, в которой можно объединить несколько Item и сделать платёж в Stripe на содержимое Order c общей стоимостью всех Items

- Модели Discount, Tax, которые можно прикрепить к модели Order и связать с соответствующими атрибутами при создании платежа в Stripe - в таком случае они корректно отображаются в Stripe Checkout форме. 

- Добавить поле Item.currency, создать 2 Stripe Keypair на две разные валюты и в зависимости от валюты выбранного товара предлагать оплату в соответствующей валюте

- Реализовать не Stripe Session, а Stripe Payment Intent.


# Запуск в Python

##### 1) Клонировать репозиторий

    https://github.com/AlSh65/Django_stripe_test.git

##### 2) Указать в .env параметры STRIPE_SECRET_KEY и STRIPE_PUBLIC_KEY

##### 3) Создать виртуальное окружение и активировать виртульное окружение

    source venv/bin/activate
    
##### 4) Устанавливить зависимости:
    pip install -r requirements.txt
##### 5) Выполнить команду для выполнения миграций:
    python manage.py makemigrations

    python manage.py migrate

##### 6) Создать суперпользователя

    python manage.py createsuperuser
    
##### 7) Запустить проект
    python3 manage.py runserver

# Запуск с помощью Docker

##### 1) Клонировать репозиторий

    https://github.com/AlSh65/Django_stripe_test.git


##### 2) Указать в .env параметры STRIPE_SECRET_KEY и STRIPE_PUBLIC_KEY


##### 3) Build docker
    docker-compose build 
##### 4) Сделать миграции 
    docker-compose run web sh -c "python ./stripe_ecommerce/manage.py makemigrations"
    docker-compose run web sh -c "python ./stripe_ecommerce/manage.py migrate"

##### 4)Создать суперпользователя(опционально):

    docker-compose run web sh -c "python ./stripe_ecommerce/manage.py createsuperuser"
##### 5)  Запустить 
    docker-compoes up


