"""
Django allows you to specify configuration classes for your application.
When you create an application using the startapp command, Django adds
an app.py file to the application directory, including a basic application
configuration that inherits from the AppConfig class.
The application configuration class allows you to store metadata and the
configuration for the application, and it provides introspection for the
application.
"""

from django.apps import AppConfig


class ImagesConfig(AppConfig):
    name = 'images'

    def ready(self):
        # import signal handler
        import images.signals