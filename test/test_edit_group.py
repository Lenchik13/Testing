from model.group import Group
from random import randrange


def test_modify_first_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="gr1", header="grr1", footer="grrr1"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="New group")
    group.id = old_groups[index].id
    app.group.modify_group_by_index(index, group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    print (sorted(old_groups, key=Group.id_or_max))
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)