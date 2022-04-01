import app.service as service, os

os.environ['APP_SETTINGS'] = "config.DevelopmentConfig"
if __name__ == '__main__':

    service.app.run()
