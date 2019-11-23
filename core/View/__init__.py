from app.config.config import Config
import os


class _View:
    def __init__(self):
        pass

    application = Config.application()

    @staticmethod
    def __get_controller_name(controller):
        controller_name = controller.__class__.__name__
        if controller_name[-10:].lower() == 'controller':
            controller_name = controller_name[:-10]
        return controller_name

    @staticmethod
    def __view_exists(view_path):
        return os.path.isfile(os.path.join(_View.application['viewsDir'], view_path))

    @staticmethod
    def __view_exists_in_dir(base_dir, view_name):
        view_path = os.path.join(base_dir, view_name)
        return _View.__view_exists(view_path)

    @staticmethod
    def __get_view_name(view_name):
        view_name, ext = os.path.splitext(view_name)
        ext = ext[1:] or 'html'
        names = [view_name, '{0}.{1}'.format(view_name, ext)]
        return names

    @staticmethod
    def __find_view(controller, view_name):
        if view_name.find('/') == -1:
            controller_name = _View.__get_controller_name(controller).lower()

            # first look for views/[controller_name]/[view_name]
            # otherwise look for views/Layout/view_name
            locations = [(controller_name, view_name),
                         (controller_name, view_name.lower()),
                         ('Layout', view_name),
                         ('Layout', view_name.lower())]
            for location in locations:
                base_dir, name = location
                if _View.__view_exists_in_dir(base_dir, name):
                    return '{0}/{1}'.format(base_dir, name)

        return view_name

    @staticmethod
    def view_name(controller, view_name):
        names = _View.__get_view_name(view_name)
        for name in names:
            view_path = _View.__find_view(controller, name)
            if view_path != name:
                break
        return view_path
