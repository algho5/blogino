# Generated by Django 3.2.9 on 2021-11-05 11:01

from django.db import migrations, models
import django.db.models.deletion
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.category'),
        ),
        migrations.AlterField(
            model_name='article',
            name='image',
            field=sorl.thumbnail.fields.ImageField(upload_to='blog-images/'),
        ),
    ]
