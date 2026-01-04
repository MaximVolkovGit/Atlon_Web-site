import pytest
from data.urls import ServicesCatalogUrls

class TestServicesNavigation:
    """Тесты для проверки переходов по ссылкам в блоке Услуг"""
    
    @pytest.mark.parametrize("service_method,expected_url,expected_text", [
        ("click_service_renga", ServicesCatalogUrls.SERVICE_RENGA, "Renga. Поставка и сопровождение"),
        ("click_service_bim_learning", ServicesCatalogUrls.BIM_COURSES, "Обучение работе с BIM"),
        ("click_service_bim_projecting", ServicesCatalogUrls.BIM_WIZARD, "BIM-проектирование"),
        ("click_service_smeta_programs", ServicesCatalogUrls.SMETA_PROGRAMMS, "Программы для сметно-строительного комплекса"),
        ("click_service_project_programs", ServicesCatalogUrls.PROJECT_PROGRAMMS, "Программы для проектно-изыскательных работ"),
        ("click_service_advokat", ServicesCatalogUrls.ADVOKAT, "Адвокат в кармане"),
        ("click_service_distant_learning", ServicesCatalogUrls.DISTANT_COURSES, "Образовательные услуги дистанционно"),
        ("click_service_smeta_courses", ServicesCatalogUrls.SMETA_COURSES, "Обучение сметному делу"),
    ])
    def test_service_navigation(self, home_page, service_method, expected_url, expected_text):
        """Параметризованный тест для проверки переходов на страницы услуг"""
        
        # Получаем метод по имени и вызываем его
        method = getattr(home_page, service_method)
        method()
        
        # Ожидаем загрузки нужного URL
        home_page.wait_for_url(expected_url)
        
        # Проверяем URL
        current_url = home_page.get_current_url()
        assert current_url == expected_url, f"Ожидался URL: {expected_url}, получен: {current_url}"
        
        # Проверяем наличие текста на странице
        home_page.wait_for_page_load()
        page_source = home_page.driver.page_source
        assert expected_text in page_source, f"Текст '{expected_text}' не найден на странице"