REM activate virtualenv
call C:\git\biostar-central-virtualenv\Scripts\activate.bat
echo "Virtual Env activated"
SET DJANGO_SETTINGS_MODULE=biostar.settings.base
echo "Django Settings done"
SET PATH=C:\git\sqlite3;%PATH%
echo "PATH updated with Sqlite3 for this run"
call python manage.py runserver
echo "Server is down"
pause
