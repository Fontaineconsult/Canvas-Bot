
@cd C:\Users\913678186\IdeaProjects\Canvas-Bot
echo %1
@C:\Users\913678186\IdeaProjects\Canvas-Bot\venv\Scripts\python.exe C:\Users\913678186\IdeaProjects\Canvas-Bot\bat\run.py %1 > C:\Users\913678186\IdeaProjects\Canvas-Bot\bat\output.txt
@SET MYVAR=<C:\Users\913678186\IdeaProjects\Canvas-Bot\bat\output.txt


echo %MYVAR%
taskkill /IM chromedriver.exe /F
DEL C:\Users\913678186\IdeaProjects\Canvas-Bot\bat\output.txt
@IF %ERRORLEVEL% NEQ 0 PAUSE

