# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '<PUT YOUR SECRET KEY HERE>'
os.environ.setdefault('DJANGO_DATABASE', 'dev')
DEBUG = True
