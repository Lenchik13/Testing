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
    app.contact.edit_contact()
