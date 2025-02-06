import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Configurações básicas
DEBUG = os.getenv('DEBUG', 'True') == 'True'

# Defina ALLOWED_HOSTS
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')

# Configurações do banco de dados
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('POSTGRES_DB', 'lacrei'),  # Nome do banco de dados
        'USER': os.getenv('POSTGRES_USER', 'lacrei'),  # Nome do usuário do PostgreSQL
        'PASSWORD': os.getenv('POSTGRES_PASSWORD', 'lacrei'),  # Senha do usuário
        'HOST': os.getenv('POSTGRES_HOST', 'db'),  # Nome do serviço no docker-compose.yml
        'PORT': os.getenv('POSTGRES_PORT', '5432'),  # Porta do PostgreSQL
    }
}

# Configuração do ROOT_URLCONF
ROOT_URLCONF = 'core.urls'

SECRET_KEY = os.getenv('SECRET_KEY', 'vixyepw(_q^!%@xq8s(xyqk*wt1!2+w-##=-o0@5!dsdw(-%5=')

# Configurações de aplicativos instalados
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',  # Adicionado suporte ao Django REST Framework
    'core',
    'consultas',
]

# Configurações de middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Configurações de templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Configurações de arquivos estáticos
STATIC_URL = 'static/'

# Configuração do REST Framework
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.AllowAny',
    ),
}
