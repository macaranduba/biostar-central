@echo off
echo Activating application's virtualenv...
set biostar_env=C:\git\biostar-central-virtualenv
echo biostar-central-virtualenv PATH: %BIOSTAR_ENV%
call %BIOSTAR_ENV%\Scripts\activate.bat
echo Virtualenv activated!
echo Setting DJANGO_SETTINGS_MODULE
SET DJANGO_SETTINGS_MODULE=biostar.settings.base
echo %DJANGO_SETTINGS_MODULE%
echo Setting SQLITE3 in PATH...
SET PATH=C:\git\sqlite3;%PATH%
echo Ready!!
echo %PATH%
echo Launching Django server
call python manage.py runserver
echo Server is down
pause
