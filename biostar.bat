REM activate virtualenv
start C:\git\biostar-central-virtualenv\Scripts\activate.bat
SET DJANGO_SETTINGS_MODULE=biostar.settings.base
SET PATH=C:\git\sqlite3;%PATH%
python manage.py runserver