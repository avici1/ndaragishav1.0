# Generated by Django 2.2.2 on 2019-06-09 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_founditems'),
    ]

    operations = [
        migrations.AlterField(
            model_name='founditems',
            name='img_path',
            field=models.ImageField(upload_to='image/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='lostitems',
            name='found_desc',
            field=models.TextField(default='Empty'),
        ),
        migrations.AlterField(
            model_name='lostitems',
            name='lost_desc',
            field=models.TextField(default='Empty'),
        ),
    ]