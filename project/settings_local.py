DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'f1api',
        'USER': 'postgres',
        'PASSWORD': 'Oxygenczak1',
        'HOST': 'localhost',
        # 'HOST': '172.17.0.1',  # docker
        'PORT': '5432',
    },
}