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
    
    def find_element(self, locator, timeout=10):
        """Найти элемент на странице"""
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.visibility_of_element_located(locator))
    
    def find_elements(self, locator, timeout=10):
        """Найти несколько элементов на странице"""
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.presence_of_all_elements_located(locator))
    
    def is_element_visible(self, locator, timeout=5):
        """Проверить, виден ли элемент"""
        try:
            wait = WebDriverWait(self.driver, timeout)
            element = wait.until(EC.visibility_of_element_located(locator))
            return element.is_displayed()
        except:
            return False
    
    def get_element_text(self, locator):
        """Получить текст элемента"""
        element = self.find_element(locator)
        return element.text
    
    def click_element(self, locator):
        """Кликнуть по элементу с прокруткой"""
        element = self.find_element(locator)
        
        # Прокручиваем к элементу
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        
        # Небольшая задержка для прокрутки
        import time
        time.sleep(0.5)
        
        # Используем JavaScript для клика
        self.driver.execute_script("arguments[0].click();", element)
    
    def get_current_url(self):
        """Получить текущий URL"""
        return self.driver.current_url
    
    def wait_for_url(self, expected_url, timeout=10):
        """Ожидать загрузки конкретного URL"""
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.url_to_be(expected_url))
    
    def take_screenshot(self, name="screenshot"):
        """Сделать скриншот"""
        self.driver.save_screenshot(f"{name}.png")
    
    def wait_for_page_load(self):
        """Ожидать загрузки страницы"""
        self.wait.until(
            lambda driver: driver.execute_script('return document.readyState') == 'complete'
        )
    
    def input_text(self, locator, text):
        """Ввести текст в поле"""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)