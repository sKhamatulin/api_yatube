## API для приложение YaTube.
С Помощью API можно создавать, удалять, редактировать посты. (JSON)

## Установка на локальной машине.

### Cистемные требования:
```
    python==3
    Django==2.2
    DjangoRestFramework==3.12
```

### Порядок установки.
1) Клонировать
2) Установить зависимости
3) Запустить

```
git clone github.com/sKhamatulin/api_yatube
pip install -r requirements.txt
python manage.py runserver
```

## Примеры json
<sub>*Postman</sub>

POST запрос к ```http://127.0.0.1:8000/api/v1/posts/```
```
{
"text": "test post",
}
```
GET запрос к ```http://127.0.0.1:8000/api/v1/posts/```
```
{
    {
    "id": 1,
    "text": "test post",
    "pub_date": "2023-01-23T17:13:43.136548Z",
    "author": "superuser",
    "image": null,
    "group": null
    }
}
```
