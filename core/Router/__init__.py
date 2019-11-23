def Router(app, name, pattern, controller, action, **kwargs):
    app.add_url_rule(pattern, view_func=controller.as_view(name, action), **kwargs)
