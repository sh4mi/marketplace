# Generated by Django 2.2.13 on 2020-08-16 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20200816_2234'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=150)),
                ('state', models.CharField(max_length=150)),
            ],
        ),
        migrations.AddField(
            model_name='vendor',
            name='address',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='accounts.Address'),
            preserve_default=False,
        ),
    ]
