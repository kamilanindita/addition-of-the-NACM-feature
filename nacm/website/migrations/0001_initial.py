# Generated by Django 2.1.7 on 2019-03-27 03:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Connect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(blank=True, max_length=255, null=True)),
                ('conft', models.TextField(blank=True, null=True)),
                ('fileup', models.FileField(blank=True, null=True, upload_to='')),
                ('fileup_name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ipaddr', models.CharField(max_length=255)),
                ('vendor', models.CharField(max_length=255)),
                ('connect_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='devices', to='website.Connect')),
            ],
            options={
                'db_table': 'autonet_ip',
            },
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sett_name', models.CharField(max_length=255)),
                ('sett_name_desc', models.CharField(max_length=255)),
                ('sett_static_routing', models.TextField(blank=True, null=True)),
                ('sett_dynamic_routing_ospf', models.TextField(blank=True, null=True)),
                ('sett_dynamic_routing_ripv1', models.TextField(blank=True, null=True)),
                ('sett_dynamic_routing_ripv2', models.TextField(blank=True, null=True)),
                ('sett_dynamic_routing_bgp', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'autonet_setting',
            },
        ),
    ]
