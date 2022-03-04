from selenium.webdriver.common.by import By


class MainPageLocatorsWhiter:
    """In this class presented Constants for email-owner. Constants are sorted by filling logic."""
    LOGIN = ""  # White login until '@' in this Constant to log in your email , type 'str'.
    PASSWORD = ""  # White password in this Constant to log in your email, type 'str'.


class MainPageLocatorsEmail:
    """In this class presented Constants for writing mail. Constants are sorted by filling logic."""
    EMAIL_TO_SEND_MESSAGE = ""  # You can change sending mail-address by this Constant, type 'str'.
    SUBJECT_IN_SEND_MESSAGE = "Тестовое письмо"  # You can change mail subject editing this Constant, type 'str'.
    BODY_IN_SEND_MESSAGE = "Текст тестового письма."  # You can change mail-message editing this Constant, type 'str'


class MainPageLocators:
    """In this class presented all locators for test-parser. Constants sorted alphabetically."""
    ENTER_PASSWORD_BUTTON = (By.XPATH, "//button[@data-test-id='next-button']")
    FRAME_LOGIN = (By.XPATH, "//iframe[contains(@class, 'ag-popup')]")
    LETTER_BODY_MESSAGE = (By.XPATH, "//div[@role='textbox']/div[1]")
    LETTER_EMAIL_ADDRESS = (By.XPATH, "//div[contains(@class, 'contacts')]//input")
    LETTER_SEND_BUTTON = (By.XPATH, "//span[contains(@class, 'button2_primary')]")
    LETTER_SUBJECT = (By.XPATH, "//div[contains(@class, 'subject')]//input")
    LOGIN_INPUT_FIELD = (By.XPATH, "//input[@name='username']")
    LOGIN_LINK = (By.XPATH, "//button[@data-testid='enter-mail-primary']")
    PASSWORD_INPUT_FIELD = (By.XPATH, "//input[@name='password']")
    SIGN_IN_BUTTON = (By.XPATH, "//button[@data-test-id='submit-button']")
    SUCCESS_LETTER_MESSAGE = (By.XPATH, "//a[@class='layer__link']")
    WRITE_LETTER_BUTTON = (By.XPATH, "//a[contains(@class, 'compose-button')]")
