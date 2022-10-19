import jwt
from jwt.exceptions import ExpiredSignatureError, InvalidSignatureError, DecodeError

from datetime import timedelta, datetime
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

from app.models import User

from rest_framework.decorators import api_view
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_200_OK
from rest_framework.response import Response

SECRET_KEY = settings.SECRET_KEY

@csrf_exempt
@api_view(['POST'])

def login(request):
    """
    Copy and paste the json below:
    {"user_name": "test_user_01", "user_psw": "321"}
    """
    post_name = request.data.get('user_name')
    post_psw = request.data.get('user_psw')
    user_auth_check = User.objects.filter(user_name = post_name, user_password = post_psw)
    if post_name is None or post_psw is None:
        return Response(
            {'Error': 'Please provide the user name and password'},
            status = HTTP_400_BAD_REQUEST
            )
    elif user_auth_check:
        payload = {
            ## Registered claims
            "sub" : "test_jwt",  # Subject
            "iss" : "Jerry Yu",  # Issuer
            'iat': datetime.now(),  # Issued At, Should be int
            'exp': datetime.now() + timedelta(minutes = 1),  # Expiration Time, Should be int
            # "aud" : "test_user",  # Audience
            # "jti" : None,  # JWT ID
            ## Privete claims
            'user_name': post_name,
            # 'user_psw': "NEVER DO THIS"
            }
        jwt_token = jwt.encode(payload, SECRET_KEY, algorithm='HS256').decode('utf-8')
        return Response({"msg": 'You got the token!',
                         'JWT': jwt_token,
                         },
                        status =HTTP_200_OK)
    else:
        return Response(
            {'Error': 'Invalid credentials'},
            status = HTTP_404_NOT_FOUND
            )
        
@csrf_exempt
@api_view(['POST'])

def test_token(request):
    """
    {"JWT":<Your Login JWT>}
    """
    encoded_jwt = request.data.get('JWT')
    if encoded_jwt:
        try:
            decode_jwt = jwt.decode(encoded_jwt, SECRET_KEY, algorithms=['HS256'])
            return Response(
                {"msg": "Token is still valid and active",
                 "Encoded_jwt": encoded_jwt,
                 "Decode_jwt": decode_jwt,
                 },
                status =HTTP_200_OK
                )
        except ExpiredSignatureError:
            return Response(
                {'Error': "Token expired. Please get new one"},
                status = HTTP_400_BAD_REQUEST
                )
        except InvalidSignatureError:
            return Response(
                {'Error': "Token expired. Please get new one"},
                status = HTTP_400_BAD_REQUEST
                )
        except DecodeError:
            return Response(
                {'Error': "Invalid header string, Please check your JWT HEADERS"},
                status = HTTP_400_BAD_REQUEST
                )
    else:
        return Response(
            {'Error': 'Please paste your JWT'},
            status = HTTP_400_BAD_REQUEST
            )


"""    
>>> print(type(User.objects.filter(user_name = '??')))
<class 'django.db.models.query.QuerySet'>
>>> print(bool(User.objects.filter(user_name = '??')))
False
>>> print(bool(User.objects.filter(user_name = 'test_user_01')))
True


>>> User.objects.filter(user_name = 'test_user_01', user_password = "321")
<QuerySet [<User: User object (6)>]>
>>> User.objects.filter(user_name = 'test_user_01', user_password = "3211")
<QuerySet []>
>>> User.objects.filter(user_name = 'test_user_01').get(user_name = 'test_user_01',user_password = "321")
<User: User object (6)>
>>> User.objects.filter(user_name = 'test_user_01').get(user_name = 'test_user_01',user_password = "3211")
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "/Users/jy-m1/Library/Mobile Documents/com~apple~CloudDocs/code/code/django_jwt_demo/lib/python3.10/site-packages/django/db/models/query.py", line 650, in get
    raise self.model.DoesNotExist(
app.models.User.DoesNotExist: User matching query does not exist.


>>> User.objects.filter(user_name = 'test_user_01', user_password = "3211").id
Traceback (most recent call last):
  File "<console>", line 1, in <module>
AttributeError: 'QuerySet' object has no attribute 'id'
>>> User.objects.filter(user_name = 'test_user_01', user_password = "3211").get()
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "/Users/jy-m1/Library/Mobile Documents/com~apple~CloudDocs/code/code/django_jwt_demo/lib/python3.10/site-packages/django/db/models/query.py", line 650, in get
    raise self.model.DoesNotExist(
app.models.User.DoesNotExist: User matching query does not exist.
>>> User.objects.filter(user_name = 'test_user_01', user_password = "321").get()
<User: User object (6)>
"""