from model.contact import Contact
from random import randrange

def test_delete_some_contact(app):
    app.open_home_page()
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Contact", lastname="", nickname="",
                              address="", company="", home="",
                              mobile="", work="", fax="", email="",
                              email2="", email3="", homepage="",
                              byear="", address2="", phone2="",
                              notes="", bday="20", bmonth="6"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    app.open_home_page()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts
