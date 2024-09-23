import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:

    def __init__(self, browser: webdriver.Chrome):
        self.browser = browser

    def find(self, args):
        return self.browser.find_element(*args)

    def open(self):
        self.browser.get("https://sbis.ru/")

    def wait_element_to_be_clickable(self, args):
        wait = WebDriverWait(self.browser, 10)
        element = wait.until(
            ec.element_to_be_clickable(args))
        return element

    def click_button_contacts(self):
        element = self.find(
            (By.CSS_SELECTOR, 'div.sbisru-Header-ContactsMenu.js-ContactsMenu'))
        element.click()
        new_element = self.find(
            (By.CSS_SELECTOR, ".sbisru-Header-ContactsMenu__items a.sbisru-link span")
        )
        new_element.click()

    def click_button_about(self):
        element = self.find(
            (By.CSS_SELECTOR, '.tensor_ru-Index__block4-content a.tensor_ru-Index__link'))
        self.browser.execute_script("arguments[0].click();", element)

    def click_logo_tenzor(self):
        element = self.find(
            (By.CSS_SELECTOR, 'a[title="tensor.ru"]'))
        element.click()
        self.switch_window()

    def get_current_url(self):
        return self.browser.current_url

    def switch_window(self):
        new_window = self.browser.window_handles[1]
        self.browser.switch_to.window(new_window)

    def get_size_img(self):
        imgs = self.browser.find_elements(
            By.CSS_SELECTOR,
            '.s-Grid-container .tensor_ru-About__block3-image-wrapper img'
        )
        img_sizes = [img.size for img in imgs]
        return img_sizes

    def get_my_region(self):
        element = self.find((By.CLASS_NAME, "sbis_ru-Region-Chooser__text"))
        return element.text

    def get_list_partners(self):
        block = self.find((By.CSS_SELECTOR, 'div[data-qa="items-container"]'))
        partners = block.find_elements(By.CLASS_NAME, "sbisru-Contacts-List__item")
        return partners

    def select_kamchatka_region(self):
        self.find((By.CLASS_NAME, "sbis_ru-Region-Chooser__text")).click()
        element = self.find((By.CSS_SELECTOR, "li span[title='Камчатский край']"))
        self.browser.execute_script("arguments[0].click();", element)
        time.sleep(1)

    def get_title_page(self):
        return self.browser.title

    def click_upload_local_versions(self):
        element = self.find(
            (By.CSS_SELECTOR, 'li a[href="/download"]'))
        element.click()

    def click_sbis_plugin(self):
        element = self.find(
            (By.CSS_SELECTOR,
             '.controls-TabButton[data-id="plugin"]')
        )
        element.click()

    def click_sbis_plugin_windows(self):
        element = self.find(
            (By.XPATH,
             "//span[text()='Windows']")
        )
        element.click()

    def click_upload_web_uploader_windows(self):
        element = self.find(
            (By.CSS_SELECTOR,
             "div a[href='https://update.sbis.ru/Sbis3Plugin/master/win32/sbisplugin-setup-web.exe']")
        )
        element.click()

    def get_mb_file(self):
        element = self.find(
            (By.CSS_SELECTOR,
             "div a[href='https://update.sbis.ru/Sbis3Plugin/master/win32/sbisplugin-setup-web.exe']")
        )
        mb = element.text.strip("Скачать ( Exe МБ )")
        return mb

    def get_block_sila_v_lydiah(self):
        block = self.find(
            (By.CSS_SELECTOR,
             ".tensor_ru-Index__block4-content")
        )
        return block
