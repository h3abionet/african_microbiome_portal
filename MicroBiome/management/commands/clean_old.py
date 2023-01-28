#!/usr/bin/env python

# https://pypi.org/project/django-crontab/

from shutil import rmtree
from glob import glob
from django.conf import settings
import datetime
import os

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Docstring for Command."""

    def __init__(self):
        """TODO: to be defined."""
        BaseCommand.__init__(self)

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        """TODO: Docstring for function.

        :arg1: TODO
        :returns: TODO

        """
        today = datetime.datetime.today()

        fold = f"{settings.STATIC_ROOT}/downloads"

        for fl in glob(f"{fold}/*"):
            # print(fl)
            modified_date = datetime.datetime.fromtimestamp(
                os.path.getmtime(fl))
            duration = today - modified_date
            if duration.days > 7:
                rmtree(fl)
