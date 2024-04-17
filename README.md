# django_jwt_demo
- [Notes](https://github.com/jeyu54217/Notes/blob/main/Web/Security/JWT.md)
## Setting Up
### Enviroment

```
pip install -r requirements.txt
```
```
python3 manage.py makemigrations
```
```
python3 manage.py migrate
```

### User Registration
```
python3 manage.py shell
from app.models import User
User.objects.create(user_name="test_user_01", user_password="321")
python3 manage.py runserver 8000
```

## API Test
### Login
- URL: [http://127.0.0.1:8000/api/login](http://127.0.0.1:8000/api/login)
- Method: POST
- Body: {"user_name": "test_user_01", "user_psw": "321"}
- Response: {"msg": 'You got the token!', 'JWT':< Your Login JWT>}
- or
    ```
    curl -d '{"user_name": "test_user_01", "user_psw": "321"}' -H 'Content-Type: application/json' http://127.0.0.1:8000/api/login
    ```
### Test_Token
- URL: [http://127.0.0.1:8000/api/test_token](http://127.0.0.1:8000/api/test_token)
- Method: POST
- Body: {"JWT":< Your Login JWT>}
- Response: {"msg": "Token is still valid and active"}
- or
    ```bash
    curl -d '{"JWT": "<Your JWT>"}' -H 'Content-Type: application/json' http://127.0.0.1:8000/api/test_token
    ```
### DEMO
#### Login
![image](https://github.com/jeyu54217/django_jwt_demo/blob/main/jwt_demo/img/login.png?raw=true)
#### Test_Token
![image](https://github.com/jeyu54217/django_jwt_demo/blob/main/jwt_demo/img/test_token.png?raw=true)

## References
- [Introduction to JSON Web Tokens - JWT](https://jwt.io/introduction)
- [RFC 7519](https://www.rfc-editor.org/rfc/rfc7519)
- [pyjwt API Reference](https://pyjwt.readthedocs.io/en/stable/api.html)


