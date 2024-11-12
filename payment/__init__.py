from django.apps import AppConfig


class MyAppConfig(AppConfig):
    name = "payment"

    def ready(self):
        import payment.signals  # ensure your signals are imported
