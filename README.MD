# Автотесты для сайта ООО МКП "Атлон"

Набор автотестов для регрессионного тестирования основных страниц сайта ooo-atlon.ru. Тесты разработаны с использованием Selenium WebDriver, Pytest и Page Object Model (POM).

## 📁 Структура проекта

Atlon_Web-site/
conftest.py # Фикстуры Pytest (настройка драйвера)
data/
    urls.py # URL тестируемых страниц
locators/
    locators.py # Локаторы элементов страниц
pages/
    base_page.py # Базовый класс страницы
    home_page.py # Класс главной страницы
    renga_page.py # Класс страницы Renga
tests/
    test_home_page.py # Тесты главной страницы
    test_urls_check.py # Тесты переходов по услугам
    test_renga_page.py # Тесты страницы Renga

## 🎯 Тестируемые страницы

### Основные страницы
- **Главная страница** (`https://ooo-atlon.ru/`)
- **Renga. Поставка и сопровождение** (`https://ooo-atlon.ru/katalog1/renga_postavka_i_soprovozhdenie/`)
- **Обучение работе с BIM** (`https://ooo-atlon.ru/katalog1/obuchenie_rabote_s_bim/`)
- **BIM-проектирование. Сметы по BIM** (`https://ooo-atlon.ru/katalog1/bim-proektirovanie_smety_po_bim/`)
- **Программы для сметно-строительного комплекса** (`https://ooo-atlon.ru/katalog1/programs/`)
- **Программы для проектно-изыскательных работ** (`https://ooo-atlon.ru/katalog1/programmy_dlya_proektno-izyskatel_nyh_rabot/`)
- **Адвокат в кармане** (`https://ooo-atlon.ru/katalog1/advokat_v_karmane1/`)
- **Образовательные услуги дистанционно** (`https://ooo-atlon.ru/katalog1/obrazovatel_nye_uslugi_distancionno/`)
- **Обучение сметному делу** (`https://ooo-atlon.ru/katalog1/kursy_smetchikov/`)

### Дополнительные страницы
- **Форма обратной связи** (`https://ooo-atlon.ru/forma_zayavki/`)
- **Каталог услуг** (`https://ooo-atlon.ru/katalog1/`)
- **Новости** (`https://ooo-atlon.ru/allnews/`)
- **О компании** (`https://ooo-atlon.ru/o_kompanii1/`)
- **Контакты** (`https://ooo-atlon.ru/contacts/`)
- **Вакансии** (`https://ooo-atlon.ru/vakansii/`)

## Набор тестов

### `test_home_page.py` - Тесты главной страницы
- **Класс:** `TestHomePageElements` - Проверка отображения элементов на главной странице
- **Класс:** `TestHomePageContent` - Проверка содержания элементов
- **Класс:** `TestHomePageFunctionality` - Проверка функциональности элементов

### `test_urls_check.py` - Тесты переходов по услугам
- **Класс:** `TestServicesNavigation` - Параметризованная проверка корректности переходов в блоке "Услуги"

### `test_renga_page.py` - Тесты страницы Renga
- **Класс:** `TestRengaPageNavigation` - Проверка переходов со страницы Renga на дочерние страницы


## 🚀 Установка и запуск

### Установка зависимостей
pip install -r requirements.txt

### Запуск всех тестов
pytest tests/test_home_page.py -v

### Запуск тестов главной страницы
pytest tests/test_home_page.py -v

### Запуск тестов переходов по услугам:
pytest tests/test_urls_check.py -v

### Запуск тестов страницы Renga:
pytest tests/test_renga_page.py -v

