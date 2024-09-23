import os
import time


def test_script_1(browser, page):
    page.click_button_contacts()  # в раздел "Контакты"
    page.click_logo_tenzor()  # Найти баннер Тензор, кликнуть по нему
    assert page.get_current_url() == "https://tensor.ru/"  # Перейти на https://tensor.ru/
    assert page.get_block_sila_v_lydiah()  # Проверить, что есть блок "Сила в людях"
    page.click_button_about()  # Перейдите в этом блоке в "Подробнее"
    assert page.get_current_url() == "https://tensor.ru/about"  # убедитесь, что открывается https://tensor.ru/about
    size_photo = {'height': 193, 'width': 272}
    assert len([size for size in page.get_size_img() if
                size == size_photo]) == 4  # проверяем, что у всех фотографий одинаковые высота и ширина


def test_script_2(browser, page):
    page.click_button_contacts()  # в раздел "Контакты"
    assert page.get_my_region() == "Калининградская обл."  # Проверить, что определился ваш регион
    list_partners_kld = page.get_list_partners()
    assert page.get_list_partners()  # есть список партнеров
    page.select_kamchatka_region()  # Изменить регион на Камчатский край
    assert page.get_my_region() == "Камчатский край"  # Проверить, что подставился выбранный регион
    assert page.get_list_partners()
    assert page.get_list_partners() != list_partners_kld  # список партнеров изменился,
    assert "41-kamchatskij-kraj" in page.get_current_url()  # url и
    assert "Камчатский край" in page.get_title_page()  # title содержат информацию выбранного региона


def test_script_3(browser, page):
    page.click_upload_local_versions()  # В Footer'e найти и перейти "Скачать локальные версии"
    page.click_sbis_plugin()  # Выбрать СБИС Плагин
    page.click_sbis_plugin_windows()  # для windows
    page.click_upload_web_uploader_windows()  # Скачать веб-установщик в папку с данным тестом (в папку files)
    time.sleep(3)
    assert "sbisplugin-setup-web.exe" in os.listdir(f"{os.getcwd()}\\files")  # Убедиться, что плагин скачался
    size_kb = round(os.path.getsize(f"{os.getcwd()}\\files\\sbisplugin-setup-web.exe") / 1024, 2)
    size_mb = round(size_kb / 1024, 2)
    assert str(size_mb) == page.get_mb_file()  # Сравнить размер скачанного файла в мегабайтах
