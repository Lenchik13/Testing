from model.group import Group

def test_modify_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="gr1", header="grr1", footer="grrr1"))
    app.group.modify_group()


def test_modify_first_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="gr1", header="grr1", footer="grrr1"))
    app.group.modify_first_group(Group(name="New group"))


def test_modify_first_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="gr1", header="grr1", footer="grrr1"))
    app.group.modify_first_group(Group(header="New header"))
