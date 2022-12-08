
@cd C:\Users\DanielPC\Desktop\Servers\Canvas-Bot\
echo %1
@C:\Users\DanielPC\Desktop\Servers\Canvas-Bot\root\windowsvenv\Scripts\python.exe C:\Users\DanielPC\Desktop\Servers\Canvas-Bot\bat\run.py %1 > C:\Users\DanielPC\Desktop\Servers\Canvas-Bot\bat\output.txt
@SET MYVAR=<C:\Users\DanielPC\Desktop\Servers\Canvas-Bot\bat\output.txt


echo %MYVAR%
taskkill /IM "chromedriver.exe" /F
DEL C:\Users\DanielPC\Desktop\Servers\Canvas-Bot\bat\output.txt
@IF %ERRORLEVEL% NEQ 0 PAUSE

