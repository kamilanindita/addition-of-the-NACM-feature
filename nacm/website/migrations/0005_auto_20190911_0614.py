# Generated by Django 2.1.7 on 2019-09-11 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_c_setting_sett_vlan'),
    ]

    operations = [
        migrations.AddField(
            model_name='c_setting',
            name='sett_dynamic_routing_ospf_ipv6',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='c_setting',
            name='sett_static_routing_ipv6',
            field=models.TextField(blank=True, null=True),
        ),
    ]
