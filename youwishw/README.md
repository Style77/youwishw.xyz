# youwishw.xyz

Site created with use of [Django](https://www.djangoproject.com/), inspired by old [picosong](https://picosong.com/), and [Soundcloud](https://soundcloud.com/)

## How to run project on local server

First, you need to install all required packages using command `$ pip install -r requirements.txt` \
then you have to migrate database using commands:

`$ python manage.py makemigrations` and then `$ python manage.py migrate`

To run actual server use `$ python manage.py runserver`, and go to http://127.0.0.1:8000/

## How to create account
I made that website for my friends and me, so there isn't any registration page \
Creating account is little tricky, first you need to make [superuser](https://docs.djangoproject.com/en/1.8/intro/tutorial02/) account. 
Run the following command:

`$ python manage.py createsuperuser`

Enter your desired username and press enter.

`Username: admin`

You will then be prompted for your desired email address:

`Email address: admin@example.com`

The final step is to enter your password. You will be asked to enter your password twice, the second time as a confirmation of the first.

```
Password: ********** 
Password (again): *********
Superuser created successfully.
```


When your superuser is created, you can already log in to page as superuser (it really doesn't matter)\
or create new account in admin panel.

To get to admin panel just go to http://127.0.0.1:8000/admin

### Voilà
<sub>made by [youwish](https://github.com/Style77) </sub>