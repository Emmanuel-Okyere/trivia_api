# TRIVIA API DOCUMENTATION
## Table of Contents
- [List of Categories](#get_all_category)
- [Create Categories](#add_category)
- [List of question](#get_all_questions)
- [Create question ](#add_question)
- [Delete question](#delete_question)
- [Search for a question](#search_question)
- [Get Question by Category](#question_by_category)
- [Post a Quiz to Play](#quiz)



<a name="get_all_category"></a>

## Get all Categories

This API endpoint is used to get all categories.

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
        "6": "Sports",
        "7": "School",
        "8": "News"
    },
    "status": "success"
}
```

<a name="add_category"></a>

## Create Categories

This API endpoint is used to create a category.

### Request Information

| Type | URL         |
| ---- | ----------- |
| POST | /categories |

### Header

| Type         | Property name    |
| ------------ | ---------------- |
| Allow        | POST             |
| Content-Type | application/json |

### JSON Body

| Property Name | type   | required | Description |
| ------------- | ------ | -------- | ----------- |
| type          | string | true     | Category    |



### Error Responses

| Code | Message       |
| ---- | ------------- |
| 422  | UNPROCESSABLE |

### Successful Response Example

```
{
    "data": {
        "category": "School"
    },
    "details": "Category created",
    "status": "success"
}
```

<a name="get_all_questions"></a>

## Get all Questions

This API endpoint is used to get all questions.
**Note** This is a paginated endpoint. Pass _?page=number_ as params to the request to return a response of the requested page number. If the number is not found, the first page is used as default.

### Request Information

| Type | URL        |
| ---- | ---------- |
| GET  | /questions |

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
    "questions": [
        {
            "answer": "Agra",
            "category": 3,
            "difficulty": 2,
            "id": 15,
            "question": "The Taj Mahal is located in which Indian city?"
        },
        {
            "answer": "Escher",
            "category": 2,
            "difficulty": 1,
            "id": 16,
            "question": "Which Dutch graphic artist–initials M C was a creator of optical illusions?"
        }
    ]
    "status": "success",
    "total_questions": 2
}

```

<a name="add_question"></a>

## Create Questions

This API endpoint is used to create a question.

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

| Property Name | type   | required | Description                      |
| ------------- | ------ | -------- | -------------------------------- |
| question      | string | true     | Question                         |
| answer        | string | true     | Answer to the question           |
| category      | int    | true     | Category for the question        |
| difficulty    | int    | true     | Difficulty level of the question |



### Error Responses

| Code | Message       |
| ---- | ------------- |
| 422  | UNPROCESSABLE |

### Successful Response Example

```
{
    "data": {
        "answer": "This is the answer",
        "category": 2,
        "difficulty": 6,
        "question": "Here is a question"
    },
    "details": "Question created",
    "status": "success"
}
```


<a name="delete_question"></a>

## Delete Question

This API endpoint is used to delete a category.
**Note** Deletion can be done with only **int** type id.

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

| Code | Message       |
| ---- | ------------- |
| 404  | NOT FOUND     |
| 422  | UNPROCESSABLE |

### Successful Response Example

```
{
    "message": "Deleted 32",
    "status": "success"
}
```


<a name="search_question"></a>

## Search for a Question

This API endpoint is used search for a question with a keyword.

### Request Information

| Type   | URL     |
| ------ | ------- |
| DELETE | /search |

### Header

| Type         | Property name    |
| ------------ | ---------------- |
| Allow        | POST             |
| Content-Type | application/json |

### JSON Body

| Property Name | type   | required | Description              |
| ------------- | ------ | -------- | ------------------------ |
| search        | string | true     | Parameter to be searched |

### Error Responses

| Code | Message     |
| ---- | ----------- |
| 404  | NOT FOUND   |
| 400  | BAD REQUEST |

### Successful Response Example (_searched for title_)

```
{
    "questions": [
        {
            "answer": "Maya Angelou",
            "category": 4,
            "difficulty": 2,
            "id": 5,
            "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
        },
        {
            "answer": "Edward Scissorhands",
            "category": 5,
            "difficulty": 3,
            "id": 6,
            "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
        }
    ],
    "status": "success",
    "total_questions": 2
}
```


<a name="question_by_category"></a>

## Get Questions by Category

This API endpoint is used to get the questions for a specific category.
**Note** Deletion can be done with only **int** type id.

### Request Information

| Type   | URL                                   |
| ------ | ------------------------------------- |
| DELETE | /category/{int:category_id}/questions |

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
    "category": 6,
    "questions": [
        {
            "answer": "Brazil",
            "category": 6,
            "difficulty": 3,
            "id": 10,
            "question": "Which is the only team to play in every soccer World Cup tournament?"
        },
        {
            "answer": "Uruguay",
            "category": 6,
            "difficulty": 4,
            "id": 11,
            "question": "Which country won the first ever soccer World Cup in 1930?"
        }
    ],
    "status": "success",
    "total_questions": 2
}
```

<a name="quiz"></a>

## Post a quiz to play

This API endpoint is used to get random question to answer.
**note** This uses JSON request parameters of category and previous questions.


Sample request: `curl http://127.0.0.1:5000/quizzes -X POST -H "Content-Type: application/json" -d '{"previous_question": [12, 8, 2, 19, 34], "category": {"type": "Entertainment", "id": "5"}}'`
### Request Information

| Type | URL   |
| ---- | ----- |
| POST | /quiz |

### Header

| Type         | Property name    |
| ------------ | ---------------- |
| Allow        | POST             |
| Content-Type | application/json |

### JSON Body

| Property Name     | type | required | Description                  |
| ----------------- | ---- | -------- | ---------------------------- |
| previous_question | dict | true     | Previous question dictionary |
| category          | dict | true     | Category of that question    |


### Error Responses

| Code | Message     |
| ---- | ----------- |
| 400  | BAD REQUEST |

### Successful Response Example

```
{
    "question": {
        "answer": "Agra",
        "category": 3,
        "difficulty": 2,
        "id": 15,
        "question": "The Taj Mahal is located in which Indian city?"
    },
    "status": "success"
}
```

