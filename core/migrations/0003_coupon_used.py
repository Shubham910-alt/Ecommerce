# Generated by Django 4.0 on 2022-07-15 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_refund_order_remove_userprofile_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='used',
            field=models.BooleanField(default=False),
        ),
    ]