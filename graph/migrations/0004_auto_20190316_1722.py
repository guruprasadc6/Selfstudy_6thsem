# Generated by Django 2.1.7 on 2019-03-16 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('graph', '0003_stock'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stocks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.TextField(max_length=5)),
                ('actual_price', models.FloatField()),
                ('predicted_price', models.FloatField()),
                ('timestamp', models.DateTimeField(null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Stock',
        ),
    ]
