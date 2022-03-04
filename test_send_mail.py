from mail_ru_page import MailRuPage


def test_send_mail(browser):
    """Test for mail.ru service: write test message. Input Constants LOGIN and PASSWORD in locators.py before test."""
    URL = "https://mail.ru/"
    page = MailRuPage(browser, URL)
    page.open()
    page.mail_ru_login()
    page.write_letter()
    page.should_be_text_successfully_sent()
