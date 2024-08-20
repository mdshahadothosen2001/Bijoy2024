# DRD_Evaluation_Task
Django Rest Developer Evaluation Task

# APIs endpoints (based on task)
1. Initialize the project

First, create and activate a virtual environment, then install the required packages, after completion run the project.
Follow these commands-

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements/development.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

2. Sign Up API
```bash
{base}/user/sign-up/
```
Method: POST <br>
Body: email, password must be required and first name and last name optional,
data like
```bash
{
    "email": "p.ms.hosen@gmail.com",
    "first_name": "Md. Shahadot",
    "last_name": "Hosen",
    "password": "sohanmondol"
}
```

3. Add and list users API
```bash
{base}/user/add-or-list/
```
Firstly Add Users API is required<br>
Method: POST<br>
Token: Access token required<br>
Body: email, password must be required and first name and last name optional for each user,
data like
```bash
{
    "email": "p.ms.hosen@gmail.com",
    "first_name": "MD. SHAHADOT",
    "last_name": "HOSEN",
    "password": "sohanmondol"
}
```
or more than one users add at a time
```bash
[
    {
    "email": "p.ms.hosen11@gmail.com",
    "first_name": "MD. SHAHADOT",
    "last_name": "HOSEN",
    "password": "sohanmondol"
    },
    {
    "email": "p.ms.hosen12@gmail.com",
    "first_name": "SINTHIYA",
    "last_name": "HOSEN",
    "password": "sohanmondol"
    }
]
```

Second API for user list required<br>

Method: GET<br>
Token: Access token required

4. Update and Delete a user
```bash
{base}/user/profile-update/
```
Firstly API for update a user profile required<br>
Method: PATCH<br>
Token: Access token required<br>
Body: first name and last name, user can update only one attribute,
data like
```bash
{
    "first_name": "MD. SHAHADOT",
    "last_name": "HOSEN",
}
```

Secondly API for delete a user profile<br>
Method: DELETE<br>
Token: Access token required




# Extra APIs for Token
1. Token
```bash
{base}/user/token/
```
Method: POST<br>
Body: email, password,
data like
```bash
{
    "email": "p.ms.hosen@gmail.com",
    "password": "sohanmondol"
}
```

2. Refresh token
```bash
{base}/user/token/refresh/
```
Method: POST<br>
Body: refresh,
data like
```bash
{
 "refresh": "eyJ.....g1OGg"
}
```


<mark>Note: Must be APIs {base} replaced by actual.</mark>
