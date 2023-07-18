@echo off
cmd /k "cd %~dp0\Env\Scripts & activate & cd /d %~dp0\myweb & python manage.py runserver"