#!/usr/bin/env python
# -*- coding:utf-8 -*-

from __future__ import unicode_literals

from rest_framework.views import exception_handler

from rest_framework import status

def rewrite_reponse(response):
    if response is None:
        return None
    data = response.data
    status_code = response.status_code
    reason_phrase = response.reason_phrase
    # headers = response._headers
    rewrite_data = {
        "status_code": status_code,
        "status_text": reason_phrase,
        "data": data,
    }

    response.status_code = status.HTTP_200_OK
    response.reason_phrase = "OK"
    response.data = rewrite_data

    return response


def customise_exception_handler(exc, context):
    """
    重写rest_framework的view.py中的异常处理方法。
    rest_framework使用response的http_status_code返回不同异常码。
    但是前端要求所有的响应都返回200 OK，另外用status_code和msg表明异常信息。

    Returns the response that should be used for any given exception.

    By default we handle the REST framework `APIException`, and also
    Django's built-in `Http404` and `PermissionDenied` exceptions.

    Any unhandled exceptions may return `None`, which will cause a 500 error
    to be raised.
    """
    """
    if isinstance(exc, exceptions.APIException):
        headers = {}
        if getattr(exc, 'auth_header', None):
            headers['WWW-Authenticate'] = exc.auth_header
        if getattr(exc, 'wait', None):
            headers['Retry-After'] = '%d' % exc.wait

        if isinstance(exc.detail, (list, dict)):
            data = exc.detail
        else:
            data = {'error': exc.detail}

        set_rollback()
        return Response(data, status=exc.status_code, headers=headers)

    elif isinstance(exc, Http404):
        msg = _('Not found.')
        data = {'error': six.text_type(msg)}

        set_rollback()
        return Response(data, status=status.HTTP_404_NOT_FOUND)

    elif isinstance(exc, PermissionDenied):
        msg = _('Permission denied.')
        data = {'error': six.text_type(msg)}

        set_rollback()
        return Response(data, status=status.HTTP_403_FORBIDDEN)

    # Note: Unhandled exceptions will raise a 500 error.
    return None
    """
    response = exception_handler(exc, context)
    #response1 = rewrite_reponse(response)
    return response


from rest_framework import renderers


class CustomiseJSONRenderer(renderers.JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        response = renderer_context.get("response", None)
        response1 = rewrite_reponse(response)
        if response1:
            data = response1.data
        ret = super(CustomiseJSONRenderer, self).render(data, accepted_media_type=accepted_media_type,
                                               renderer_context=renderer_context)
        return ret




