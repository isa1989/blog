from __future__ import absolute_import
from celery import shared_task

from news.models import Upvote


@shared_task
def all_upvotes_delete():
    Upvote.objects.all().delete()
    return "All upvotes deleted!"
