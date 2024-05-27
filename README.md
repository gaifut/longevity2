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

I want to point out straight away the limitations of my project. I failed to properly connect PostgreSQL database. I struggled to apply my models when I set up the database. Since I could not identify the root cause of the problem I decided to continue with Sqlite. I did try another approach (that was my first choice) of using Docker containers system. While I managed to compile backend, nginx and postgresql database container system and deploy it on my server, only admin address worked and I couldn't figure out what the problem with authentication was. Prioritizing the actual launch of the project over this issue I opted to get rid of containers with 2 nginx setup (one inside container and one outside on a server) and instead go with gunicorn and nginx with simply deploying my code from github on my remote server. Therefore, Postgres part is not done and Sqlite is used instead.

I also did not do the Celery part. The reason is I do not know this technology yet and I estimate I need at least several days to get the hang of it and then use it. While I would definitely learn it should it be the 'real' project the reason I decided to not do it here is time constaints. 

Those choices affected the other processes. For example, one of the requirements for passwords was hashing and storage and from what I have checked in Sqlite, hashes have already been in place, so I just used the default way of storying them.

Standard error handling is used.

As per requirements, I made a customer user model that uses email as login means as well as the unique identifier.

## API documentation.
All API endpoint instructions can be checked at https://longevity.ddns.net/swagger/

## How to deploy.

## API request samples.
