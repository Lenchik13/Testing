# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Elena", lastname="Sycheva", nickname="Lenchik",
                              address="Moscow, Mira str,, 1/2", company="Test Company", home="+7(499)7654321",
                              mobile="+7(999)8765432", work="+7(987)6543210", fax="+7(123)456789", email="elena@mail.ru",
                              email2="elena1111@mail.ru", email3="elena2222@gmail.com", homepage="www.homepage.ru/elena",
                              byear="1978", address2="Moscow, Andropova pr., 27/3", phone2="+7(495)7777777",
                              notes="Hello!", bday="20", bmonth="6")
    app.contact.create(contact)
    app.open_home_page()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)