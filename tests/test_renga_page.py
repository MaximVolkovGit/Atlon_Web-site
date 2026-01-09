import pytest
from pages.renga_page import RengaPage
from data.urls import BasicUrls, RengaURLS

class TestRengaPageNavigation:
    """Тесты для проверки переходов со страницы Renga"""
    
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        """Открываем страницу Renga перед каждым тестом"""
        self.renga_page = RengaPage(driver)
        self.renga_page.open()
    
    def test_contact_button_navigation(self, driver):
        """Проверка перехода на страницу контактов по кнопке консультации"""
        # Проверяем, что кнопка видна
        assert self.renga_page.is_contact_button_visible(), "Кнопка консультации не видна"
        
        # Кликаем по кнопке
        self.renga_page.click_contact_button()
        
        # Проверяем URL
        current_url = driver.current_url
        expected_url = BasicUrls.CONTACT_FORM
        assert current_url == expected_url, f"Ожидался URL: {expected_url}, получен: {current_url}"
    
    def test_standart_link_navigation(self, driver):
        """Проверка перехода на страницу Renga Standard"""
        # Проверяем, что ссылка видна
        assert self.renga_page.is_standart_link_visible(), "Ссылка на Renga Standard не видна"
        
        # Кликаем по ссылке
        self.renga_page.click_standart_link()
        
        # Проверяем URL
        current_url = driver.current_url
        expected_url = RengaURLS.RENGA_STANDART_URL
        assert current_url == expected_url, f"Ожидался URL: {expected_url}, получен: {current_url}"
        
        # Проверяем наличие ключевого текста на странице
        assert "Renga Standard" in driver.page_source, "Текст 'Renga Standard' не найден на странице"
    
    def test_professional_link_navigation(self, driver):
        """Проверка перехода на страницу Renga Professional"""
        # Проверяем, что ссылка видна
        assert self.renga_page.is_professional_link_visible(), "Ссылка на Renga Professional не видна"
        
        # Кликаем по ссылке
        self.renga_page.click_professional_link()
        
        # Проверяем URL
        current_url = driver.current_url
        expected_url = RengaURLS.RENGA_PROFESSIONAL_URL
        assert current_url == expected_url, f"Ожидался URL: {expected_url}, получен: {current_url}"
        
        # Проверяем наличие ключевого текста на странице
        assert "Renga Professional" in driver.page_source, "Текст 'Renga Professional' не найден на странице"


# class TestRengaPageParametrized:
#     """Параметризованные тесты для проверки переходов со страницы Renga"""
    
#     @pytest.fixture(autouse=True)
#     def setup(self, driver):
#         """Открываем страницу Renga перед каждым тестом"""
#         self.renga_page = RengaPage(driver)
#         self.renga_page.open()
    
#     @pytest.mark.parametrize("element_type,expected_url,expected_text", [
#         ("contact_button", BasicUrls.CONTACT_FORM, None),
#         ("standart_link", RengaURLS.RENGA_STANDART_URL, "Renga"),
#         ("professional_link", RengaURLS.RENGA_PROFESSIONAL_URL, "Renga"),
#     ])
#     def test_navigation_parametrized(self, driver, element_type, expected_url, expected_text):
#         """Параметризованный тест проверки переходов"""
        
#         # Словарь соответствия типов элементов и методов
#         element_methods = {
#             "contact_button": (self.renga_page.is_contact_button_visible, self.renga_page.click_contact_button),
#             "standart_link": (self.renga_page.is_standart_link_visible, self.renga_page.click_standart_link),
#             "professional_link": (self.renga_page.is_professional_link_visible, self.renga_page.click_professional_link),
#         }
        
#         # Получаем методы проверки и клика
#         check_method, click_method = element_methods[element_type]
        
#         # Проверяем видимость элемента
#         assert check_method(), f"Элемент {element_type} не виден"
        
#         # Кликаем по элементу
#         click_method()
        
#         # Проверяем URL
#         current_url = driver.current_url
#         assert current_url == expected_url, f"Ожидался URL: {expected_url}, получен: {current_url}"
        
#         # Проверяем текст на странице, если он указан
#         if expected_text:
#             assert expected_text in driver.page_source, f"Текст '{expected_text}' не найден на странице"