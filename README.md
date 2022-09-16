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
        "id": 1
        "title": "string"  
        "slug": "string"
        "description": "string"     
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
    "id": 1
    "title": "string"  
    "slug": "string"
    "description": "string"    
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
  "count": 1234,
  "next": "http://www.example.org/acc/?offset=300&limit=100",
  "previous": "http://www.example.org/acc/?offset=300&limit=100",
  "results": [
    {
      "id": 1,
      "text": "string",
      "pub_date": "2022-09-16T20:01:29.648Z",
      "author": "string",
      "group": 1 or null,
      "image": "string <binary> or null"
    }
  ]
  }
  ```

### Создание публикации
  **Запрос**
  ```
  POST /api/v1/posts/
  body: {
    "text": "string",
    "group": 1 or null
    "image": "string <binary> or null",
  }
  ```
  **Ответ**
  ```
  body: {
    "id": 1,
    "text": "string",
    "pub_date": "2022-09-16T20:01:29.648Z",
    "author": "string",
    "group": 1 or null,
    "image": "string <binary> or null"
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
    "id": 1,
    "text": "string",
    "pub_date": "2022-09-16T20:01:29.648Z",
    "author": "string",
    "group": 1 or null,
    "image": "string <binary> or null"
  }
  ```

### Обновление публикации по идентификатору
  **Запрос**
  ```
  PUT /api/v1/posts/{id}/
  body: {
    "text": "string",
    "group": 1 or null
    "image": "string <binary> or null",
  }
  ```
  **Ответ**
  ```
  body: {
    "id": 1,
    "text": "string",
    "pub_date": "2022-09-16T20:01:29.648Z",
    "author": "string",
    "group": 1 or null,
    "image": "string <binary> or null"
  }
  ```
### Создание подписки
  **Запрос**
  ```
  POST /api/v1/follow/
  body: {
    "following": "string"
  }
  ```
  **Ответ**
  ```
  body: {
    "user": "string",
    "following": "string"
  }
  ```
### Получение всех комментариев к публикации.
  **Запрос**
  ```
  GET /api/v1/posts/{post_id}/comments/
  ```
  **Ответ**
  ```
  body: {
    [
        {
            "id": 1,
            "author": "string",
            "post": 1,
            "text": "string",
            "created": "2022-09-16T20:01:29.648Z"
        }
    ]
  }
  ```
### Добавление нового комментария к публикации. 
**Запрос**
  ```
  POST /api/v1/posts/{post_id}/comments/
  body: {
    "text": "string"
  }
  ```
  **Ответ**
  ```
  body: {
    "id": 1,
    "author": "string",
    "post": 1,
    "text": "string",
    "created": "2022-09-16T20:01:29.648Z"
  }
  ```