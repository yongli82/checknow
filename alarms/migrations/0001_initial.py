# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
from decimal import Decimal


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AlarmBalance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('current_balance', models.DecimalField(default=Decimal('0'), help_text=b'\xe7\x8e\xb0\xe9\x87\x91\xe4\xbd\x99\xe9\xa2\x9d', verbose_name=b'\xe7\x8e\xb0\xe9\x87\x91\xe4\xbd\x99\xe9\xa2\x9d', max_digits=12, decimal_places=2)),
                ('alarm_balance', models.DecimalField(default=Decimal('0'), help_text=b'\xe9\x97\xb9\xe5\xb8\x81\xe4\xbd\x99\xe9\xa2\x9d', verbose_name=b'\xe9\x97\xb9\xe5\xb8\x81\xe4\xbd\x99\xe9\xa2\x9d', max_digits=12, decimal_places=2)),
                ('current_consumed', models.DecimalField(default=Decimal('0'), help_text=b'\xe7\x8e\xb0\xe9\x87\x91\xe6\xb6\x88\xe8\xb4\xb9', verbose_name=b'\xe7\x8e\xb0\xe9\x87\x91\xe6\xb6\x88\xe8\xb4\xb9', max_digits=12, decimal_places=2)),
                ('alarm_consumed', models.DecimalField(default=Decimal('0'), help_text=b'\xe9\x97\xb9\xe5\xb8\x81\xe6\xb6\x88\xe8\xb4\xb9', verbose_name=b'\xe9\x97\xb9\xe5\xb8\x81\xe6\xb6\x88\xe8\xb4\xb9', max_digits=12, decimal_places=2)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name=b'\xe4\xbf\xae\xe6\x94\xb9\xe6\x97\xb6\xe9\x97\xb4')),
                ('user', models.ForeignKey(related_name='alarm_balance_user', verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7', to=settings.AUTH_USER_MODEL, help_text=b'\xe7\x94\xa8\xe6\x88\xb7')),
            ],
            options={
                'db_table': 'alarm_balances',
                'verbose_name': '\u8d26\u6237\u4f59\u989d',
                'verbose_name_plural': '\u8d26\u6237\u4f59\u989d',
            },
        ),
        migrations.CreateModel(
            name='AlarmOrder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.IntegerField(default=1, help_text=b'\xe6\x95\xb0\xe9\x87\x8f', verbose_name=b'\xe6\x95\xb0\xe9\x87\x8f')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12, blank=True, help_text=b'\xe9\x87\x91\xe9\xa2\x9d', null=True, verbose_name=b'\xe9\x87\x91\xe9\xa2\x9d')),
                ('consumed', models.DecimalField(default=Decimal('0'), help_text=b'\xe6\xb6\x88\xe8\xb4\xb9', verbose_name=b'\xe6\xb6\x88\xe8\xb4\xb9', max_digits=12, decimal_places=2)),
                ('status', models.IntegerField(default=1, help_text=b'\xe7\x8a\xb6\xe6\x80\x81', verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81', choices=[(1, b'\xe7\x94\x9f\xe6\x95\x88'), (2, b'\xe5\xae\x8c\xe6\x88\x90'), (3, b'\xe4\xbd\x9c\xe5\xba\x9f')])),
                ('ordered_at', models.DateField(auto_now_add=True, verbose_name=b'\xe8\xae\xa2\xe8\xb4\xad\xe6\x97\xa5\xe6\x9c\x9f')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name=b'\xe4\xbf\xae\xe6\x94\xb9\xe6\x97\xb6\xe9\x97\xb4')),
            ],
            options={
                'db_table': 'alarm_product_orders',
                'verbose_name': '\u95f9\u94c3\u4ea7\u54c1\u8ba2\u5355',
                'verbose_name_plural': '\u95f9\u94c3\u4ea7\u54c1\u8ba2\u5355',
            },
        ),
        migrations.CreateModel(
            name='AlarmProduct',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(help_text=b'\xe6\xa0\x87\xe9\xa2\x98', max_length=120, null=True, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98', blank=True)),
                ('content', models.TextField(null=True, verbose_name=b'\xe5\x86\x85\xe5\xae\xb9', blank=True)),
                ('cover_image', models.CharField(help_text=b'\xe5\xb0\x81\xe9\x9d\xa2\xe5\x9b\xbe\xe8\xb7\xaf\xe5\xbe\x84', max_length=1024, null=True, verbose_name=b'\xe5\xb0\x81\xe9\x9d\xa2\xe5\x9b\xbe\xe8\xb7\xaf\xe5\xbe\x84', blank=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=12, blank=True, help_text=b'\xe4\xbb\xb7\xe6\xa0\xbc', null=True, verbose_name=b'\xe4\xbb\xb7\xe6\xa0\xbc')),
                ('member_price', models.DecimalField(decimal_places=2, max_digits=12, blank=True, help_text=b'\xe4\xbc\x9a\xe5\x91\x98\xe4\xbb\xb7\xe6\xa0\xbc', null=True, verbose_name=b'\xe4\xbc\x9a\xe5\x91\x98\xe4\xbb\xb7\xe6\xa0\xbc')),
                ('promotion_price', models.DecimalField(decimal_places=2, max_digits=12, blank=True, help_text=b'\xe4\xbf\x83\xe9\x94\x80\xe4\xbb\xb7\xe6\xa0\xbc', null=True, verbose_name=b'\xe4\xbf\x83\xe9\x94\x80\xe4\xbb\xb7\xe6\xa0\xbc')),
                ('status', models.IntegerField(default=1, verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81', choices=[(1, b'\xe5\xbe\x85\xe5\x8f\x91\xe5\xb8\x83'), (2, b'\xe5\xb7\xb2\xe5\x8f\x91\xe5\xb8\x83'), (3, b'\xe5\xb7\xb2\xe4\xb8\x8b\xe6\x9e\xb6')])),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name=b'\xe4\xbf\xae\xe6\x94\xb9\xe6\x97\xb6\xe9\x97\xb4')),
                ('author', models.ForeignKey(related_name='alarm_author', verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe8\x80\x85', to=settings.AUTH_USER_MODEL, help_text=b'\xe5\x88\x9b\xe5\xbb\xba\xe8\x80\x85')),
            ],
            options={
                'db_table': 'alarm_products',
                'verbose_name': '\u95f9\u94c3\u4ea7\u54c1',
                'verbose_name_plural': '\u95f9\u94c3\u4ea7\u54c1',
            },
        ),
        migrations.CreateModel(
            name='AlarmProductItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('media_path', models.CharField(help_text=b'\xe5\xaa\x92\xe4\xbd\x93\xe8\xb7\xaf\xe5\xbe\x84', max_length=1024, null=True, verbose_name=b'\xe5\xaa\x92\xe4\xbd\x93\xe8\xb7\xaf\xe5\xbe\x84', blank=True)),
                ('media_type', models.IntegerField(default=1, verbose_name=b'\xe5\xaa\x92\xe4\xbd\x93\xe7\xb1\xbb\xe5\x9e\x8b', choices=[(1, b'\xe9\x9f\xb3\xe9\xa2\x91'), (2, b'\xe8\xa7\x86\xe9\xa2\x91')])),
                ('status', models.IntegerField(default=1, verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81', choices=[(1, b'\xe5\xbe\x85\xe5\x8f\x91\xe5\xb8\x83'), (2, b'\xe5\xb7\xb2\xe5\x8f\x91\xe5\xb8\x83'), (3, b'\xe5\xb7\xb2\xe4\xb8\x8b\xe6\x9e\xb6')])),
                ('item_title', models.CharField(help_text=b'\xe6\xa0\x87\xe9\xa2\x98(\xe5\x8f\xaf\xe9\x80\x89)', max_length=120, null=True, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98', blank=True)),
                ('item_content', models.TextField(help_text=b'\xe5\x86\x85\xe5\xae\xb9(\xe5\x8f\xaf\xe9\x80\x89)', null=True, verbose_name=b'\xe5\x86\x85\xe5\xae\xb9', blank=True)),
                ('item_cover_image', models.CharField(help_text=b'\xe5\xb0\x81\xe9\x9d\xa2\xe5\x9b\xbe\xe8\xb7\xaf\xe5\xbe\x84(\xe5\x8f\xaf\xe9\x80\x89)', max_length=1024, null=True, verbose_name=b'\xe5\xb0\x81\xe9\x9d\xa2\xe5\x9b\xbe\xe8\xb7\xaf\xe5\xbe\x84', blank=True)),
                ('published_at', models.DateField(null=True, verbose_name=b'\xe5\x8f\x91\xe5\xb8\x83\xe6\x97\xa5\xe6\x9c\x9f', blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name=b'\xe4\xbf\xae\xe6\x94\xb9\xe6\x97\xb6\xe9\x97\xb4')),
                ('product', models.ForeignKey(related_name='alarm_product', verbose_name=b'\xe9\x97\xb9\xe9\x93\x83\xe4\xba\xa7\xe5\x93\x81', to='alarms.AlarmProduct', help_text=b'\xe9\x97\xb9\xe9\x93\x83\xe4\xba\xa7\xe5\x93\x81')),
            ],
            options={
                'db_table': 'alarm_product_items',
                'verbose_name': '\u95f9\u94c3\u4ea7\u54c1\u9879\u76ee',
                'verbose_name_plural': '\u95f9\u94c3\u4ea7\u54c1\u9879\u76ee',
            },
        ),
        migrations.CreateModel(
            name='AlarmTrigger',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('schedule_type', models.IntegerField(default=2, help_text=b'\xe6\x97\xa5\xe7\xa8\x8b\xe7\xb1\xbb\xe5\x9e\x8b', verbose_name=b'\xe6\x97\xa5\xe7\xa8\x8b\xe7\xb1\xbb\xe5\x9e\x8b', choices=[(1, b'\xe4\xb8\x80\xe6\xac\xa1\xe6\x80\xa7\xe6\x97\xa5\xe7\xa8\x8b'), (2, b'\xe6\x8c\x89\xe6\x97\xa5\xe5\xbe\xaa\xe7\x8e\xaf\xe6\x97\xa5\xe7\xa8\x8b'), (3, b'\xe6\x8c\x89\xe5\x91\xa8\xe5\xbe\xaa\xe7\x8e\xaf\xe6\x97\xa5\xe7\xa8\x8b'), (4, b'\xe6\x8c\x89\xe6\x9c\x88\xe5\xbe\xaa\xe7\x8e\xaf\xe6\x97\xa5\xe7\xa8\x8b'), (5, b'\xe6\x8c\x89\xe5\xb9\xb4\xe5\xbe\xaa\xe7\x8e\xaf\xe6\x97\xa5\xe7\xa8\x8b'), (6, b'\xe6\x8c\x89\xe5\xb7\xa5\xe4\xbd\x9c\xe6\x97\xa5\xe5\xbe\xaa\xe7\x8e\xaf\xe6\x97\xa5\xe7\xa8\x8b'), (7, b'\xe6\x8c\x89\xe4\xbc\x91\xe6\x81\xaf\xe6\x97\xa5\xe5\xbe\xaa\xe7\x8e\xaf\xe6\x97\xa5\xe7\xa8\x8b')])),
                ('schedule_time', models.TimeField(verbose_name=b'\xe9\x97\xb9\xe9\x93\x83\xe6\x97\xb6\xe9\x97\xb4')),
                ('product', models.ForeignKey(related_name='alarm_trigger_product', verbose_name=b'\xe9\x97\xb9\xe9\x93\x83\xe4\xba\xa7\xe5\x93\x81', to='alarms.AlarmProduct', help_text=b'\xe9\x97\xb9\xe9\x93\x83\xe4\xba\xa7\xe5\x93\x81')),
                ('user', models.ForeignKey(related_name='alarm_trigger_user', verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7', to=settings.AUTH_USER_MODEL, help_text=b'\xe7\x94\xa8\xe6\x88\xb7')),
            ],
        ),
        migrations.AddField(
            model_name='alarmorder',
            name='product',
            field=models.ForeignKey(related_name='alarm_order_product', verbose_name=b'\xe9\x97\xb9\xe9\x93\x83\xe4\xba\xa7\xe5\x93\x81', to='alarms.AlarmProduct', help_text=b'\xe9\x97\xb9\xe9\x93\x83\xe4\xba\xa7\xe5\x93\x81'),
        ),
        migrations.AddField(
            model_name='alarmorder',
            name='user',
            field=models.ForeignKey(related_name='alarm_order_user', verbose_name=b'\xe8\xb4\xad\xe4\xb9\xb0\xe8\x80\x85', to=settings.AUTH_USER_MODEL, help_text=b'\xe8\xb4\xad\xe4\xb9\xb0\xe8\x80\x85'),
        ),
    ]
