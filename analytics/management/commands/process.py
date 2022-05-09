from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Start/Stop/Restart/Get information about analytics processes'

    def add_arguments(self, parser) -> None:
        parser.add_argument(
            '--start',
            action='store_true',
            help='Start processing'
        )

        parser.add_argument(
            '--detached',
            action='store_true',
            help='Detach process'
        )

    def handle(self, *args, **options) -> None:
        _start = options.get('start')

        if _start:
            self._start(*args, **options)

    def _start(self, *args, **options) -> None:
        pass
