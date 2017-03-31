SET virtualenvName=solit_cloud
SET pipPath=%virtualenvName%\Scripts\pip.exe

pip.exe install virtualenv
virtualenv %virtualenvName%
%pipPath% install selenium
%pipPath% install pytest
%pipPath% install pyhamcrest
%pipPath% install pytest-allure-adaptor