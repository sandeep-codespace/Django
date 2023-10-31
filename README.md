Steps to create new projects

# create environment
    -- python -m venv envname

# activate env
    -- envname\scripts\activate
# install django
    -- pip install django
#  start project and runserver
    --  django-admin startproject projectname
    --  cd projectName
    --  python manage.py runserver
# runapp
    -- django-admin startapp appname

# Intsall external dependencies
# install boostrap
    -- pip install django-bootstrap-v5
    update intsalled app in settings.py file
    update INSTALLED_APPS and add bootstrap5 in it