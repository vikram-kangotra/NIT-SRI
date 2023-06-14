from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fields import PublicationJournalFields
from scraper import ScholarScraper
import time

class NITSRILogin:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get("https://www.nitsri.ac.in/Department/DeptWiseLogin.aspx?nDeptID=cs")
        self.enter_input("ContentPlaceHolder1_TextBox_LoginID", self.username)
        self.enter_input("ContentPlaceHolder1_TextBox_Password", self.password)
        self.enter_captcha()
        self.click_button("ContentPlaceHolder1_Button_Login")
        WebDriverWait(self.driver, 30).until(EC.url_contains("https://www.nitsri.ac.in/Department/CPWelcomeDept.aspx"))

    def enter_input(self, element_id, value):
        input_field = self.driver.find_element(By.ID, element_id)
        input_field.send_keys(value)

    def enter_captcha(self):
        captcha_input = input("Enter captcha: ")
        self.enter_input("ContentPlaceHolder1_TextBox_Captcha", captcha_input)

    def click_button(self, element_id):
        button = self.driver.find_element(By.ID, element_id)
        button.click()

    def open_page(self, url):
        self.driver.get(url)

    def fill_publication_journal_form(self):
        self.open_page("https://www.nitsri.ac.in/Department/CPDeptProfile.aspx")

        self.click_button("ContentPlaceHolder1_LinkButton_PublicationJounral")

        scraper = ScholarScraper()
        publications = scraper.get_new_publications_by_author("RK Rout")

        for publication in publications:
            publication.type = "SCOPUS"
            publication.clear(self.driver)
            publication.send_keys(self.driver)
            publication.print()
            submit = input("Submit? (y/n): ")
            if submit == "y":
                self.click_button("ContentPlaceHolder1_Button_PubJournals_Submit")

        scraper.close()

    def close(self):
        time.sleep(50)
        self.driver.quit()


def read_config_file(file_path):
    config_data = {}
    with open(file_path, "r") as file:
        for line in file:
            key, value = line.strip().split("=")
            config_data[key] = value
    return config_data


def main():
    config_data = read_config_file("user.config")

    username = config_data.get("username", "")
    password = config_data.get("password", "")

    nitsri_login = NITSRILogin(username, password)
    nitsri_login.login()
    nitsri_login.fill_publication_journal_form()
    nitsri_login.close()


if __name__ == "__main__":
    main()
