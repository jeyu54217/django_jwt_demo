# django_jwt_demo

## Set Up
```bash
git clone https://github.com/jeyu54217/django_jwt_demo.git
```
```bash
python3 -m venv <proj_path>
```
```bash
pip install -r requirements.txt
```
```bash
cd jwt_demo
```
```bash
python3 manage.py shell
```
```bash
from app.models import User
```
```bash
User.objects.create(user_name="test_user_01", user_password="321")
```
```bash
python3 manage.py runserver
```
## API Routes
### Login
- URL: [http://127.0.0.1:8000/api/login](http://127.0.0.1:8000/api/login)
- Method: POST
- Body: {"user_name": "test_user_01", "user_psw": "321"}
- Response: {"msg": 'You got the token!', 'JWT':< Your Login JWT>}

### Test_Token
- URL: [http://127.0.0.1:8000/api/test_token](http://127.0.0.1:8000/api/test_token)
- Method: POST
- Token: {"JWT":< Your Login JWT>}
- Response: {"msg": "Token is still valid and active"}
### DEMO
#### Login
![image](https://github.com/jeyu54217/django_jwt_demo/blob/main/jwt_demo/img/login.png?raw=true)
#### Test_Token
![image](https://github.com/jeyu54217/django_jwt_demo/blob/main/jwt_demo/img/test_token.png?raw=true)