Данная работа представляет собой Backend-часть для сайта объявлений, реализована на основе Django REST framework. </p> 

Frontend-часть уже готова и будет предоставлена командой SkyPro.
Описание задач
Бэкенд-часть проекта предполагает реализацию следующего функционала:


ТЗ:
Авторизация и аутентификация пользователей.
Распределение ролей между пользователями (пользователь и админ).
Восстановление пароля через электронную почту (не обязательно).
CRUD для объявлений на сайте (админ может удалять или редактировать все объявления, а пользователи только свои).
Под каждым объявлением пользователи могут оставлять отзывы.
В заголовке сайта можно осуществлять поиск объявлений по названию.


Для запуска проекта следуйте инструкциям:
### **Установка**
Для установки проекта SkyMarket, следуйте инструкциям ниже:

**<p>1. Сделайте Fork этого репозитория. Репозиторий появится в ваших личных репозиториях на GitHub.</p>**

**1.1 Сделайте `git clone` форкнутого репозитория, чтобы получить репозиторий локально:**

**<p>2. Перейдите в папку с проектом.</p>**

**<p>3. Создайте и активируйте виртуальное окружение:</p>**

**<p>4.Установите зависимости;**

**<p>5. Создайте файл .env  и заполните данные для настройки проекта из файла .env.example:</p>**

**<p>6. Перейдите в папку /skymarket/ и примените миграции:</p>**

`python manage.py migrate`


**<p>Для запуска на локальном компьютере:</p>**

Для Win -> python manage.py runserver

Для Linux -> python3 manage.py runserver



Необходимо прописать переменные окружения для подключения к базе данных Postgres:

POSTGRES_DB POSTGRES_USER POSTGRES_PASSWORD POSTGRES_HOST POSTGRES_PORT

SECRET_KEY

EMAIL_HOST EMAIL_HOST_USER EMAIL_HOST_PASSWORD EMAIL_PORT 

Файл .env должен находиться в корне проекта.


**<p>Для запуска в докере:</p>**

В проекте используется Docker Compose

Установите Docker, следуя инструкциям для вашей операционной системы: Docker Install.
Установите Docker Compose: Docker Compose Install.
Для запуска приложения необходимо выполнить следующие команды:

**<p>docker-compose build - сборка образа</p>**
**<p>docker-compose up - запуск контейнера</p>**
Вот пошаговая инструкция:

**<p>Откройте командную строку или терминал и перейдите в директорию, где находится файл docker-compose.yml.</p>**

**<p>Запустите команду docker-compose up.</p>** 
Docker Compose будет читать файл docker-compose.yml и создавать и запускать контейнеры, описанные в этом файле.

По умолчанию, команда docker-compose up будет выводить логи контейнеров в текущем терминале. 
Чтобы запустить контейнеры в фоновом режиме, используйте флаг -d (пример: docker-compose up -d.)

Docker Compose создаст и запустит все контейнеры, описанные в файле docker-compose.yaml. 
Вы сможете видеть логи работы контейнеров и контролировать их состояние.

Для остановки контейнера, используйте команду docker-compose down. 
Эта команда остановит и удалит все контейнеры, созданные с помощью docker-compose.yaml.

Автор проекта: Евгения Осокина