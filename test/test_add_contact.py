# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range (random.randrange(maxlen))])

def random_digits(prefix, maxlen):
    year = string.digits
    return prefix +"".join([random.choice(year) for i in range (random.randrange(maxlen))])

testdata = [Contact(firstname="", lastname="", nickname="", address="", company="", home="", mobile="", work="", fax="",
                    email="", email2="", email3="", homepage="", address2="", phone2="", notes="", byear="")] + [
    Contact(firstname=random_string("firstname", 10), lastname=random_string("lastname", 20), nickname=random_string("nickname", 20),
            address=random_string("address", 20),
            email2=random_string("email2", 10), email3=random_string("email3", 20), homepage=random_string("homepage", 20),
            notes=random_string("notes", 10), byear=random_digits("y", 4))
    for i in range (5)
    ]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    app.open_home_page()
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)