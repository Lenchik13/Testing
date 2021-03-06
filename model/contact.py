from sys import maxsize

class Contact:

    def __init__(self, firstname=None, lastname=None, all_phones_from_home_page=None, nickname=None, address=None,
                 company=None, home=None, mobile=None, work=None, fax=None, email=None, email2=None, email3=None,
                 homepage=None, byear=None, address2=None, phone2=None, notes=None, bday=None, bmonth=None, id=None,
                 all_email_from_home_page=None):
        self.firstname = firstname
        self.lastname = lastname
        self.nickname = nickname
        self.address = address
        self.company = company
        self.home = home
        self.mobile = mobile
        self.work = work
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.byear = byear
        self.address2 = address2
        self.phone2 = phone2
        self.notes = notes
        self.bday = bday
        self.bmonth = bmonth
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_email_from_home_page = all_email_from_home_page


    def __repr__(self):
        return "%s:%s:%s:%s:%s:%s:%s" % (self.id, self.lastname, self.firstname, self.address, self.home, self.mobile, self.email)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and (self.lastname is None or other.lastname is None or self.lastname == other.lastname) and (self.firstname is None or other.firstname is None or self.firstname == other.firstname)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize