# from __future__ import absolute_import
# import os
# import ssl
# from celery import Celery
# from django.conf import settings
# from celery.schedules import crontab

# # set the default Django settings module for the 'celery' program.
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blog.settings")
# app = Celery("blog")

# # Using a string here means the worker will not have to
# # pickle the object when using Windows.
# app.config_from_object("django.conf:settings")
# app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

# REDIS_CONNECTION = settings.REDIS_CONNECTION_STRING

# CELERY_CONFIG = dict(
#     BROKER_URL="{redis}/0".format(redis=REDIS_CONNECTION),
#     BROKER_TRANSPORT_OPTIONS={
#         "visibility_timeout": 86400,
#         "fanout_prefix": True,
#         "fanout_patterns": True,
#     },
#     CELERYBEAT_SCHEDULER="django_celery_beat.schedulers:DatabaseScheduler",
#     CELERY_RESULT_BACKEND="{redis}/1".format(redis=REDIS_CONNECTION),
#     CELERY_DISABLE_RATE_LIMITS=True,
#     CELERY_IGNORE_RESULT=True,
#     CELERY_ACCEPT_CONTENT=[
#         "json",
#     ],
#     CELERY_TASK_SERIALIZER="json",
#     CELERY_RESULT_SERIALIZER="json",
# )


# CELERY_CONFIG["BROKER_USE_SSL"] = {"ssl_cert_reqs": ssl.CERT_NONE}

# app.conf.update(**CELERY_CONFIG)


# @app.task(bind=True)
# def debug_task(self):
#     print("Request: {0!r}".format(self.request))


# app.conf.beat_schedule = {
#     "milli_bank_get_currencies": {
#         "task": "blog.tasks.bank_currency_parser",
#         "schedule": crontab(
#             minute="*", hour="*", day_of_month="*", month_of_year="*", day_of_week="*"
#         ),
#     }
# }
