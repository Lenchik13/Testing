from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


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
            company=random_string("company", 10), home=random_digits("h", 10), mobile=random_digits("m", 10),
            work=random_digits("w", 10), fax=random_digits("f", 10), email=random_string("email", 20),
            email2=random_string("email2", 10), email3=random_string("email3", 20), homepage=random_string("homepage", 20),
            address2=random_string("address2", 20), phone2=random_digits("p2", 11),
            notes=random_string("notes", 10), byear=random_digits("y", 4))
    for i in range (n)
    ]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))