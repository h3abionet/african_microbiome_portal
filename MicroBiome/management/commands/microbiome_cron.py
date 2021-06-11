from django.core.management.base import BaseCommand, CommandError
from MicroBiome import models


class Command(BaseCommand):

    """Docstring for Command. """

    def __init__(self):
        """TODO: to be defined. """
        BaseCommand.__init__(self)

    def handle(self, *args, **options):
        """TODO: Docstring for function.

        :arg1: TODO
        :returns: TODO

        """
        xx = models.Assay.objects.all()
        for x in xx:
            print(x.assay)
        pass
