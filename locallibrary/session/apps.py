from django.apps import AppConfig


class SessionConfig(AppConfig):
    name = 'session'

    def ready(self):
        import session.signals