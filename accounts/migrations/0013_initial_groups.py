# Generated by Django 3.0.4 on 2020-04-13 11:19

from django.db import migrations


# mapping
add = ['add']
change = ['change']
delete = ['delete']
add_change = add + change
add_change_delete = add + change + delete

permissions = {
    'Администраторы': {
        'auth': {
            'user': change,
        },
        'accounts': {
            'profile': add_change_delete + ["can_drive"],
        },
    },
    'Подрядные организации': {
        'auth': {
            'user': change,
        },
        'accounts': {
            'profile': add_change_delete + ["can_drive"],
        },
    },
    'Отдел обработки информации': {
        'auth': {
            'user': change,
        },
        'accounts': {
            'profile': add_change_delete + ["can_drive"],
        },
    },
    'Сотрудники КПП': {
        'auth': {
            'user': change,
        },
        'accounts': {
            'profile': add_change_delete + ["can_drive"],
        },
    },
    'Inspector': {
        'auth': {
            'user': change,
        },
        'accounts': {
            'profile': add_change_delete + ["can_drive"],
        },
    },
    'Инспектора': {
        'auth': {
            'user': change,
        },
        'accounts': {
            'profile': add_change_delete + ["can_drive"],
        },
    },
}


def add_group_permissions(apps, schema_editor):
    ContentType = apps.get_model('contenttypes', 'ContentType')
    Group = apps.get_model('auth', 'Group')
    Permission = apps.get_model('auth', 'Permission')

    for group_name in permissions:
        group, created = Group.objects.get_or_create(name=group_name)
        mapping = permissions.get(group_name)
        for app_label in mapping:
            for model in mapping[app_label]:
                actions = mapping[app_label][model]
                try:
                    contenttype = ContentType.objects.get(app_label=app_label, model=model)
                    for action in actions:
                        try:
                            code_name = ''
                            if action in add_change_delete:
                                permission = Permission.objects.get(content_type=contenttype,
                                                                    codename='{action}_{model}'
                                                                    .format(action=action, model=model))
                            else:
                                permission = Permission.objects.get(content_type=contenttype,
                                                                    codename=action)
                            group.permissions.add(permission)
                        except Permission.DoesNotExist as e:
                            print('--> ', e)
                except ContentType.DoesNotExist as e:
                    print('--> ', e)


def remove_group_permissions(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')

    for group_name in permissions:
        try:
            Group.objects.get(name=group_name).delete()
        except Group.DoesNotExist as e:
            print('--> ', e)


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20200405_2108'),
    ]

    operations = [
        migrations.RunPython(add_group_permissions, remove_group_permissions),
    ]


