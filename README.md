# Example of API implementation based on the Django REST Framework Framework

Allows you to work with database models:
- Message (publications);
- Group(s);
- Comment (comments);
- Follow (subscriptions).

# Installation:
### -configure the virtual environment

venv/bin/activate source file

### -install the necessary dependencies

python3 -m pip install --update pip
installing pip -r requirements.txt

### -expand the database

python3 manage.py perform python3 migrations
manage.py migrate

### - launch the project

python manage.py startup server



# API request example:

### List of groups
**Request**
```
GET /api/v1/groups/
```
**Response**
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

### Information about the group
**Request**
```
GET /api/v1/groups/{id}
```
**Response**
```
case: {
"id": 1
"title": "string"
"slug": "string"
"description": "string"
}
```

### Receiving publications
**Request**
```
GET /api/v1/posts/
```
**Response**
```
housing: {
"quantity": 1234,
"next": "http://www.example.org/acc/?offset=300&limit=100 ",
"previous": "http://www.example.org/acc/?offset=300&limit=100 ",
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

### Creating a publication
**Request**
```
POST /api/v1/messages/
corpus: {
"text": "string",
"group": 1 or null
"image": "string <binary file> or null",
}
```
**Response**
```
body: {
"id": 1,
"text": "string",
"pub_date": "2022-09-16T20:01:29.648Z",
"author": "string",
"group": 1 or null,
"image": "string <binary> or null"
}
` `

### Getting a publication by ID
**Request**
```
GET /api/v1/posts/{id}/
```
**Response**
```
corpus: {
"id": 1,
"text": "string",
"pub_date": "2022-09-16T20:01:29.648Z",
"author": "string",
"group": 1 or null,
"image": "string <binary file> or null"
}
``

### Updating a publication by ID
**Request**
```
PUT /api/v1/posts/{id}/
body: {
"text": "string",
"group": 1 or null
"image": "string <binary> or null",
}
```
**Response**
```
corpus: {
"id": 1,
"text": "string",
"pub_date": "2022-09-16T20:01:29.648Z",
"author": "string",
"group": 1 or null,
"image": "string <binary file> or null"
}
``
### Creating a subscription
**Request**
```
POST /api/v1/follow/
body: {
"next": "string"
}
``
**Response**
```
corpus: {
"user": "string",
"next": "string"
}
``
### Getting all the comments for the publication.
**Request**
```
GET /api/v1/messages/{post_id}/comments/
``
**Response**
```
corpus: {
[
{
"id": 1,
"author": "string",
"message": 1,
"text": "string",
"created": "2022-09-16T20:01:29.648 z"
}
]
}
```
### Adding a new comment to the post.
**Request**
```
POST /api/v1/messages/{post_id}/comments/
body: {
"text": "string"
}
``
**Response**
```
body: {
"id": 1,
"author": "string",
"post": 1,
"text": "string",
"created": "2022-09-16T20:01:29.648Z"
}
``
