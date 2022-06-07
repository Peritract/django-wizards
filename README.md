## Commands

### Database setup

- `python manage.py makemigrations`
- `python manage.py migrate`
- `python manage.py createsuperuser`

### Deployment process

- Create repository
- Create Heroku app
- Add Postgres to app
- Add `DISABLE_COLLECTSTATIC` to Heroku config variables, with value `1`