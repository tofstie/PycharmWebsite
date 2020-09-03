import flask
import os
import sys
print("started")
folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, folder)

app = flask.Flask(__name__)


def main():
    register_blueprints()
    setup_db()
    app.run(debug=True)


def setup_db():
    from data.db_session import global_init
    print("setting up")
    db_file = os.path.join(
        os.path.dirname(__file__),
        'db',
        'flaskProject.sqlite')

    global_init(db_file)


def register_blueprints():
    from views import home_views
    from views import package_views
    from views import cms_views

    app.register_blueprint(home_views.blueprint)
    app.register_blueprint(package_views.blueprint)
    app.register_blueprint(cms_views.blueprint)


if __name__ == "__main__":
    main()
else:
    main()
