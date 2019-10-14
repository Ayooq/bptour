# Generated by Django 2.2.5 on 2019-10-14 12:10

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20191014_1742'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='address',
            field=models.CharField(max_length=255, null=True, verbose_name='адрес агентства'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='email',
            field=models.EmailField(max_length=254, null=True, verbose_name='электронная почта'),
        ),
        migrations.CreateModel(
            name='HomePagePhone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('landline_phone', models.CharField(max_length=20, null=True, verbose_name='стационарный телефон')),
                ('mobile_phone', models.CharField(max_length=20, null=True, verbose_name='мобильный телефон')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='phone_numbers', to='home.HomePage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]