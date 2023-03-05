# api_final
### О проекте:
Бэкенд социальной сети для публикации блогов.  
Предоставляет API для создания, чтения и редактирования публикаций и комментариев к ним. Поддерживается  оформление подписок на авторов.
### Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/avpech/api_final_yatube.git
```
```
cd yatube_api
```
Cоздать и активировать виртуальное окружение:
```
python3 -m venv env
```
```
source env/bin/activate
```
Установить зависимости из файла requirements.txt:
```
python3 -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
Выполнить миграции:
```
python3 manage.py migrate
```
Запустить проект:
```
python3 manage.py runserver
```
Подробную документацию API можно получить по адресу ```http://127.0.0.1:8000/redoc/``` после запуска проекта.
### API
##### Список эндпоинтов:  
- **/api/v1/posts/**  
*Создание и получение публикций. При GET-запросе возможно указание параметров limit и offset для пагинации ответа.*
- **/api/v1/posts/{id}/**  
  *Получение, редактирование, удаление отдельной публикации.*
- **/api/v1/posts/{post_id}/comments/**  
  *Создание и получение комментариев.*
-  **/api/v1/posts/{post_id}/comments/{id}/**  
  *Получение, редактирование, удаление отдельного комментария.*
-  **/api/v1/groups/**  
  *Получение списка сообществ.*
-  **/api/v1/groups/{id}/**  
  *Получение информации о сообществе по id.*
-  **/api/v1/follow/**  
  *Оформление и получение подписок пользователя. При GET-запросе возможно указание параметра search для поиска.*
-  **/api/v1/jwt/create/**  
  *Получение JWT-токена.*
-  **/api/v1/jwt/refresh/**  
  *Обновление JWT-токена.*
-  **/api/v1/jwt/verify/**  
  *Проверка JWT-токена.*
##### Примеры запросов:  
GET-запрос к эндпоинту ```http://127.0.0.1:8000/api/v1/posts/```  
Ответ  
```
[
    {
        "id": 1,
        "author": "user",
        "image": null,
        "text": "publiacation text",
        "pub_date": "2023-03-04T11:38:52.240260Z",
        "group": null
    },
    {
        "id": 2,
        "author": "user",
        "image": null,
        "text": "publiacation text",
        "pub_date": "2023-03-04T11:39:10.801964Z",
        "group": 1
    },
]
```
GET-запрос к эндпоинту ```http://127.0.0.1:8000/api/v1/posts/?limit=2&offset=4```　с пагинацией  
Ответ  
```
{
    "count": 6,
    "next": null,
    "previous": "http://127.0.0.1:8000/api/v1/posts/?limit=2&offset=2",
    "results": [
        {
            "id": 5,
            "author": "user",
            "image": null,
            "text": "publication text",
            "pub_date": "2023-03-04T12:07:26.966271Z",
            "group": 1
        },
        {
            "id": 6,
            "author": "user",
            "image": "http://127.0.0.1:8000/media/posts/temp.png",
            "text": "publication text",
            "pub_date": "2023-03-04T12:32:34.488770Z",
            "group": 1
        }
    ]
}
```