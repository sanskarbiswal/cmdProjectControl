@ECHO OFF
:: Change User Directory and Read Project Dir as Parameter
cd /d F:
set dir = %1

ECHO =====================================
ECHO ========= DELETE PROJECT ============
ECHO =====================================

:: Verify User Choice

::set /p var = "Remove Project ? (y/n) : "

python rmvProject.py %1

::IF "%v%"=="y"(
::    python rmvProject.py %1
::) ELSE (
::    pause
::)