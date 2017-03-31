# solitclauds
Для запуска задания необходимо (под windows 7/10)
1) Установить Chrome 57
https://www.google.ru/chrome/browser/desktop/#
2) Скачать chromedriver.exe и положить в любую папку, которая есть в переменной PATH (список папок можно увидеть в cmd->SET)
https://chromedriver.storage.googleapis.com/2.28/chromedriver_win32.zip
3) Установить python 3.5.2 x86
https://www.python.org/ftp/python/3.5.2/python-3.5.2.exe
4) Перейти в папку с задание и запустить setup.bat
Должно создаться виртуальное окружение и установиться необходимые библиотеки
5) Запустить run_test_and_generate_report.bat
* Запустится тест
* сгенерируется xml для allure report
* сгенерируется allure report
* откроется отчет в браузере
