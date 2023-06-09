# Generated by Django 4.1.4 on 2023-02-26 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0003_lead'),
    ]

    operations = [
        migrations.CreateModel(
            name='SentimentModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sentence', models.CharField(max_length=120)),
            ],
        ),
        migrations.AlterField(
            model_name='lead',
            name='cust_probability',
            field=models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='lead',
            name='priority',
            field=models.CharField(choices=[('HIGH', 'HIGH'), ('MEDIUM', 'MEDIUM'), ('LOW', 'LOW')], max_length=200, null=True),
        ),
    ]
