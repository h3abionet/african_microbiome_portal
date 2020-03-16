class Command(BaseCommand):
    args = '[count]'

    def handle(self, count=20, *args, **options):

        try:
            i = int(count)
        except ValueError:
            print u'n is to be a number!'
            sys.exit(1)

        for _ in range(i):
            # you can pass params explicitly
            m = any_model(MY_MODEL_CLASS, image=None)
            m.save()
