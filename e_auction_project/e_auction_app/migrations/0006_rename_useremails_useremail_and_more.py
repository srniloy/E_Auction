# Generated by Django 4.0.3 on 2022-04-09 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('e_auction_app', '0005_rename_userid_useremails_id'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserEmails',
            new_name='UserEmail',
        ),
        migrations.RenameField(
            model_name='useremail',
            old_name='email',
            new_name='user_email',
        ),
        migrations.RenameField(
            model_name='useremail',
            old_name='id',
            new_name='user_id',
        ),
    ]