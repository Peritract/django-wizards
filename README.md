# Django Wizards

A repository contained an example deployable Django App

## Deployment process

- Create repository
- Create Heroku app
- Add Postgres to app
- Add `DISABLE_COLLECTSTATIC` to Heroku config variables, with value `1`
- Add `PRODUCTION` to Heroku config variables, with value `True`
- Deploy the app to Heroku
- Use the Heroku CLI or the web terminal to run the following commands:
    - `python manage.py makemigrations`
    - `python manage.py migrate`
    - `python manage.py createsuperuser` (optional)