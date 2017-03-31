SET allurePath=allure-commandline\bin\allure
SET virtualenv=solit_cloud\Scripts\activate
SET reportPath=allure

call %allurePath% report clean
call %virtualenv%
pytest.exe --alluredir=%reportPath% test_main.py
call %allurePath% generate %reportPath%
call %allurePath% report open