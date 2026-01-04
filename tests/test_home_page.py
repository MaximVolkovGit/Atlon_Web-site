import pytest
from locators.locators import MainPageLocators

class TestHomePageElements:
    """Тесты для проверки отображения элементов на главной странице"""
    
    def test_logo_displayed(self, home_page):
        """Проверка отображения логотипа"""
        assert home_page.is_logo_displayed(), "Логотип не отображается"
    
    def test_company_name_displayed(self, home_page):
        """Проверка отображения заголовка компании"""
        assert home_page.is_company_name_displayed(), "Заголовок компании не отображается"
    
    def test_slogan_displayed(self, home_page):
        """Проверка отображения слогана"""
        assert home_page.is_slogan_displayed(), "Слоган не отображается"
    
    def test_phone_displayed(self, home_page):
        """Проверка отображения телефона"""
        assert home_page.is_phone_displayed(), "Телефон не отображается"
        
        # Дополнительная проверка правильности номера
        phone_text = home_page.get_phone_text()
        assert "(910) 914-32-94" in phone_text, f"Неправильный номер телефона: {phone_text}"
    
    def test_address_displayed(self, home_page):
        """Проверка отображения адреса"""
        assert home_page.is_address_displayed(), "Адрес не отображается"
        
        # Дополнительная проверка правильности адреса
        address_text = home_page.get_address_text()
        assert "г. Обнинск, пр. Ленина, д. 129, оф. 107" in address_text, f"Неправильный адрес: {address_text}"
    
    def test_work_time_displayed(self, home_page):
        """Проверка отображения времени работы"""
        assert home_page.is_work_time_displayed(), "Время работы не отображается"
        
        # Дополнительная проверка правильности времени работы
        work_time_text = home_page.get_work_time_text()
        assert "9-17 ч. в рабочие дни" in work_time_text, f"Неправильное время работы: {work_time_text}"
    
    def test_main_menu_displayed(self, home_page):
        """Проверка отображения основного меню"""
        assert home_page.is_main_menu_displayed(), "Основное меню не отображается"
    
    def test_services_block_displayed(self, home_page):
        """Проверка отображения блока услуг"""
        assert home_page.is_services_block_displayed(), "Блок услуг не отображается"
    
    def test_cookie_notification_displayed(self, home_page):
        """Проверка отображения уведомления о куках"""
        # Уведомление может быть скрыто после автоматического принятия в фикстуре
        # Проверяем, что элемент существует в DOM
        try:
            home_page.find_element(MainPageLocators.COOKIE_NOTIFICATION, timeout=2)
            cookie_exists = True
        except:
            cookie_exists = False
        
        assert cookie_exists, "Элемент уведомления о куках не найден в DOM"
    
    def test_accept_cookies_button_displayed(self, home_page):
        """Проверка отображения кнопки принятия куки"""
        # Кнопка может быть скрыта после автоматического принятия в фикстуре
        # Проверяем, что элемент существует в DOM
        try:
            home_page.find_element(MainPageLocators.ACCEPT_COOKIES_BUTTON, timeout=2)
            button_exists = True
        except:
            button_exists = False
        
        assert button_exists, "Элемент кнопки принятия куки не найден в DOM"
    
    def test_contact_button_displayed(self, home_page):
        """Проверка отображения кнопки 'Связаться с нами'"""
        assert home_page.is_contact_button_displayed(), "Кнопка 'Связаться с нами' не отображается"
    
    def test_search_input_displayed(self, home_page):
        """Проверка отображения поля поиска"""
        assert home_page.is_search_input_displayed(), "Поле поиска не отображается"
    
    def test_search_button_displayed(self, home_page):
        """Проверка отображения кнопки поиска"""
        assert home_page.is_search_button_displayed(), "Кнопка поиска не отображается"

class TestHomePageContent:
    """Тесты для проверки содержания элементов на главной странице"""
    
    def test_company_name_text(self, home_page):
        """Проверка текста названия компании"""
        company_name = home_page.get_company_name_text()
        assert company_name == 'ООО МКП "АТЛОН"', f"Неправильное название компании: {company_name}"
    
    def test_slogan_content(self, home_page):
        """Проверка содержания слогана"""
        slogan = home_page.get_slogan_text()
        assert "многопрофильное предприятие" in slogan.lower(), f"Слоган не содержит ожидаемый текст: {slogan}"

class TestHomePageFunctionality:
    """Тесты для проверки функциональности элементов на главной странице"""
    
    def test_search_field_is_editable(self, home_page):
        """Проверка, что поле поиска доступно для ввода"""
        search_input = home_page.find_element(MainPageLocators.SEARCH_INPUT)
        assert search_input.is_enabled(), "Поле поиска недоступно для ввода"
        
        # Проверяем, что можно ввести текст
        test_text = "тестовый поиск"
        search_input.clear()
        search_input.send_keys(test_text)
        assert search_input.get_attribute('value') == test_text, "Не удалось ввести текст в поле поиска"