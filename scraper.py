from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from fields import PublicationJournalFields
import os

class ScholarScraper:
    def __init__(self):
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--disable-gpu")
        self.driver = webdriver.Chrome(options=options)

    def scrape_publication_url_by_author(self, author_name):
        self.driver.get('https://scholar.google.com/citations?hl=en&user=UYHadLQAAAAJ')

        more_button = self.driver.find_element(By.ID, 'gsc_bpf_more')
        more_button.click()

        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located((By.CLASS_NAME, 'gs_vis')))

        publications = self.driver.find_elements(By.CLASS_NAME, 'gsc_a_tr')

        urls = []

        for publication in publications:
            url = publication.find_element(By.CLASS_NAME, 'gsc_a_at').get_attribute('href')
            authors = publication.find_element(By.CLASS_NAME, 'gs_gray').text

            if author_name in authors:
                urls.append(url)

        return urls

    def parse_date(self, date):
        if '/' in date:
            date = date.split('/')
            return date[1], date[0]
        else:
            return '', date
       

    def scrape_publication_field_by_url(self, url):
        print("Fetching: " + url)
        self.driver.get(url)

        publication = PublicationJournalFields()

        publication.title = self.driver.find_element(By.ID, 'gsc_oci_title').text

        table = self.driver.find_elements(By.CLASS_NAME, 'gs_scl')

        if table[2].find_element(By.CLASS_NAME, 'gsc_oci_field').text != 'Journal':
            return

        for row in table:
            value = row.find_element(By.CLASS_NAME, 'gsc_oci_value').text
            field = row.find_element(By.CLASS_NAME, 'gsc_oci_field').text

            if field == 'Authors':
                publication.author = value
            elif field == 'Journal':
                publication.journal = value
            elif field == 'Volume':
                publication.volume = value
            elif field == 'Pages':
                publication.pages = value
            elif field == 'Publication date':
                publication.month, publication.year = self.parse_date(value)
            elif field == 'Description':
                publication.description = value

        print("Fetched: " + publication.title)

        return publication

    def get_new_publications_by_author(self, author_name):
        urls = self.scrape_publication_url_by_author(author_name)

        old_urls = []

        if os.path.exists('urls.txt'):
            with open('urls.txt', 'r') as f:
                old_urls = f.readlines()
                old_urls = [url.strip() for url in old_urls]

        new_urls = [url for url in urls if url not in old_urls]

        with open('urls.txt', 'w') as f:
            for url in urls:
                f.write(url + '\n')

        publications = []

        for url in new_urls:
            publication = self.scrape_publication_field_by_url(url)
            if publication:
                yield publication

        return publications

    def close(self):
        self.driver.quit()

