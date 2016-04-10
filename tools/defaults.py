#!/usr/bin/env python
# -*- coding:utf-8 -*-

from __future__ import absolute_import, unicode_literals

from mezzanine.conf import register_setting


# USE_VERIFY_CODE = False
# VERIFY_CODE_EXPIRED_SECONDS = 180
# VERIFY_CODE_TEMPLATE = "【切克闹】您的验证码是%s"
# SMS_API_KEY = "803998d17b6ff9eae33e38e3e407b773"

register_setting(
    name="SMS_USE_VERIFY_CODE",
    label="是否使用验证码",
    description="是否使用验证码",
    editable=True,
    default=False,
)

register_setting(
    name="SMS_VERIFY_CODE_EXPIRED_SECONDS",
    label="SMS_VERIFY_CODE_EXPIRED_SECONDS",
    description="SMS_VERIFY_CODE_EXPIRED_SECONDS",
    editable=True,
    default=180,
)

register_setting(
    name="SMS_VERIFY_CODE_TEMPLATE",
    label="SMS_VERIFY_CODE_TEMPLATE",
    description="SMS_VERIFY_CODE_TEMPLATE",
    editable=True,
    default="【切克闹】您的验证码是%s",
)

register_setting(
    name="SMS_API_KEY",
    label="SMS_API_KEY",
    description="SMS_API_KEY",
    editable=True,
    default="803998d17b6ff9eae33e38e3e407b773",
)



