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
        element = self.wait_element_to_be_clickable(
            (By.XPATH, '//*[@id="wasaby-content"]/div/div/div[2]/div[1]/div[1]/div[1]/div[2]/ul/li[2]/div/div[1]'))
        element.click()
        new_element = self.wait_element_to_be_clickable(
            (By.XPATH, '//*[@id="wasaby-content"]/div/div/div[2]/div[1]/div[1]/div[1]/div[2]/ul/li[2]/div/div[2]/a[2]')
        )
        new_element.click()

    def click_button_about(self):
        element = self.wait_element_to_be_clickable(
            (By.XPATH, '//*[@id="container"]/div[1]/div/div[5]/div/div/div[1]/div/p[4]/a'))
        self.browser.execute_script("arguments[0].click();", element)

    def click_logo_tenzor(self):
        element = self.wait_element_to_be_clickable(
            (By.XPATH, '//*[@id="contacts_clients"]/div[1]/div/div/div[2]/div/a'))
        element.click()
        self.switch_window()

    def get_current_url(self):
        return self.browser.current_url

    def switch_window(self):
        new_window = self.browser.window_handles[1]
        self.browser.switch_to.window(new_window)

    def get_size_img(self):
        block = self.find((By.XPATH, '//*[@id="container"]/div[1]/div/div[4]'))
        imgs = block.find_elements(By.CLASS_NAME, 'tensor_ru-About__block3-image')
        img_sizes = [img.size for img in imgs]
        return img_sizes

    def get_my_region(self):
        element = self.find((By.CLASS_NAME, "sbis_ru-Region-Chooser__text"))
        return element.text

    def get_list_partners(self):
        block = self.find((By.XPATH, '//*[@id="contacts_list"]/div/div[2]/div[2]/div/div[2]/div[1]/div[3]'))
        partners = block.find_elements(By.CLASS_NAME, "sbisru-Contacts-List__item")
        return partners

    def select_kamchatka_region(self):
        self.find((By.CLASS_NAME, "sbis_ru-Region-Chooser__text")).click()
        block = self.find((By.XPATH, f'//*[@id="popup"]/div[2]/div/div/div/div/div[2]/div/ul/li[43]/span'))
        block.find_element(By.TAG_NAME, "span").click()
        time.sleep(1)

    def get_title_page(self):
        return self.browser.title

    def click_upload_local_versions(self):
        element = self.wait_element_to_be_clickable(
            (By.XPATH, '//*[@id="container"]/div[2]/div[1]/div[3]/div[3]/ul/li[8]/a'))
        element.click()

    def click_sbis_plugin(self):
        element = self.find(
            (By.XPATH,
             '/html/body/div[1]/div[2]/div[1]/div/div[1]/div/div/div/div[1]/div/div/div/div[3]/div[1]/div[1]/div')
        )
        element.click()

    def click_sbis_plugin_windows(self):
        element = self.find(
            (By.XPATH,
             '/html/body/div[1]/div[2]/div[1]/div/div[1]/div/div/div/div[2]/div/div[1]/div/div/div[1]/div/div[1]/div[1]/div/div/span')
        )
        element.click()

    def click_upload_web_uploader_windows(self):
        element = self.find(
            (By.XPATH,
             '/html/body/div[1]/div[2]/div[1]/div/div[1]/div/div/div/div[2]/div/div[1]/div/div/div[2]/div[1]/div[2]/div[2]/div/a')
        )
        element.click()

    def get_mb_file(self):
        element = self.find(
            (By.XPATH,
             '/html/body/div[1]/div[2]/div[1]/div/div[1]/div/div/div/div[2]/div/div[1]/div/div/div[2]/div[1]/div[2]/div[2]/div/a')
        )
        mb = element.text.strip("Скачать ( Exe МБ )")
        return mb
