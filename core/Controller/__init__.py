#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import app, request, render_template
from flask.views import View
from core.View import _View
import inspect


class Controller(View):

    def __init__(self, action_name):
        super(Controller, self).__init__()
        self.__action_name = action_name
        self._app = app

    def dispatch_request(self, *args, **kwargs):
        action = getattr(self, self.__action_name, None)
        if action is None:
            raise Exception('action_name', 'Action {0} not found'.format(self.__action_name))
        return action(*args, **kwargs)

    def setView(self, view_name=None, **kwargs):
        if view_name is None:
            view_name = inspect.stack()[1][3]
        view_path = _View.view_name(self, view_name)

        if 'app' not in kwargs:
            kwargs['app'] = self._app

        return render_template(view_path, **kwargs)
