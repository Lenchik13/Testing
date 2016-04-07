from model.contact import Contact

class ContactHelper:

    def __init__(self, app):
        self.app = app


    def create(self, contact):
        wd = self.app.wd
        self.add_new()
        # fill contact's form
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.home)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobile)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.work)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(contact.fax)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contact.email2)
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(contact.email3)
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(contact.homepage)
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[12]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[%s]" % contact.bday).click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[11]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[%s]" % contact.bmonth).click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.byear)
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contact.address2)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contact.phone2)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contact.notes)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.contact_cache = None

    def add_new(self):
        wd = self.app.wd
        # open add new contact
        wd.find_element_by_link_text("add new").click()

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        #select first contact
        wd.find_elements_by_name("selected[]")[index].click()
        #submit delision
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

#    def edit_contact_by_index(self, index):
#        wd = self.app.wd
#        wd.find_elements_by_name("selected[]")[index].click()
#        wd.find_elements_by_xpath("//img[@src='icons/pencil.png']")[index].click()
#        wd.find_element_by_name("firstname").click()
#        wd.find_element_by_name("firstname").clear()
#        wd.find_element_by_name("firstname").send_keys("Firstname")
#        wd.find_element_by_name("address").click()
#        wd.find_element_by_name("address").clear()
#        wd.find_element_by_name("address").send_keys("Moscow, Mira str,, 20")
#        wd.find_element_by_name("home").click()
#        wd.find_element_by_name("home").clear()
#        wd.find_element_by_name("home").send_keys("+7(499)9999999")
#        if not wd.find_element_by_xpath("//div[@id='content']/form[1]/select[1]//option[15]").is_selected():
#            wd.find_element_by_xpath("//div[@id='content']/form[1]/select[1]//option[15]").click()
#        if not wd.find_element_by_xpath("//div[@id='content']/form[1]/select[2]//option[11]").is_selected():
#            wd.find_element_by_xpath("//div[@id='content']/form[1]/select[2]//option[11]").click()
#        wd.find_element_by_name("update").click()
#        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                lastname = element.find_element_by_xpath('./td[2]').text
                firstname = element.find_element_by_xpath('./td[3]').text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.contact_cache.append(Contact(lastname=lastname, firstname=firstname, id=id))
        return list(self.contact_cache)

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()
        wd.find_elements_by_xpath("//img[@src='icons/pencil.png']")[index].click()
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("address", contact.address)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
             wd.find_element_by_name(field_name).click()
             wd.find_element_by_name(field_name).clear()
             wd.find_element_by_name(field_name).send_keys(text)



