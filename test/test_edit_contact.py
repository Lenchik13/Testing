from model.contact import Contact
import random

def test_edit_contact(app, db, check_ui):
    app.open_home_page()
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Contact", lastname="", nickname="",
                              address="", company="", home="",
                              mobile="", work="", fax="", email="",
                              email2="", email3="", homepage="",
                              byear="", address2="", phone2="",
                              notes="", bday="20", bmonth="6"))
    old_contacts = db.get_contact_list()
    rcontact = random.choice(old_contacts)
    contact = Contact(lastname="lname", firstname="fname", address="address")
    contact.id = rcontact.id
    app.contact.modify_contact_by_id(contact)
    app.open_home_page()
    assert len(old_contacts) == app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts.remove(rcontact)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)



