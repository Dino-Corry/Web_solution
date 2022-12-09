from django.apps import AppConfig


class CryptoappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cryptoapp'
    
    def ready(self):
        import cryptoapp.signals
