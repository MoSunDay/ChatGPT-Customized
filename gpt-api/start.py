import app

if __name__ == '__main__':
    _app = app.create_app()
    _app.run(port=8080)
    # uvicorn.run(_app, host='0.0.0.0', port=8080)
