from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGO_IMG = (By.CSS_SELECTOR, ".logo img")                       # Логотип
    COMPANY_NAME = (By.CSS_SELECTOR, ".title_company .name")        # Заголовок компании
    SLOGAN = (By.CSS_SELECTOR, ".title_company .slogan")            # Слоган
    PHONE = (By.CSS_SELECTOR, ".contacts .phone .big-phone")        # Телефон
    ADDRESS = (By.CSS_SELECTOR, ".contacts .address")               # Адрес
    WORK_TIME = (By.CSS_SELECTOR, ".contacts .time")                # Время работы
    SEARCH_INPUT = (By.CSS_SELECTOR, ".search_form input[name='search_string']")     # Поле поиска
    SEARCH_BUTTON = (By.CSS_SELECTOR, ".search_form input[type='submit']")           # Кнопка поиска

    MAIN_MENU = (By.CSS_SELECTOR, ".menu ul.level-0")               # Основное меню
    SERVICES_BLOCK = (By.CSS_SELECTOR, ".index_catalog")            # Блок "Услуги" на главной
    CONTACT_BUTTON = (By.CSS_SELECTOR, "li[data-id='810'] a[href='/forma_zayavki/']")  # Кнопка "Связаться с нами"
    COOKIE_NOTIFICATION = (By.ID, "cookie-notification")            # Уведомление о куках
    ACCEPT_COOKIES_BUTTON = (By.ID, "accept-cookies")               # Кнопка принятия куки
    MENU_SERVICES_LINK = (By.CSS_SELECTOR, ".menu ul.level-0 li a[href='/katalog1/']")     # Ссылка "Услуги" в меню

