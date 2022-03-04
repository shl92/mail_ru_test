Test parser for sending mail on mail.ru.
Before test starting please input following information:
- LOGIN in file 'locators.py', where you should write login (without domain '@mail.ru') for your mail.ru account, type string.
- PASSWORD in file 'locators.py', where you should write password for your mail.ru account, type string.
- EMAIL_TO_SEND_MESSAGE in file 'locators.py', where you should write email-address with domain '@mail.ru'.

You can write in terminal: "pytest -v -s --tb=line test_send_mail.py" to start test.
Test should be start using Chrome browser.
Packages can be installed by command in terminal: "pip install -r requirements.txt"