"""
Django settings for casher project.

Generated by 'django-admin startproject' using Django 5.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from datetime import timedelta
from pathlib import Path

from dotenv import dotenv_values

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-i(cf)0ow&74jv8l86wiu@wn(@*rvj3$5*p3ditoanrgs$oxi5o"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

if DEBUG:
    config = dotenv_values("test.env")
else:
    config = dotenv_values("prod.env")

SECURE_SSL_REDIRECT = False
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ["aidep.cn", "www.aidep.cn", "*"]
CSRF_TRUSTED_ORIGINS = ["https://aidep.cn", "https://aidep.cn"]
DATA_UPLOAD_MAX_NUMBER_FIELDS = 2000


# Application definition

INSTALLED_APPS = [
    "daphne",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.google",
    "allauth.socialaccount.providers.weixin",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "corsheaders",
    "rest_framework",
    "rest_framework.authtoken",
    "rest_framework_simplejwt",
    "djstripe",
    "casher",
    "flow",
    "task",
    "dj_rest_auth",
    "dj_rest_auth.registration",
    "payment",
    "wxapp",
    "wxappb",
    "accounts",
    "invitation",
    "cash_statistics",
]

SITE_ID = 1

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
    "casher.log_middleware.RequestResponseLoggingMiddleware",
]

CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_METHODS = [
    'GET',
    'POST',
    'OPTIONS',
    'PUT',
    'DELETE',
]

# 允许的请求头
CORS_ALLOW_HEADERS = [
    "Authorization",
    "authorization",
    "Content-Type",
    "X-Requested-With",
    "x-requested-with",
    "languageStr",
    "languagestr",
]

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by email
    "allauth.account.auth_backends.AuthenticationBackend",
)
SOCIAL_AUTH_REQUIRE_POST = True

ROOT_URLCONF = "casher.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "casher.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",  # 或者使用 'django.db.backends.mysql'
        "NAME": "casher",
        "USER": config.get("MYSQL_USERNAME"),
        "PASSWORD": config.get("MYSQL_PASSWORD"),
        "HOST": config.get("MYSQL_HOST"),
        "PORT": config.get("MYSQL_PORT"),  # mysql 端口
        "OPTIONS": {"charset": "utf8mb4"},
    }
}

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#         'OPTIONS': {
#             'timeout': 30,  # 设置为 30 秒超时
#         }
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "zh-Hans"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "static"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
        "LOCATION": BASE_DIR / "cache",
    }
}

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

ASGI_APPLICATION = "casher.asgi.application"

# 配置通道层，channels 需要一个消息队列来处理多个连接
CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "channels.layers.InMemoryChannelLayer",  # 内存中运行通道层，适用于小项目或开发阶段
    },
}
WS_CLOSE_TIMEOUT = 60  # 单位：秒，设置为 60 秒

REST_AUTH = {"USE_JWT": True}
SIMPLE_JWT = {
    "AUTH_HEADER_TYPES": ("Bearer", "bearer"),
    "ACCESS_TOKEN_LIFETIME": timedelta(days=1),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=5),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
}
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "dj_rest_auth.jwt_auth.JWTCookieAuthentication",
        # "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    'EXCEPTION_HANDLER': 'utils.custom_exception_handler'
}
REST_AUTH_SERIALIZERS = {
    "JWT_SERIALIZER": "dj_rest_auth.serializers.JWTSerializer",
}

SOCIAL_AUTH_URL_NAMESPACE = "social"
LOGIN_REDIRECT_URL = "/"  # 登录后跳转的页面
LOGOUT_REDIRECT_URL = "/"  # 登出后跳转的页面


GOOGLE_OAUTH_CLIENT_ID = config.get("GOOGLE_OAUTH_CLIENT_ID")
GOOGLE_OAUTH_CLIENT_SECRET = config.get("GOOGLE_OAUTH_CLIENT_SECRET")
GOOGLE_OAUTH_CALLBACK_URL = config.get("GOOGLE_OAUTH_CALLBACK_URL")
WEIXIN_OAUTH_CALLBACK_URL = config.get("WEIXIN_OAUTH_CALLBACK_URL")
ACCOUNT_EMAIL_VERIFICATION = "none"
SOCIALACCOUNT_EMAIL_AUTHENTICATION = True
# Connect local account and social account if local account with that email address already exists
SOCIALACCOUNT_EMAIL_AUTHENTICATION_AUTO_CONNECT = True
SOCIALACCOUNT_PROVIDERS = {
    "google": {
        "APPS": [
            {
                "client_id": GOOGLE_OAUTH_CLIENT_ID,
                "secret": GOOGLE_OAUTH_CLIENT_SECRET,
            },
        ],
        "SCOPE": ["profile", "email"],
        "AUTH_PARAMS": {
            "access_type": "online",
        },
    },
    "weixin": {
        "APP": {
            "client_id": config.get('WEIXINB_H5_APPID'),
            "secret": config.get('WEIXINB_H5_APPSECRET'),
        },
    },
}

WEIXIN_APPID = config.get("WEIXIN_APPID")
WEIXIN_APPSECRET = config.get("WEIXIN_APPSECRET")

WEIXINH5_APPID = config.get("WEIXINH5_APPID")
WEIXINH5_APPSECRET = config.get("WEIXINH5_APPSECRET")

WEIXINB_H5_APPID = config.get('WEIXINB_H5_APPID')
WEIXINB_H5_APPSECRET = config.get('WEIXINB_H5_APPSECRET')

WEIXINPAY_MCHID = config.get("WEIXINPAY_MCHID")
WEIXINPAY_APPID = config.get("WEIXINPAY_APPID")
WEIXINPAY_APIV3KEY = config.get("WEIXINPAY_APIV3KEY")
WEIXINPAY_SERIAL_NO = config.get("WEIXINPAY_SERIAL_NO")

WEIXINB_APPID = config.get("WEIXINB_APPID")
WEIXINB_APPSECRET = config.get("WEIXINB_APPSECRET")

# Stripe API Key
STRIPE_TEST_PUBLIC_KEY = config.get("STRIPE_TEST_PUBLIC_KEY")
STRIPE_TEST_SECRET_KEY = config.get("STRIPE_TEST_SECRET_KEY")
STRIPE_LIVE_MODE = False  # False 表示测试模式
DJSTRIPE_WEBHOOK_SECRET = config.get("DJSTRIPE_WEBHOOK_SECRET")
DJSTRIPE_USE_NATIVE_JSONFIELD = True
DJSTRIPE_WEBHOOK_VALIDATION = "retrieve_event"
DJSTRIPE_FOREIGN_KEY_TO_FIELD = "id"
DJSTRIPE_AUTO_SYNC_MODELS = True

PAGSMILE_APP_ID = config.get("PAGSMILE_APP_ID")
PAGSMILE_SECRET_KEY = config.get("PAGSMILE_SECRET_KEY")
PAGSMILE_URL = config.get("PAGSMILE_URL")

YUNZHANGHU_DEALER_ID = config.get("YUNZHANGHU_DEALER_ID")
YUNZHANGHU_BROKER_ID = config.get("YUNZHANGHU_BROKER_ID")
YUNZHANGHU_3DES_KEY = config.get("YUNZHANGHU_3DES_KEY")
YUNZHANGHU_APP_KEY = config.get("YUNZHANGHU_APP_KEY")
YUNZHANGHU_PUBLIC_KEY = config.get("YUNZHANGHU_PUBLIC_KEY")
YUNZHANGHU_PRIVATE_KEY = config.get("YUNZHANGHU_PRIVATE_KEY")
YUNZHANGHU_HOST = config.get("YUNZHANGHU_HOST")

# Celery settings
CELERY_BROKER_URL = config.get("CELERY_BROKER_URL")
CELERY_RESULT_BACKEND = config.get("CELERY_RESULT_BACKEND")
REDBEAT_REDIS_URL = config.get("REDBEAT_REDIS_URL")

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',  # 使用花括号作为格式化符号
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'django': {
            'level': 'INFO',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': str(BASE_DIR / 'logs/django.log'),
            'when': 'midnight',  # 按天切割日志
            'backupCount': 7,     # 保留7天的日志
            'formatter': 'verbose',  # 使用 verbose 格式
        },
        'channel': {
            'level': 'DEBUG',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': str(BASE_DIR / 'logs/channel.log'),
            'when': 'midnight',
            'backupCount': 7,
            'formatter': 'verbose',  # 使用 verbose 格式
        },
    },
    'loggers': {
        'django': {
            'handlers': ['django'],
            'level': 'INFO',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['django'],
            'level': 'ERROR',  # 只记录错误日志
            'propagate': False,
        },
        'channel': {
            'handlers': ['channel'],
            'level': 'DEBUG',  # 记录所有日志
            'propagate': False,
        },
    },
}
