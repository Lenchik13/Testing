from model.group import Group
import random


def test_modify_first_group_name(app, db, check_ui):
    if app.group.count() == 0:
        app.group.create(Group(name="gr1", header="grr1", footer="grrr1"))
    old_groups = db.get_group_list()
    rgroup = random.choice(old_groups)
    group = Group(name="New group")
    group.id = rgroup.id
    app.group.modify_group_by_id(group)
    assert len(old_groups) == app.group.count()
    new_groups = db.get_group_list()
    old_groups.remove(rgroup)
    old_groups.append(group)
    print (sorted(old_groups, key=Group.id_or_max))
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
