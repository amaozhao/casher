"""
Django settings for casher project.

Generated by 'django-admin startproject' using Django 5.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-i(cf)0ow&74jv8l86wiu@wn(@*rvj3$5*p3ditoanrgs$oxi5o"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["http://aidep.cn:8601", "http://0.0.0.0:8000", "*"]
CSRF_TRUSTED_ORIGINS = ["http://aidep.cn:8601", "http://0.0.0.0:8000"]
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
    "dj_rest_auth.registration",
    "payment",
    "wxapp",
    "accounts",
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
]

CORS_ALLOW_ALL_ORIGINS = True

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
        "USER": "root",
        "PASSWORD": "casher",
        "HOST": "192.168.10.100",  # 如果数据库和应用在同一台服务器上
        "PORT": "3307",  # PostgreSQL 的默认端口
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
    "AUTH_HEADER_TYPES": ("Bearer",),
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
}
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        # 'rest_framework_simplejwt.authentication.JWTAuthentication',
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ]
}
REST_AUTH_SERIALIZERS = {
    "JWT_SERIALIZER": "dj_rest_auth.serializers.JWTSerializer",
}

SOCIAL_AUTH_URL_NAMESPACE = "social"
LOGIN_REDIRECT_URL = "/"  # 登录后跳转的页面
LOGOUT_REDIRECT_URL = "/"  # 登出后跳转的页面


GOOGLE_OAUTH_CLIENT_ID = (
    "88674082295-pc3uu9ptrat6tuegmua1e4uhl0jj0i4l.apps.googleusercontent.com"
)
GOOGLE_OAUTH_CLIENT_SECRET = "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"
GOOGLE_OAUTH_CALLBACK_URL = "http://aidep.cn:8601/accounts/google/callback/"
WEIXIN_OAUTH_CALLBACK_URL = "http://aidep.cn:8601/accounts/google/callback/"
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
                "key": "",
            },
        ],
        "SCOPE": ["profile", "email"],
        "AUTH_PARAMS": {
            "access_type": "online",
        },
    },
    "weixin": {
        "APP": {
            "client_id": "wxf55b8e3b119d67cd",
            "secret": "8be5d5ebe318ecfe220f2776d79fb732",
            "key": "",
        },
    },
}

WXAPP_APPID = "wx93f89569dfcc5828"
WXAPP_SECRET = "a93d88cce0432a81cbb76b2fff27be1e"

# Stripe API Key
STRIPE_TEST_PUBLIC_KEY = "pk_test_51Q0gamCBS8Aso0qd6cFAJ17EtVgNU0xq5aXnQMgVAx0zdpRGxHVaAwCvdguB7sDGx8dr1GllHF6ydJbUwMjqEPc800CWdocpen"
STRIPE_TEST_SECRET_KEY = "sk_test_51Q0gamCBS8Aso0qdIApezKcTSfhZvPxJdTO61TRtjf5xBbsXE4TKUJ3IXxIGYNuuxMCdtjZ0k6OxAezKU5MR4qs800OH6vixIW"
STRIPE_LIVE_MODE = False  # False 表示测试模式
DJSTRIPE_WEBHOOK_SECRET = "whsec_pYrg2zCBNVYGeaOwsgRnMiMev238opnO"
DJSTRIPE_USE_NATIVE_JSONFIELD = True
DJSTRIPE_WEBHOOK_VALIDATION = "retrieve_event"
DJSTRIPE_FOREIGN_KEY_TO_FIELD = "id"
DJSTRIPE_AUTO_SYNC_MODELS = True

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": "INFO",
        },
        "channels": {
            "handlers": ["console"],
            "level": "INFO",
        },
    },
}
