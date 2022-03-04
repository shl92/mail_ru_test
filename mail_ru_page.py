from selenium.webdriver import Remote as RemoteWebDriver
from selenium.webdriver.support import expected_conditions as EC
import selenium.common.exceptions as EXC
from selenium.webdriver.support.ui import WebDriverWait
from locators import MainPageLocators, MainPageLocatorsWhiter, MainPageLocatorsEmail


class MailRuPage:
    """Main Class for page 'mail.ru'."""
    def __init__(self, browser: RemoteWebDriver, url: str, timeout=10) -> None:
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        """Function to open website"""
        self.browser.get(self.url)

    def link_or_button_click(self, how: object, what: str) -> None:
        """Function for clicking on links or on buttons on website."""
        link_or_button = self.browser.find_element(how, what)
        link_or_button.click()

    def field_input(self, how: object, what: str, input_date: str) -> None:
        """Function for filling input fields with text."""
        field = self.browser.find_element(how, what)
        field.send_keys(input_date)

    def should_be_text_successfully_sent(self) -> None:
        """Function to check if the email has been sent."""
        message = self.browser.find_element(*MainPageLocators.SUCCESS_LETTER_MESSAGE).text
        assert message == "Письмо отправлено", "Mail was not sent."

    def switch_to_frame(self, how: object, what: str) -> None:
        """Function for switching to the first frame."""
        frame = self.browser.find_elements(how, what)[0]
        self.browser.switch_to.frame(frame)

    def wait_until_button_present(self, how: object, what: str) -> bool:
        """Function for waiting the element on website."""
        try:
            return WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((how, what)))
        except (EXC.TimeoutException, EXC.NoSuchWindowException):
            return False

    def mail_ru_login(self) -> None:
        """Function for logging to mail.ru mail-box."""
        self.link_or_button_click(*MainPageLocators.LOGIN_LINK)
        self.switch_to_frame(*MainPageLocators.FRAME_LOGIN)
        self.field_input(*MainPageLocators.LOGIN_INPUT_FIELD, MainPageLocatorsWhiter.LOGIN.strip())
        self.link_or_button_click(*MainPageLocators.ENTER_PASSWORD_BUTTON)
        self.field_input(*MainPageLocators.PASSWORD_INPUT_FIELD, MainPageLocatorsWhiter.PASSWORD.strip())
        self.link_or_button_click(*MainPageLocators.SIGN_IN_BUTTON)
        self.wait_until_button_present(*MainPageLocators.WRITE_LETTER_BUTTON)

    def write_letter(self) -> None:
        """Function for writing message."""
        self.link_or_button_click(*MainPageLocators.WRITE_LETTER_BUTTON)
        self.field_input(*MainPageLocators.LETTER_EMAIL_ADDRESS, MainPageLocatorsEmail.EMAIL_TO_SEND_MESSAGE)
        self.field_input(*MainPageLocators.LETTER_SUBJECT, MainPageLocatorsEmail.SUBJECT_IN_SEND_MESSAGE)
        self.field_input(*MainPageLocators.LETTER_BODY_MESSAGE, MainPageLocatorsEmail.BODY_IN_SEND_MESSAGE)
        self.link_or_button_click(*MainPageLocators.LETTER_SEND_BUTTON)
