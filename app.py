from application.app_factory import create_web_app

app = create_web_app()


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
