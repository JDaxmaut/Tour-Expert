from django.db import migrations


PAGES = [
    ('turoperatoram',            'Туроператорам',           0),
    ('organizatoram-turov',      'Организаторам туров',     1),
    ('turagentam',               'Турагентам',              2),
    ('gidam-i-instruktoram',     'Гидам и инструкторам',   3),
    ('oteliam-i-gostevym-domam', 'Отелям и гостевым домам',4),
]


def create_pages(apps, schema_editor):
    AudiencePage = apps.get_model('core', 'AudiencePage')
    for slug, title, order in PAGES:
        AudiencePage.objects.get_or_create(
            slug=slug,
            defaults={'title': title, 'order': order, 'is_published': True},
        )


def delete_pages(apps, schema_editor):
    AudiencePage = apps.get_model('core', 'AudiencePage')
    AudiencePage.objects.filter(slug__in=[s for s, *_ in PAGES]).delete()


class Migration(migrations.Migration):
    dependencies = [
        ('core', '0005_audiencepage'),
    ]

    operations = [
        migrations.RunPython(create_pages, delete_pages),
    ]
