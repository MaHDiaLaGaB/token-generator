from project.app import create_app


if __name__ == '__main__':
    create_app().run(host="localhost", port=5001, debug=True)
