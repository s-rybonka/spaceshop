# SpaceShop #
[spacehop.com](http://stanislavrybonka.pythonanywhere.com/)

## Pre-requirements ##
* Python >= 3.5
* PostgreSQL >= 9.5
* virtualenv

## Installation ##

#### Dev ####
1. Clone project [SpaceShop](https://github.com/Stanislav-Rybonka/spaceshop.git)
2. Create settings.ini file, example below; 
3. Go to the project root directory "spaceshop", through your terminal or other way;
4. Run script setup.sh e.g.(sh setup.sh), this script will install all dependencies
5. Run script update.sh e.g.(sh update.sh), for set up needed options and special commands, also create admin user with credentials (email=root@spaceshop.com, password=root);;
6. After that you should set project interpreter from virtual environment from ./soft_environment/python_env, e.g.(./soft_environment/python_env/bin/python3.5);
7. Also need create django-server in your IDE, if you are use it.
8. Would you like use pip for instalation or other, don't forget activate python env, like we do it above
#### Commonly step 5 and 6 should do in IDE. ####

## Settings ## 

Create `settings.ini`,file in `project root`  with options like this:
```python
[settings]
DEBUG=True
ALLOWED_HOSTS=.127.0.0.1
SECRET_KEY=stf)=8djmvems$$lnmc-2@o9puwf&$u(ui51nvdy2vs$)%%d$v+
DB_NAME=spaceshopdb
DB_USER=root
DB_PASSWORD=root
DB_HOST=127.0.0.1
DOMAIN_NAME=localhost:8000
```
##### Don't forget about database, you should create it alone, configure roles and permissions if you have some special


###### Recommended PyCharm plugins  ######
* Markdown support
* BashSupport

### Production ###
1. Clone project [SpaceShop](https://github.com/Stanislav-Rybonka/spaceshop.git)
2. Create settings.ini file, example below; 
3. Go to the project root directory "spaceshop", through your terminal or other way;
4. Run script setup.sh e.g.(sh setup.sh), this script will install all dependencies 
5. Run script update.sh e.g.(sh update.sh), for set up needed options and special commands, also create admin user with credentials (email=root@spaceshop.com, password=root);
6. Reload your server
7. Don't forget about python env activation, during your activity on server


## Settings ## 

Create `settings.ini`,file in `project root`  with options like this:
```python
[settings]
DEBUG=False
ALLOWED_HOSTS=your host
SECRET_KEY=your key
DB_NAME=name of your DB
DB_USER= your user
DB_PASSWORD=yiur password
DB_HOST= your DB host
DOMAIN_NAME=your domain name
```
## Developments idioms ##

* PEP8