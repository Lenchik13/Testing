from model.group import Group

#def test_modify_group(app):
#    if app.group.count() == 0:
#        app.group.create(Group(name="gr1", header="grr1", footer="grrr1"))
#    old_groups = app.group.get_group_list()
#    app.group.modify_group()
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)


def test_modify_first_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="gr1", header="grr1", footer="grrr1"))
    old_groups = app.group.get_group_list()
    group = Group(name="New group")
    group.id = old_groups[0].id
    app.group.modify_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


#def test_modify_first_group_header(app):
#    if app.group.count() == 0:
#    app.group.create(Group(name="gr1", header="grr1", footer="grrr1"))
#    old_groups = app.group.get_group_list()
#    app.group.modify_first_group(Group(header="New header"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)