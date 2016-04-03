from model.contact import Contact

def test_edit_contact(app):
    app.open_home_page()
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Contact", lastname="", nickname="",
                              address="", company="", home="",
                              mobile="", work="", fax="", email="",
                              email2="", email3="", homepage="",
                              byear="", address2="", phone2="",
                              notes="", bday="20", bmonth="6"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Contact")
    contact.id = old_contacts[0].id
    app.contact.edit_contact()
    app.open_home_page()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
