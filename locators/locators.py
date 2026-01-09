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

    '''Локаторы для кнопок услуг на главной странице'''
    SERVICE_RENGA = (By.XPATH, "//div[contains(@class, 'category_title_bottom')]//a[text()='Renga. Поставка и сопровождение']")
    SERVICE_BIM_LEARNING = (By.XPATH, "//div[contains(@class, 'category_title_bottom')]//a[text()='Обучение работе с BIM']")
    SERVICE_BIM_PROJECTING = (By.XPATH, "//div[contains(@class, 'category_title_bottom')]//a[text()='BIM-проектирование. Сметы по BIM']")
    SERVICE_SMETA_PROGRAMS = (By.XPATH, "//div[contains(@class, 'category_title_bottom')]//a[text()='Программы для сметно-строительного комплекса']")
    SERVICE_PROJECT_PROGRAMS = (By.XPATH, "//div[contains(@class, 'category_title_bottom')]//a[text()='Программы для проектно-изыскательных работ']")
    SERVICE_ADVOKAT = (By.XPATH, "//div[contains(@class, 'category_title_bottom')]//a[text()='Адвокат в кармане']")
    SERVICE_DISTANT_LEARNING = (By.XPATH, "//div[contains(@class, 'category_title_bottom')]//a[text()='Образовательные услуги дистанционно']")
    SERVICE_SMETA_COURSES = (By.XPATH, "//div[contains(@class, 'object_title_bottom')]//a[text()='Обучение сметному делу']")

class RengaPageLocators:
    RENGA_CONTACT_BUTTON = (By.XPATH, "//a[text()='Получить консультацию по покупке программы']")  # Кнопка перехода к Контактам
    RENGA_STANDART_LINK = (By.CSS_SELECTOR, "a.catalog_item_img[href='/katalog1/renga_postavka_i_soprovozhdenie/vozmozhnosti_renga_standard/']") # Кнопка перехода к Renga Stangart
    RENGA_PROFESSIONAL_LINK = (By.CSS_SELECTOR, "a.catalog_item_img[href='/katalog1/renga_postavka_i_soprovozhdenie/vozmozhnosti_renga_professional/']") # Кнопка перехода к Renga Prof

class BimWizardPageLocators:
    WIZARD_CONTACT_BUTTON = (By.XPATH, "//a[text()='Получить помощь по подбору программы']") # Кнопка перехода к Контактам

class SmetaProgramsPageLocators:
    SMETA_PROGRAMS_CONTACT_BUTTON_UP = (By.XPATH, "(//a[text()='Получить помощь по подбору программы'])[1]") # Верхняя Кнопка перехода к Контактам
    SMETA_PROGRAMS_CONTACT_BUTTON_DOWN = (By.XPATH, "(//a[text()='Получить помощь по подбору программы'])[2]") # Нижняя Кнопка перехода к Контактам

class ProjectPrigramsPageLocators:
    PROJECT_PROGRAMS_CONTACT_BUTTON = (By.XPATH, "//a[text()='Получить помощь по подбору программы']") # Кнопка перехода к Контактам

class AdvokatPageLocators:
    ADVOKAT_CONTACT_BUTTON_UP = (By.XPATH, "//a[text()='Узнать, как это работает']") # Верхняя Кнопка перехода к Контактам
    ADVOKAT_CONTACT_BUTTON_DOWN = (By.XPATH, "//a[text()='Купить абонемент']") # Нижняя Кнопка перехода к Контактам

class DistantLearningPageLocators:
    DISTANT_LEARNING_CONTACT_BUTTON_UP = (By.XPATH, "//a[text()='Получить консультацию']") # Верхняя Кнопка перехода к Контактам
    DISTANT_LEARNING_CONTACT_BUTTON_DOWN = (By.XPATH, "//a[text()='Подобрать курс']") # Нижняя Кнопка перехода к Контактам