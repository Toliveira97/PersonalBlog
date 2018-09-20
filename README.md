# Personal Website 

A Website that I have built for myself to display my resume and projects on the web. 

## Installation

### To run locally:

1. Install python v3.5 or higher and pip
2. Run pip install -r requirements.txt
3. Load the default.env file, or create your own .env file with your environment variables (check next section):
```bash
$ source dotenv.sh local.env #this will load the environment variables in default.env
```
4. Execute the following:
```bash
$ ./build.sh # to collect static files, build sass
$ ./start_server.sh # to init your database and start your django app
```
5. Visit http://0.0.0.0:8000

### To build and run in docker

1. Load your secret environment variables (check docker-compose.yml for missing envs)
2. Execute
```bash
$ docker-compose up
```

### Docker Backup databse

1. Back up:
```bash
pg_dumpall -U postgres -c > backup/dump_`date +%d-%m-%Y"_"%H_%M_%S`.sql

# or

ssh root@<hostname> cd <source location> && docker-compose exec db pg_dumpall -U postgres -c > backup/dump_`date +%d-%m-%Y"_"%H_%M_%S`.sql
```
2. Restore:
3. 
## Environment Variables

- DEBUG (optional): set this to "y" if you want debug information, leave unset or different from "y" to disable debugging.
- SECRET_KEY: the private key used by django.
- DATABASE_URL: url to the database following the [dj-database-url format](https://github.com/kennethreitz/dj-database-url/blob/master/README.rst)
- P_USERNAME: the username from the Person table (personalWebsite/models.py). A tuple that contains this username will be used to populate the website with data.
- WEBSITE_HOSTNAME: Your hostname with protocol, used to embed the resume pdf for mobile devices. Ex: "http://website-name.com"
- ADMIN_EMAIL: Email of the system admin account. 
- ADMIN_PASS: Password used to to login to the admin account (username 'admin')

## Personalization

You can login to you admin account and populate the website with data by creating various tuples for the database tables. Login at <website>/admin with username 'admin' and the password you specified in the environment variable (default 'admin')

## Features

- Showcase for projects
- Resume display

The blog feature is not implemented yet.

The style follows the [Tomorrow Night](https://github.com/chriskempson/tomorrow-theme) color scheme