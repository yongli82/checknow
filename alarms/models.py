#!/usr/bin/env python
# -*- coding:utf-8 -*-

from decimal import Decimal

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class AlarmProductStatus(object):
    STATUS_INIT = 1
    STATUS_PUBLISHED = 2
    STATUS_UNPUBLISHED = 3
    STATUS_CHOICES = {
        STATUS_INIT: "待发布",
        STATUS_PUBLISHED: "已发布",
        STATUS_UNPUBLISHED: "已下架",
    }


class AlarmProductMediaType(object):
    VOICE_MEDIA = 1
    VIDEO_MEDIA = 2
    CHOICES = {
        VOICE_MEDIA: "音频",
        VIDEO_MEDIA: "视频",
    }


class AlarmOrderStatus(object):
    STATUS_RUNNING = 1
    STATUS_COMPLETED = 2
    STATUS_INVALID = 3
    STATUS_CHOICES = {
        STATUS_RUNNING: "生效",
        STATUS_COMPLETED: "完成",
        STATUS_INVALID: "作废",
    }


class AlarmProduct(models.Model):
    """
    闹铃产品是一项服务，类似于订阅广播，可以每天收到新的内容。
    每天的内容用AlarmProductItem保存，通过外键关联到产品。
    闹铃产品
      |- 闹铃产品项目 2016-05-01
      |- 闹铃产品项目 2016-05-02
    """
    author = models.ForeignKey(User, related_name='alarm_author', verbose_name="创建者", help_text="创建者")
    title = models.CharField("标题", help_text="标题", max_length=120, blank=True, null=True)
    content = models.TextField("内容", blank=True, null=True)
    cover_image = models.CharField("封面图路径", help_text="封面图路径", max_length=1024, blank=True, null=True)
    price = models.DecimalField("价格", help_text="价格", max_digits=12, decimal_places=2, blank=True, null=True)
    member_price = models.DecimalField("会员价格", help_text="会员价格", max_digits=12, decimal_places=2, blank=True, null=True)
    promotion_price = models.DecimalField("促销价格", help_text="促销价格", max_digits=12, decimal_places=2, blank=True,
                                          null=True)
    status = models.IntegerField("状态", choices=AlarmProductStatus.STATUS_CHOICES.items(),
                                 default=AlarmProductStatus.STATUS_INIT)
    created_at = models.DateTimeField("创建时间", auto_now_add=True)
    updated_at = models.DateTimeField("修改时间", auto_now=True)

    class Meta:
        db_table = "alarm_products"
        verbose_name = "闹铃产品"
        verbose_name_plural = "闹铃产品"

    def __unicode__(self):
        return "[%s]创建的闹铃产品[%s: %s]" % (self.author, self.id, self.title)


class AlarmProductItem(models.Model):
    """
    闹铃产品项目
    """
    product = models.ForeignKey(AlarmProduct, related_name='alarm_product', verbose_name="闹铃产品", help_text="闹铃产品")
    media_path = models.CharField("媒体路径", help_text="媒体路径", max_length=1024, blank=True, null=True)
    media_type = models.IntegerField("媒体类型", choices=AlarmProductMediaType.CHOICES.items(),
                                     default=AlarmProductMediaType.VOICE_MEDIA)
    status = models.IntegerField("状态", choices=AlarmProductStatus.STATUS_CHOICES.items(),
                                 default=AlarmProductStatus.STATUS_INIT)
    item_title = models.CharField("标题", help_text="标题(可选)", max_length=120, blank=True, null=True)
    item_content = models.TextField("内容", help_text="内容(可选)", blank=True, null=True)
    item_cover_image = models.CharField("封面图路径", help_text="封面图路径(可选)", max_length=1024, blank=True, null=True)
    published_at = models.DateField("发布日期", blank=True, null=True)
    created_at = models.DateTimeField("创建时间", auto_now_add=True)
    updated_at = models.DateTimeField("修改时间", auto_now=True)

    class Meta:
        db_table = "alarm_product_items"
        verbose_name = "闹铃产品项目"
        verbose_name_plural = "闹铃产品项目"

    def __unicode__(self):
        return "闹铃产品项目[%s: %s]" % (self.id, self.title)


class AlarmOrder(models.Model):
    user = models.ForeignKey(User, related_name='alarm_order_user', verbose_name="购买者", help_text="购买者")
    product = models.ForeignKey(AlarmProduct, related_name='alarm_order_product', verbose_name="闹铃产品", help_text="闹铃产品")
    quantity = models.IntegerField("数量", help_text="数量", default=1)
    amount = models.DecimalField("金额", help_text="金额", max_digits=12, decimal_places=2, blank=True,
                                 null=True)
    consumed = models.DecimalField("消费", help_text="消费", max_digits=12, decimal_places=2, default=Decimal(0))
    status = models.IntegerField("状态", help_text="状态", choices=AlarmOrderStatus.STATUS_CHOICES.items(),
                                 default=AlarmOrderStatus.STATUS_RUNNING)
    ordered_at = models.DateField("订购日期", auto_now_add=True)
    created_at = models.DateTimeField("创建时间", auto_now_add=True)
    updated_at = models.DateTimeField("修改时间", auto_now=True)

    class Meta:
        db_table = "alarm_product_orders"
        verbose_name = "闹铃产品订单"
        verbose_name_plural = "闹铃产品订单"

    def __unicode__(self):
        return "闹铃产品订单[%s: %s 订购产品 %s]" % (self.id, self.user, self.product)


class AlarmBalance(models.Model):
    user = models.ForeignKey(User, related_name='alarm_balance_user', verbose_name="用户", help_text="用户")
    current_balance = models.DecimalField("现金余额", help_text="现金余额", max_digits=12, decimal_places=2, default=Decimal(0))
    alarm_balance = models.DecimalField("闹币余额", help_text="闹币余额", max_digits=12, decimal_places=2, default=Decimal(0))
    current_consumed = models.DecimalField("现金消费", help_text="现金消费", max_digits=12, decimal_places=2,
                                           default=Decimal(0))
    alarm_consumed = models.DecimalField("闹币消费", help_text="闹币消费", max_digits=12, decimal_places=2, default=Decimal(0))
    created_at = models.DateTimeField("创建时间", auto_now_add=True)
    updated_at = models.DateTimeField("修改时间", auto_now=True)

    class Meta:
        db_table = "alarm_balances"
        verbose_name = "账户余额"
        verbose_name_plural = "账户余额"

    def __unicode__(self):
        return "账户[%s: %s 订购产品 %s]" % (self.id, self.user)


class AlarmTriggerScheduleType(object):
    """
    触发器日程类型:指定时间（某天某时某分），循环日程（每天某时某分，周一某时某分）
    """
    ONE_TIME_SCHEDULE = 1
    DAILY_LOOP_SCHEDULE = 2
    WEEKLY_LOOP_SCHEDULE = 3
    MONTHLY_LOOP_SCHEDULE = 4
    YEARLY_LOOP_SCHEDULE = 5
    WORKDAY_LOOP_SCHEDULE = 6
    REST_DAY_LOOP_SCHEDULE = 7
    CHOICES = {
        ONE_TIME_SCHEDULE: "一次性日程",
        DAILY_LOOP_SCHEDULE: "按日循环日程",
        WEEKLY_LOOP_SCHEDULE: "按周循环日程",
        MONTHLY_LOOP_SCHEDULE: "按月循环日程",
        YEARLY_LOOP_SCHEDULE: "按年循环日程",
        WORKDAY_LOOP_SCHEDULE: "按工作日循环日程",
        REST_DAY_LOOP_SCHEDULE: "按休息日循环日程",
    }


class AlarmTrigger(models.Model):
    """
    闹铃触发设置
    """
    user = models.ForeignKey(User, related_name='alarm_balance_user', verbose_name="用户", help_text="用户")
    product = models.ForeignKey(AlarmProduct, related_name='alarm_order_product', verbose_name="闹铃产品", help_text="闹铃产品")
    schedule_type = models.IntegerField("日程类型", help_text="日程类型", choices=AlarmTriggerScheduleType.CHOICES.items(),
                                 default=AlarmTriggerScheduleType.DAILY_LOOP_SCHEDULE)
    schedule_time = models.TimeField("闹铃时间")
    
    