# Generated by Django 3.1.3 on 2020-12-01 16:05


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='ticket_id',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
