# User Managment Microservice
## JWT 
Response:
```json
{
  "id": "int",
  "session_token": "string",
  "email": "string",
  "first_name": "string",
  "last_name": "string",
  "role": "int",
  "status": "int"
}
```
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
Response:\
__Success:__\
Status Code: `201`\
__Error:__
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
Response:\
__Success:__\
Status Code: `200`\
__Error:__
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
Response:\
__Success:__\
Status Code: `200`\
__Error:__
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
Response:\
__Success:__\
Status Code: `200`\
```json
{
    "teacher": "Boolean",
    "admin": "Boolean",
    "privileged_student": "Boolean",
    "report_spammer": "Number"
}
```
__Error:__
```json
{
    "error": "String" // only present on response codes 40x
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
Response:\
__Success:__\
Status Code: `200`\
__Error:__
```json
{
    "error": "String" // only present on response codes 40x
}
```
### User Session
**[POST] /user/session**\
Body:
```json
{
    "session_token": "string"
}
```
Response:\
__Success:__\
Status Code: `200`\
__Error:__
```json
{
    "error": "String" // only present on response codes 40x
}
```
## Explanations 
### Role
0 = Student\
1 = Teacher\
2 = Admin
### Status
0 = Unverified\
1 = Verified\
2 = Reported\
3 = Banned
