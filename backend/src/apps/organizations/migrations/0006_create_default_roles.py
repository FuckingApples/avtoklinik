from django.db import migrations


def create_initial_roles(apps, schema_editor):
    Role = apps.get_model("organizations", "Role")
    Role.objects.bulk_create(
        [
            Role(name="Владелец", default_permissions=0b1111),
            Role(name="Администратор", default_permissions=0),
            Role(name="Менеджер", default_permissions=0),
            Role(name="Сотрудник", default_permissions=0),
        ]
    )


class Migration(migrations.Migration):

    dependencies = [
        ("organizations", "0005_role_remove_membership_permission_and_more"),
    ]

    operations = [
        migrations.RunPython(create_initial_roles),
    ]
