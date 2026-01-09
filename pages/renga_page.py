# pages/renga_page.py
from .base_page import BasePage
from locators.locators import RengaPageLocators
from data.urls import ServicesCatalogUrls, BasicUrls, RengaURLS

class RengaPage(BasePage):
    """Класс для работы со страницей Renga. Поставка и сопровождение"""
    
    def __init__(self, driver):
        super().__init__(driver, ServicesCatalogUrls.SERVICE_RENGA)
    
    def open(self):
        """Открыть страницу Renga"""
        self.driver.get(self.url)
        return self
    
    def click_contact_button(self):
        """Кликнуть по кнопке 'Получить консультацию по покупке программы'"""
        self.click_element(RengaPageLocators.RENGA_CONTACT_BUTTON)
    
    def click_standart_link(self):
        """Кликнуть по ссылке 'Renga Standard'"""
        self.click_element(RengaPageLocators.RENGA_STANDART_LINK)
    
    def click_professional_link(self):
        """Кликнуть по ссылке 'Renga Professional'"""
        self.click_element(RengaPageLocators.RENGA_PROFESSIONAL_LINK)
    
    def is_contact_button_visible(self):
        """Проверить видимость кнопки консультации"""
        return self.is_element_visible(RengaPageLocators.RENGA_CONTACT_BUTTON)
    
    def is_standart_link_visible(self):
        """Проверить видимость ссылки на Renga Standard"""
        return self.is_element_visible(RengaPageLocators.RENGA_STANDART_LINK)
    
    def is_professional_link_visible(self):
        """Проверить видимость ссылки на Renga Professional"""
        return self.is_element_visible(RengaPageLocators.RENGA_PROFESSIONAL_LINK)