# Generated by Django 3.1.2 on 2020-11-16 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20201116_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='transactionID',
            field=models.UUIDField(blank=True, default=None, null=True),
        ),
    ]
