# Generated by Django 4.1.7 on 2023-04-04 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tips', '0003_alter_tip_favorite_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tip',
            name='category',
            field=models.IntegerField(blank=True, choices=[(1, 'Yoga/Stretching'), (2, 'Diet/Supplements'), (3, 'Lifestyle/Other')], null=True),
        ),
        migrations.AlterField(
            model_name='tip',
            name='favorite_count',
            field=models.IntegerField(default='0'),
        ),
    ]