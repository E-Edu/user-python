# User Managment Microservice
## REST API Endpoints
### Register User
**[POST] /user/register**\
Body:
```json
{
    "email": "String",
    "password": "String",
    "first_name": "String",
    "last_name": "String",
    "teacher_token": "String"
}
```
Response:
```json
{
    "error": "String" // only present on response codes 40x
}
```
### Verify User
**[PATCH] /user/verify**\
Body:
```json
{
    "token": "String"
}
```
Response:
```json
{
    "error": "String", // only present on response codes 40x
    "session": "Guid|null"
}
```
### Login User
**[POST] /user/login**\
Body:
```json
{
    "email": "String",
    "password": "String"
}
```
Response:
```json
{
    "error": "String", // only present on response codes 40x
    "session": "Guid|null"
}
```
### User Info
**[POST] /user/info**\
Body:
```json
{
    "session": "Guid",
    "user": "Guid|null"
}
```
Response:
```json
{
    "error": "String", // only present on response codes 40x
    "teacher": "Boolean",
    "admin": "Boolean",
    "privileged_student": "Boolean",
    "report_spammer": "Number"
}
```
### Update User
**[PUT] /user/update**\
Body:
```json
{
    "session": "Guid",
    "user": "Guid|null",
    "teacher": "Boolean|null",
    "admin": "Boolean|null",
    "privileged_student": "Boolean|null",
    "report_spammer": "Boolean|null"
}
```
Response:
```json
{
    "error": "String" // only present on response codes 40x
}
```

