from django.apps import AppConfig
import logging

logger = logging.getLogger(__name__)

class PltplconfConfig(AppConfig):
    name = 'pltplconf'
    verbose_name = "pl-log-notic应用程序"

    def ready(self):
        """服务器启动后初始化应用"""
