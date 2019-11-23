#!/usr/bin/python
# -*- coding: utf-8 -*-
from app.config.loader import loader


if __name__ == '__main__':
    loader().run(debug=True, use_reloader=True)
