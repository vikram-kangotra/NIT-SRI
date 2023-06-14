from selenium.webdriver.common.by import By

class PublicationJournalFields:
    def __init__(self):
        self.fields = {
            "ContentPlaceHolder1_ddl_Jounrals_Month": "",
            "ContentPlaceHolder1_ddl_Jounrals_Year": "",
            "ContentPlaceHolder1_txtJourAuthor": "",
            "ContentPlaceHolder1_txtJourTitle": "",
            "ContentPlaceHolder1_txtJourVolume": "",
            "ContentPlaceHolder1_txtJourPN": "",
            "ContentPlaceHolder1_txtJourDOI": "",
            "ContentPlaceHolder1_txtJourFactor": "",
            "ContentPlaceHolder1_ddlJourType": "",
            "ContentPlaceHolder1_TextBox_PubJournals": "",
        }

    def send_keys(self, driver):
        for element_id, value in self.fields.items():
            self.enter_input(driver, element_id, value)

    def enter_input(self, driver, element_id, value):
        input_field = driver.find_element(By.ID, element_id)
        input_field.clear()
        input_field.send_keys(value if value is not None else "")

    @property
    def month(self):
        return self.fields["ContentPlaceHolder1_ddl_Jounrals_Month"]

    @month.setter
    def month(self, value):
        self.fields["ContentPlaceHolder1_ddl_Jounrals_Month"] = value

    @property
    def year(self):
        return self.fields["ContentPlaceHolder1_ddl_Jounrals_Year"]

    @year.setter
    def year(self, value):
        self.fields["ContentPlaceHolder1_ddl_Jounrals_Year"] = value

    @property
    def author(self):
        return self.fields["ContentPlaceHolder1_txtJourAuthor"]

    @author.setter
    def author(self, value):
        self.fields["ContentPlaceHolder1_txtJourAuthor"] = value

    @property
    def title(self):
        return self.fields["ContentPlaceHolder1_txtJourTitle"]

    @title.setter
    def title(self, value):
        self.fields["ContentPlaceHolder1_txtJourTitle"] = value

    @property
    def volume(self):
        return self.fields["ContentPlaceHolder1_txtJourVolume"]

    @volume.setter
    def volume(self, value):
        self.fields["ContentPlaceHolder1_txtJourVolume"] = value

    @property
    def page_number(self):
        return self.fields["ContentPlaceHolder1_txtJourPN"]

    @page_number.setter
    def page_number(self, value):
        self.fields["ContentPlaceHolder1_txtJourPN"] = value

    @property
    def doi(self):
        return self.fields["ContentPlaceHolder1_txtJourDOI"]

    @doi.setter
    def doi(self, value):
        self.fields["ContentPlaceHolder1_txtJourDOI"] = value

    @property
    def impact_factor(self):
        return self.fields["ContentPlaceHolder1_txtJourFactor"]

    @impact_factor.setter
    def impact_factor(self, value):
        self.fields["ContentPlaceHolder1_txtJourFactor"] = value

    @property
    def journal_type(self):
        return self.fields["ContentPlaceHolder1_ddlJourType"]

    @journal_type.setter
    def journal_type(self, value):
        self.fields["ContentPlaceHolder1_ddlJourType"] = value

    @property
    def journal_name(self):
        return self.fields["ContentPlaceHolder1_TextBox_PubJournals"]

    @journal_name.setter
    def journal_name(self, value):
        self.fields["ContentPlaceHolder1_TextBox_PubJournals"] = value
