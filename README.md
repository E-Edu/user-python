# User Managment Microservice
## JWT 
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
## Enviroment Variables
- DATABASE_HOSTNAME        ="localhost"
- DATABASE_PORT            =3306
- DATABASE_USERNAME        ="e-edu"
- DATABASE_PASSWORD        ="e-edu"
- DATABASE_DATABASE        ="e-edu"
- PRODUCTIVE               =true
- BASE_URL                 ="e-edu.the-morpheus.de"
- JWT_SECRET               ="somesecrettokenshere"
- SERVICE_SECRET           ="somesecrettokenshere"