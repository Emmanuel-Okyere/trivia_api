## Table of Contents
- [List of Categories](#get_all_category)
- [Create a Category](#add_category)
- [Delete question](#delete_category)
- [Create question ](#add_question)
- [List of question](#get_all_questions)


```
<a name="add_category"></a>

## Create Book Category

This API endpoint is used to create book category.
**Note** Only authenticated, libarian users can access this endpoint.

### Request Information

| Type | URL        |
| ---- | ---------- |
| POST | /questions |

### Header

| Type         | Property name    |
| ------------ | ---------------- |
| Allow        | POST             |
| Content-Type | application/json |

### JSON Body

| Property Name | type   | required | Description              |
| ------------- | ------ | -------- | ------------------------ |
| question      | string | true     | Question to be asked     |
| answer        | string | true     | Answer to the question   |
| category      | int    | true     | Category of the question |
| difficulty    | int    | true     | The level od difficulty  |

### Error Responses

| Code | Message       |
| ---- | ------------- |
| 400  | BAD REQUEST   |
| 422  | UNPROCESSABLE |

### Successful Response Example

```
{
    "data": {
        "answer": "This is the answer",
        "category": 2,
        "difficulty": 3,
        "question": "Here is a question"
    },
    "details": "Question created",
    "status": "success"
}
```

<a name="get_all_category"></a>

## Get Book Categories

This API endpoint is used to create book category.
**Note** Only authenticated, libarian users can access this endpoint.

### Request Information

| Type | URL         |
| ---- | ----------- |
| GET  | /categories |

### Header

| Type         | Property name    |
| ------------ | ---------------- |
| Allow        | GET              |
| Content-Type | application/json |

### Error Responses

| Code | Message   |
| ---- | --------- |
| 404  | NOT FOUND |


### Successful Response Example

```
{
    "categories": {
        "1": "Science",
        "2": "Art",
        "3": "Geography",
        "4": "History",
        "5": "Entertainment",
        "6": "Sports"
    },
    "status": "success"
}

```

<a name="delete_category"></a>

## Delete Question Category

This API endpoint is used to delete a book category.
**Note** Only authenticated, libarian users can access this endpoint.

### Request Information

| Type   | URL                 |
| ------ | ------------------- |
| DELETE | /questions/{int:pk} |

### Header

| Type         | Property name    |
| ------------ | ---------------- |
| Allow        | DELETE           |
| Content-Type | application/json |

### Error Responses

| Code | Message   |
| ---- | --------- |
| 400  | NOT FOUND |

### Successful Response Example

```
{
    "message": "Deleted 32",
    "status": "success"
}
```

<a name="add_question"></a>

## Create Questions

This API endpoint is used to create book to a category.
**Note** Only authenticated, libarian users can access this endpoint.

### Request Information

| Type | URL        |
| ---- | ---------- |
| POST | /questions |

### Header

| Type          | Property name    |
| ------------- | ---------------- |
| Allow         | POST             |
| Content-Type  | application/json |
| Authorization | IsSuperUser      |

### JSON Body

| Property Name | type    | required | Description          |
| ------------- | ------- | -------- | -------------------- |
| category      | string  | true     | Id of book category  |
| title         | string  | true     | Title of book        |
| description   | string  | true     | Description of book  |
| is_available  | boolean | true     | Availability of book |
| image         | image   | true     | Image of book        |



### Error Responses

| Code | Message         |
| ---- | --------------- |
| 400  | BAD REQUEST     |
| 400  | feilds required |
| 401  | UNAUTHORIZED    |
| 403  | FORBIDDEN       |

### Successful Response Example

```
{
    "status": "success",
    "details": "book added successfully",
    "data": {
        "category_id": 2,
        "title": "Robotics for all",
        "description": "I am testing this",
        "is_available": true,
        "image": "/media/images/2022/06/05/57065066.png"
    }
}
```

<a name="get _all_questions"></a>

## Get all Books

This API endpoint is used to view all book.
**Note** Only authenticated, libarian users can access this endpoint.

### Request Information

| Type | URL         |
| ---- | ----------- |
| GET  | /api/books/ |

### Header

| Type          | Property name    |
| ------------- | ---------------- |
| Allow         | GET              |
| Content-Type  | application/json |
| Authorization | IsSuperUser      |

### Error Responses

| Code | Message      |
| ---- | ------------ |
| 400  | BAD REQUEST  |
| 401  | UNAUTHORIZED |
| 403  | FORBIDDEN    |

### Successful Response Example

```
[
    {
        "id": 1,
        "name": "History"
    },
    {
        "id": 2,
        "name": "Social Science"
    }
]

```

<a name="delete_book"></a>

## Delete Book

This API endpoint is used to delete a book.
**Note** Only authenticated, libarian users can access this endpoint.

### Request Information

| Type   | URL                 |
| ------ | ------------------- |
| DELETE | /api/books/{int:pk} |

### Header

| Type          | Property name    |
| ------------- | ---------------- |
| Allow         | DELETE           |
| Content-Type  | application/json |
| Authorization | IsSuperUser      |

### Error Responses

| Code | Message        |
| ---- | -------------- |
| 400  | BAD REQUEST    |
| 400  | Does not exits |
| 401  | UNAUTHORIZED   |
| 403  | FORBIDDEN      |

### Successful Response Example

```
{
      "status": "success",
      "details":"book deleted"
}
```

