# Code-share-django
This is a simple code snippet sharing app that lets you share code snippets with easy copy paste options and a unique url

## Tech stack
- **Frontend:** HTML/CSS
- **Backend:** Python/Django

## Install

- Clone repo using
  ```
  git clone git@github.com:4lexbit/code-share-django.git

- Install dependencies using
  ```
  pip install -r requirements.txt
  
- In setting.py replace the existing code with this code
  ```
  DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
  }
 
 
- Make migrations using
  ```
  .src/manage.py makemigrations

- Migrate Database
  ```
  .src/manage.py migrate

- Create a superuser
  ```
  .src/manage.py createsuperuser
  
- Run server using
  ```
  .src/manage.py runserver
  
### Demo
Available at this [link](https://snippet-share-django.herokuapp.com/)