# Space Shop #

## Pre-requirements ##
* Python >= 3.5
* PostgreSQL >= 9.5
* virtualenv

## Installation ##

#### Dev ####
1. Clone project [Space-Shop](https://github.com/Stanislav-Rybonka/spaceshop.git)
2. Configure  database according to (Database settings), example below; 
3. Go to the project root directory "spaceshop", through your terminal or other way;
4. Run script setup.sh e.g.(sh setup.sh), this script will install all dependencies
5. Run script update.sh e.g.(sh update.sh), for set up needed options and special commands;
6. After that you should set project interpreter from virtual environment from ./soft_environment/python_env, e.g.(./soft_environment/python_env/bin/python3.5);
7. Also need create django-server in your IDE, if you are use it.
#### Commonly step 5 and 6 should do in the IDE. ####

## Database settings ## 

Create `local_settings.py`, in `spaceshop` package, with database options like this:
```python
DATABASES = {
    'default': {
        'NAME': 'spaceshop',
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'USER': 'root',
        'PASSWORD': 'root',
        'PORT': '5432',
        'HOST': 'localhost',

    },
}
```

###### Recommended PyCharm plugins  ######
* Markdown support
* BashSupport

### Production ###


## Developments idioms ##

* PEP8