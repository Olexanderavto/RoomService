# Room Booking Service

Сервис для бронирования комнат с API на **Django REST Framework**.  
Проект использует **Docker + PostgreSQL** и поддерживает аутентификацию через **JWT**.

---

## 🚀 Архитектура проекта

room-service/
│── booking/               # Основное приложение
│ ├── api/                 # API слой
│ │ ├── views.py           # ViewSet-ы для моделей
│ │ ├── serializers.py     # Сериализаторы
│ │ ├── routers.py         # DRF Router
│ │ └── permissions.py     # (кастомные права, если появятся)
│ │
│ ├── models.py            # Модели: Room, Booking, Category, Equipment и др.
│ ├── urls.py              # Роутинг API
│ ├── admin.py             # Админка Django
│ └── ...
│
│── room_booking/          # Конфигурация Django-проекта
│ ├── settings/            # Настройки
│ │ ├── base.py            # Общие настройки
│ │ ├── dev.py             # Для разработки
│ │ └── prod.py            # Для продакшена
│ ├── urls.py              # Основной роутинг
│ ├── wsgi.py              # WSGI
│ └── asgi.py              # ASGI
│
│── media/                 # Загруженные изображения (например, фото комнат)
│── static/                # (если будут шаблоны)
│
│── docker-compose.yml     # Docker-сервисы (Django + PostgreSQL)
│── Dockerfile             # Образ Django-приложения
│── requirements.txt       # Python-зависимости
│── manage.py              # Django CLI
│── README.md              # Документаци



---

## 🔑 Аутентификация

Проект поддерживает **JWT-аутентификацию** через `djangorestframework-simplejwt`.  

### Доступные эндпоинты:
- `POST /api/auth/login/` → вход (access + refresh токены)  
- `POST /api/auth/token/refresh/` → обновить `access`  
- `POST /api/auth/token/verify/` → проверить токен  
- `POST /api/auth/check-login/` → проверить логин/пароль (без выдачи токена)  

Также доступна аутентификация через `TokenAuthentication` (`rest_framework.authtoken`).  

---

## 📡 API

Все основные эндпоинты доступны по `/api/`:

- `rooms/` – список комнат  
- `bookings/` – бронирования  
- `categories/` – категории  
- `equipment/` – оборудование  
- `images/` – изображения  
- `ratings/` – рейтинги  

Примеры запросов:
```http
GET /api/rooms/
POST /api/bookings/

____________________________________________________________________________
Запуск через Docker

Собрать и запустить контейнеры:
docker-compose up --build

Push на GitHub:
git add .
git commit -m "комент"
git push origin main
_______________________________________________________________________________

Регистрация пользователя:
В проекте используется JWT-аутентификация через djangorestframework-simplejwt.

             Эндпоинты авторизации
Метод	URL	                         Описание
POST	/auth/register/	        Регистрация нового пользователя
POST	/auth/login/	        Авторизация по username и password. Возвращает access и refresh токены
POST	/auth/token/refresh/	Обновление access токена по refresh
POST	/auth/token/verify/	    Проверка валидности токена
GET	    /auth/profile/	        Данные текущего авторизованного пользователя
POST	/auth/logout/	        Разлогин (инвалидирует refresh токен)
_______________________________
       Регистрация:

POST /auth/register/
Content-Type: application/json

{
  "username": "john",
  "email": "john@example.com",
  "password": "strong_password"
}

       Ответ:
{
  "id": 1,
  "username": "john",
  "email": "john@example.com"
}
________________________________

       Логин:
POST /auth/login/
Content-Type: application/json

{
  "username": "john",
  "password": "strong_password"
}

      Ответ:

{
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGci...",
  "access": "eyJ0eXAiOiJKV1QiLCJhbGci..."
}
___________________________________________

          Профиль:
          
GET /auth/profile/
Authorization: Bearer <access_token>


         Ответ:

{
  "id": 1,
  "username": "john",
  "email": "john@example.com"
}

__________________________________________

           Логаут:
           
POST /auth/logout/
Authorization: Bearer <access_token>
Content-Type: application/json

{
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGci..."
}


          Ответ:

{
  "detail": "Вы вышли из системы"
}

_________________________________________