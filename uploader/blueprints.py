def register_files(app, url_prefix=None) -> None:
    from files.controller import FileController
    from files import create_endpoints

    api_blueprint = create_endpoints(FileController)
    app.register_blueprint(api_blueprint, url_prefix=url_prefix)


def register_folders(app, url_prefix=None) -> None:
    from folders.controller import FolderController
    from folders import create_endpoints

    api_blueprint = create_endpoints(FolderController)
    app.register_blueprint(api_blueprint, url_prefix=url_prefix)


def register_users(app, url_prefix=None) -> None:
    from users.controller import UserController
    from users import create_endpoints

    api_blueprint = create_endpoints(UserController)
    app.register_blueprint(api_blueprint, url_prefix=url_prefix)


def register_config(app, url_prefix=None) -> None:
    from config import create_endpoints

    api_blueprint = create_endpoints()
    app.register_blueprint(api_blueprint, url_prefix=url_prefix)
