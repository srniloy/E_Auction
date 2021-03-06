# Generated by Django 4.0.3 on 2022-04-09 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_auction_app', '0002_rename_usermails_useremails'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInformation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.RenameField(
            model_name='useremails',
            old_name='user_id',
            new_name='userId',
        ),
    ]
