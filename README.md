# Task-Backend-1

## Table of contents:
- [Tech stack.](#Tech-stack)
- [Description and comments.](#Description-and-comments)
- [API documentation.](#API-documentation)
- [How to deploy.](#How-to-deploy)
- [API request samples.](API-request-samples)

## Tech stack:
- Python
- Django
- DRF
- JWT token authentication
- Gunicorn
- Nginx
- Linux

## Description and comments.
The website is available at https://longevity.ddns.net/
While there is no frontpage available, API endpoints and admin portal are accessible and more information can be found in [API documentation.](#API-documentation

I want to point out straight away the limitations of my project. I failed to properly connect PostgreSQL database. I struggled to apply my models when I set up the database. Since I could not identify the root cause of the problem I decided to continue with Sqlite. I did try another approach (that was my first choice, hence the name of the current project being longevity2) of using Docker containers system. While I managed to compile backend, nginx and postgresql database container system and deploy it on my server, only admin address worked and I couldn't figure out what the problem with authentication was. Prioritizing the actual launch of the project over this issue I opted to get rid of containers with 2 nginx setup (one inside container and one outside on a server) and instead go with gunicorn and nginx with simply deploying my code from github on my remote server. Therefore, Postgres part is not done and Sqlite is used instead.

I also did not do the Celery part. The reason is I do not know this technology yet and I estimate I need at least several days to get the hang of it and then use it. While I would definitely learn it should it be the 'real' project the reason I decided to not do it here is time constaints. 

Those choices affected the other processes. For example, one of the requirements for passwords was hashing and storage and from what I have checked in Sqlite, hashes have already been in place, so I just used the default way of storying them.

Standard error handling is used.

As per requirements, I made a customer user model that uses email as login means as well as the unique identifier.

## API documentation.
All API endpoint instructions can be checked at https://longevity.ddns.net/swagger/

## How to deploy.
You do not need to deploy anything to access the current project's API endpoints, but here are the instructions just in case:
1. Clone the repository:

```
git clone git@github.com:gaifut/longevity2.git
```
2. Go to the cloned directory:
```
cd Test_Django_Alfa_Ecosystem/task2/product_store
```

3. Create and activate virtual environment:

```
python3 -m venv venv
```

```
. venv/bin/activate
```
4. Go to the directory where manage.py file is and create .env file, for example with command:
   ```
   nano .env
   ```
   In that file add the following infomration:
   SECRET_KEY=django project key
   DEBUG=False
   ALLOWED_HOSTS= all of your hosts like local ones 127.0.0.1, localhost, as well as remote host IP address and domain name.

6. Install dependencies from a file requirements.txt:

```
pip install --upgrade pip
```

```
pip install -r requirements.txt
```

6. Make migrations:

```
python3 manage.py migrate
```

7. Install gunicorn if you don't have it:
```
pip install gunicorn
```
8. Run the server:

```
gunicorn --bind 0.0.0.0:8000 longevity2.wsgi
```

## API request samples.

### Create user
Type of request: POST.

URL:
```
http://longevity.ddns.net:8000/auth/users/
```
Request body:
{
    "username": "string",
    "password": "string",
    "email": "string"
}

### Get JWT token
Type of request: POST.

URL:
```
http://longevity.ddns.net:8000/auth/jwt/create/
```

Request body:
```
{
  "username": "string",
  "password": "string"
  "email": "string"
}
```
#### Get user's profile
Type of request: GET.

URL:
```
http://longevity.ddns.net:8000/api/profiles/
```
