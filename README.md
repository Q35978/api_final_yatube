# Пример реализации API на базе Django REST Framework

Позволяет работать с моделями базы:
- Post (публикации);
- Group (группы);
- Comment (комментарии);
- Follow (подписки).  

### Установка:
-настройте виртуальное окружение
    ```
    source venv/bin/activate
    ```
-установите необходимые зависимости
    ```
    python3 -m pip install --upgrade pip
    pip install -r requirements.txt
    ```
-разверните базу данных
    ```
    python3 manage.py makemigrations
    python3 manage.py migrate
    ```
- запустите проект
    ```
    python manage.py runserver
    ```


### Пример запроса к API:
```
/api/v1/posts/   
/api/v1/posts/<id>   
/api/v1/posts/<id>/comments 
/api/v1/posts/<id>/comments/<id>  
/api/v1/group/ 
/api/v1/follow/  