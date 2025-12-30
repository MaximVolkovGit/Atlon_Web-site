from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, url=None):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(driver, 10)
    
    def open(self):
        """Открыть страницу"""
        if self.url:
            self.driver.get(self.url)
        return self
    
    def find_element(self, locator):
        """Найти элемент на странице"""
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    def find_elements(self, locator):
        """Найти несколько элементов на странице"""
        return self.wait.until(EC.presence_of_all_elements_located(locator))
    
    def is_element_visible(self, locator):
        """Проверить, виден ли элемент"""
        try:
            element = self.find_element(locator)
            return element.is_displayed()
        except:
            return False
    
    def get_element_text(self, locator):
        """Получить текст элемента"""
        element = self.find_element(locator)
        return element.text
    
    def click_element(self, locator):
        """Кликнуть по элементу"""
        element = self.find_element(locator)
        element.click()