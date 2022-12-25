# Installing
1. 
+ `git clone https://github.com/hrumarko/user-authentication-django`
+ `cd user-authentication-django`
---
2. 
  + `python3 -m venv venv` - for Linux
  + `python -m venv venv` - for Windows
  + `virtualenv venv` - for macOS
---
3. 
+ `source venv/bin/activate` - for Linux/macOS
+ `venv\Scripts\activate` - for Windows
---
4. `pip install -r requirements.txt`
---
5. `python3 manage.py migrate`
---
6. `python manage.py runserver`
---
7. Go to http://127.0.0.1:8000/
