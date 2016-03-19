# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
   app.login(username="admin", password="secret")
   app.create_contact(Contact(firstname="Elena", lastname="Sycheva", nickname="Lenchik",
                            address="Moscow, Mira str,, 1/2", company="Test Company", home="+7(499)7654321",
                            mobile="+7(999)8765432", work="+7(987)6543210", fax="+7(123)456789", email="elena@mail.ru",
                            email2="elena1111@mail.ru", email3="elena2222@gmail.com", homepage="www.homepage.ru/elena",
                            byear="1978", address2="Moscow, Andropova pr., 27/3", phone2="+7(495)7777777",
                            notes="Hello!", bday="20", bmonth="6"))
   app.logout()