import sys

from bottle import app

from configuration_files.configuration_by_environment import config

if __name__ == '__main__':
    env = sys.argv[1] if len(sys.argv) > 2 else 'dev'

    if env == 'dev':
        app.config = config.DevelopmentConfig

    elif env == 'test':
        app.config = config.TestConfig
    elif env == 'prod':
        print('Select: production')
        app.config = config.ProductionConfig

    else:
        raise ValueError('Invalid environment name')

    app.ci = config.CIConfig
