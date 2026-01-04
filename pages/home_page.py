from .base_page import BasePage
from locators.locators import MainPageLocators
from data.urls import BasicUrls

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, BasicUrls.HOME)
    
    # Проверки отображения элементов
    
    def is_logo_displayed(self):
        return self.is_element_visible(MainPageLocators.LOGO_IMG)
    
    def is_company_name_displayed(self):
        return self.is_element_visible(MainPageLocators.COMPANY_NAME)
    
    def is_slogan_displayed(self):
        return self.is_element_visible(MainPageLocators.SLOGAN)
    
    def is_phone_displayed(self):
        return self.is_element_visible(MainPageLocators.PHONE)
    
    def is_address_displayed(self):
        return self.is_element_visible(MainPageLocators.ADDRESS)
    
    def is_work_time_displayed(self):
        return self.is_element_visible(MainPageLocators.WORK_TIME)
    
    def is_main_menu_displayed(self):
        return self.is_element_visible(MainPageLocators.MAIN_MENU)
    
    def is_services_block_displayed(self):
        return self.is_element_visible(MainPageLocators.SERVICES_BLOCK)
    
    def is_cookie_notification_displayed(self):
        return self.is_element_visible(MainPageLocators.COOKIE_NOTIFICATION)
    
    def is_accept_cookies_button_displayed(self):
        return self.is_element_visible(MainPageLocators.ACCEPT_COOKIES_BUTTON)
    
    def is_contact_button_displayed(self):
        return self.is_element_visible(MainPageLocators.CONTACT_BUTTON)
    
    def is_search_input_displayed(self):
        return self.is_element_visible(MainPageLocators.SEARCH_INPUT)
    
    def is_search_button_displayed(self):
        return self.is_element_visible(MainPageLocators.SEARCH_BUTTON)
    
    # Получение текста элементов
    
    def get_company_name_text(self):
        return self.get_element_text(MainPageLocators.COMPANY_NAME)
    
    def get_phone_text(self):
        return self.get_element_text(MainPageLocators.PHONE)
    
    def get_address_text(self):
        return self.get_element_text(MainPageLocators.ADDRESS)
    
    def get_work_time_text(self):
        return self.get_element_text(MainPageLocators.WORK_TIME)
    
    def get_slogan_text(self):
        return self.get_element_text(MainPageLocators.SLOGAN)
    
    # Действия с элементами
    
    def accept_cookies(self):
        self.click_element(MainPageLocators.ACCEPT_COOKIES_BUTTON)
    
    def click_contact_button(self):
        self.click_element(MainPageLocators.CONTACT_BUTTON)
    
    def search_for(self, text):
        """Выполнить поиск по тексту"""
        self.input_text(MainPageLocators.SEARCH_INPUT, text)
        self.click_element(MainPageLocators.SEARCH_BUTTON)
    
    # Методы для кликов по блокам услуг
    
    def click_service_renga(self):
        self.click_element(MainPageLocators.SERVICE_RENGA)
    
    def click_service_bim_learning(self):
        self.click_element(MainPageLocators.SERVICE_BIM_LEARNING)
    
    def click_service_bim_projecting(self):
        self.click_element(MainPageLocators.SERVICE_BIM_PROJECTING)
    
    def click_service_smeta_programs(self):
        self.click_element(MainPageLocators.SERVICE_SMETA_PROGRAMS)
    
    def click_service_project_programs(self):
        self.click_element(MainPageLocators.SERVICE_PROJECT_PROGRAMS)
    
    def click_service_advokat(self):
        self.click_element(MainPageLocators.SERVICE_ADVOKAT)
    
    def click_service_distant_learning(self):
        self.click_element(MainPageLocators.SERVICE_DISTANT_LEARNING)
    
    def click_service_smeta_courses(self):
        self.click_element(MainPageLocators.SERVICE_SMETA_COURSES)