from selenium.webdriver.common.by import By

from pages.base_page import BasePage


def test_script_1(browser):
    page = BasePage(browser=browser)
    page.open()  # Перейти на https://sbis.ru/
    page.click_button_contacts()  # в раздел "Контакты"
    page.click_logo_tenzor()  # Найти баннер Тензор, кликнуть по нему
    assert page.get_current_url() == "https://tensor.ru/"  # Перейти на https://tensor.ru/
    assert page.find(
        (By.XPATH, '//*[@id="container"]/div[1]/div/div[5]/div/div/div[1]'))  # Проверить, что есть блок "Сила в людях"
    page.click_button_about()  # Перейдите в этом блоке в "Подробнее"
    assert page.get_current_url() == "https://tensor.ru/about"  # убедитесь, что открывается https://tensor.ru/about
    size_photo = {'height': 193, 'width': 272}
    assert len([size for size in page.get_size_img() if
                size == size_photo]) == 4  # проверяем, что у всех фотографий одинаковые высота и ширина


def test_script_2(browser):
    page = BasePage(browser=browser)
    page.open()  # Перейти на https://sbis.ru/
    page.click_button_contacts()  # в раздел "Контакты"
    assert page.get_my_region() == "Калининградская обл."  # Проверить, что определился ваш регион
    list_partners_kld = page.get_list_partners()
    assert page.get_list_partners() != []  # есть список партнеров
    page.select_kamchatka_region()  # Изменить регион на Камчатский край
    assert page.get_my_region() == "Камчатский край"  # Проверить, что подставился выбранный регион
    assert page.get_list_partners() != []
    assert page.get_list_partners() != list_partners_kld  # список партнеров изменился,
    assert "41-kamchatskij-kraj" in page.get_current_url()  # url и
    assert "Камчатский край" in page.get_title_page()  # title содержат информацию выбранного региона
