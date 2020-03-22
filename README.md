# User Managment Microservice
## [REST API Endpoints Documentation](https://editor.swagger.io/?url=https://raw.githubusercontent.com/E-Edu/draft-documents/master/swagger/user.yaml)
## Explanations 
### Role
0 = Student\
1 = Teacher\
2 = Admin\
3 = Privileged Student
### Status
0 = Unverified\
1 = Verified\
2 = Reported\
3 = Banned
## Enviroment Variables
- DATABASE_HOSTNAME=localhost
- DATABASE_PORT=3306
- DATABASE_USERNAME=userms
- DATABASE_PASSWORD=userms
- DATABASE_DATABASE=userms
- SMTP_HOST=server.url
- SMTP_PORT=587
- SMTP_USERNAME=user@name.email
- SMTP_PORT=password
- JWT_TOKEN=jwt_private_key
- SERVICE_TOKEN=a_service_token_to_communicate

### JWT (Json Web Token) [[Infos](https://jwt.io)]
Response:
```jsonc
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