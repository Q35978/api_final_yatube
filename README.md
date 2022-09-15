# Пример реализации API на базе Django REST Framework

Позволяет работать с моделями базы:
- Post (публикации);
- Group (группы);
- Comment (комментарии);
- Follow (подписки).  

# Установка:
### -настройте виртуальное окружение

    source venv/bin/activate

### -установите необходимые зависимости

    python3 -m pip install --upgrade pip
    pip install -r requirements.txt

### -разверните базу данных

    python3 manage.py makemigrations
    python3 manage.py migrate

### - запустите проект

    python manage.py runserver



# Пример запроса к API:

### Список групп
  **Запрос**
  ```
  GET /api/v1/groups/
  ```
  **Ответ**
  ```
  body: {
    [
      {
        "id": integer
        "title": string  
        "slug": string
        "description": string     
      }
    ]
  }  
  ```

### Информация о группе
  **Запрос**
  ```
  GET /api/v1/groups/{id}
  ```
  **Ответ**
  ```
  body: {
    "id": integer
    "title": string  
    "slug": string
    "description": string    
  }
  ```

### Получение публикаций
  **Запрос**
  ```
  GET /api/v1/posts/
  ```
  **Ответ**
  ```
  body: {
  "count": integer,
  "next": string with http address,
  "previous": string with http address,
  "results": [
    {
      "id": integer,
      "text": string,
      "pub_date": date-time,
      "author": string,
      "group": integer or null,
      "image": string <binary> or null
    }
  ]
  }
  ```

### Создание публикации
  **Запрос**
  ```
  POST /api/v1/posts/
  body: {
    "text": string,
    "group": integer or null
    "image": string <binary> or null,
  }
  ```
  **Ответ**
  ```
  body: {
    "id": integer,
    "text": string,
    "pub_date": date-time,
    "author": string,
    "group": integer or null,
    "image": string <binary> or null
  }
  ```

### Получение публикации по идентификатору
  **Запрос**
  ```
  GET /api/v1/posts/{id}/
  ```
  **Ответ**
  ```
  body: {
    "id": integer,
    "text": string,
    "pub_date": date-time,
    "author": string,
    "group": integer or null,
    "image": string <binary> or null
  }
  ```

### Обновление публикации по идентификатору
  **Запрос**
  ```
  PUT /api/v1/posts/{id}/
  body: {
    "text": string,
    "group": integer or null
    "image": string <binary> or null,
  }
  ```
  **Ответ**
  ```
  body: {
    "id": integer,
    "text": string,
    "pub_date": date-time,
    "author": string,
    "group": integer or null,
    "image": string <binary> or null
  }
  ```
### Создание подписки
  **Запрос**
  ```
  POST /api/v1/follow/
  body: {
    "following": string
  }
  ```
  **Ответ**
  ```
  body: {
    "user": string,
    "following": string
  }
  ```
### Получение всех комментариев к публикации.
  **Запрос**
  ```
  GET /api/v1/posts/{post_id}/comments/
  ```
  **Ответ**
  ```
  {
    [
        {
            "id": integer,
            "author": string,
            "post": integer,
            "text": string,
            "created": date-time
        }
    ]
  }
  ```
### Добавление нового комментария к публикации. 
**Запрос**
  ```
  POST /api/v1/posts/{post_id}/comments/
  body: {
    "text": string
  }
  ```
  **Ответ**
  ```
  body: {
    "id": integer,
    "author": string,
    "post": integer,
    "text": string,
    "created": date-time
  }
  ```