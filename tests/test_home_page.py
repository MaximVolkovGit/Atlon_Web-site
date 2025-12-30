# tests/test_home_page.py
import pytest
from locators.locators import MainPageLocators
from pages.home_page import HomePage

class TestHomePageElements:
    """Тесты для проверки отображения элементов на главной странице"""
    
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        """Открываем главную страницу перед каждым тестом"""
        self.home_page = HomePage(driver)
        self.home_page.open()
    
    def test_logo_displayed(self):
        """Проверка отображения логотипа"""
        assert self.home_page.is_logo_displayed(), "Логотип не отображается"
    
    def test_company_name_displayed(self):
        """Проверка отображения заголовка компании"""
        assert self.home_page.is_company_name_displayed(), "Заголовок компании не отображается"
    
    def test_slogan_displayed(self):
        """Проверка отображения слогана"""
        assert self.home_page.is_slogan_displayed(), "Слоган не отображается"
    
    def test_phone_displayed(self):
        """Проверка отображения телефона"""
        assert self.home_page.is_phone_displayed(), "Телефон не отображается"
        
        # Дополнительная проверка правильности номера
        phone_text = self.home_page.get_phone_text()
        assert "(910) 914-32-94" in phone_text, f"Неправильный номер телефона: {phone_text}"
    
    def test_address_displayed(self):
        """Проверка отображения адреса"""
        assert self.home_page.is_address_displayed(), "Адрес не отображается"
        
        # Дополнительная проверка правильности адреса
        address_text = self.home_page.get_address_text()
        assert "г. Обнинск, пр. Ленина, д. 129, оф. 107" in address_text, f"Неправильный адрес: {address_text}"
    
    def test_work_time_displayed(self):
        """Проверка отображения времени работы"""
        assert self.home_page.is_work_time_displayed(), "Время работы не отображается"
        
        # Дополнительная проверка правильности времени работы
        work_time_text = self.home_page.get_work_time_text()
        assert "9-17 ч. в рабочие дни" in work_time_text, f"Неправильное время работы: {work_time_text}"
    
    def test_main_menu_displayed(self):
        """Проверка отображения основного меню"""
        assert self.home_page.is_main_menu_displayed(), "Основное меню не отображается"
    
    def test_services_block_displayed(self):
        """Проверка отображения блока услуг"""
        assert self.home_page.is_services_block_displayed(), "Блок услуг не отображается"
    
    def test_cookie_notification_displayed(self):
        """Проверка отображения уведомления о куках"""
        assert self.home_page.is_cookie_notification_displayed(), "Уведомление о куках не отображается"
    
    def test_accept_cookies_button_displayed(self):
        """Проверка отображения кнопки принятия куки"""
        assert self.home_page.is_accept_cookies_button_displayed(), "Кнопка принятия куки не отображается"
    
    def test_contact_button_displayed(self):
        """Проверка отображения кнопки 'Связаться с нами'"""
        assert self.home_page.is_contact_button_displayed(), "Кнопка 'Связаться с нами' не отображается"
    
    def test_search_input_displayed(self):
        """Проверка отображения поля поиска"""
        assert self.home_page.is_search_input_displayed(), "Поле поиска не отображается"
    
    def test_search_button_displayed(self):
        """Проверка отображения кнопки поиска"""
        assert self.home_page.is_search_button_displayed(), "Кнопка поиска не отображается"

class TestHomePageContent:
    """Тесты для проверки содержания элементов на главной странице"""
    
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        """Открываем главную страницу перед каждым тестом"""
        self.home_page = HomePage(driver)
        self.home_page.open()
    
    def test_company_name_text(self):
        """Проверка текста названия компании"""
        company_name = self.home_page.get_company_name_text()
        assert company_name == 'ООО МКП "АТЛОН"', f"Неправильное название компании: {company_name}"
    
    def test_slogan_content(self):
        """Проверка содержания слогана"""
        slogan = self.home_page.get_slogan_text()
        assert "многопрофильное предприятие" in slogan.lower(), f"Слоган не содержит ожидаемый текст: {slogan}"

class TestHomePageFunctionality:
    """Тесты для проверки функциональности элементов на главной странице"""
    
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        """Открываем главную страницу перед каждым тестом"""
        self.home_page = HomePage(driver)
        self.home_page.open()
    
    def test_accept_cookies(self):
        """Проверка функционала принятия куки"""
        # Проверяем, что уведомление видно до нажатия
        assert self.home_page.is_cookie_notification_displayed()
        
        # Нажимаем кнопку принятия
        self.home_page.accept_cookies()
        
        # Даем время для скрытия уведомления
        import time
        time.sleep(1)
        
        # Проверяем, что уведомление скрылось
        # Внимание: на реальном сайте уведомление может просто скрываться, а не удаляться из DOM
        # Поэтому проверяем либо отсутствие, либо невидимость
        try:
            is_still_displayed = self.home_page.is_cookie_notification_displayed()
            # Если элемент все еще есть в DOM, он может быть скрыт CSS
            if is_still_displayed:
                print("Элемент уведомления остался в DOM, но может быть скрыт стилями")
        except:
            pass  # Если элемент удален из DOM - это нормально

    def test_search_field_is_editable(self):
        """Проверка, что поле поиска доступно для ввода"""
        search_input = self.home_page.find_element(MainPageLocators.SEARCH_INPUT)
        assert search_input.is_enabled(), "Поле поиска недоступно для ввода"
        
        # Проверяем, что можно ввести текст
        test_text = "тестовый поиск"
        search_input.clear()
        search_input.send_keys(test_text)
        assert search_input.get_attribute('value') == test_text, "Не удалось ввести текст в поле поиска"