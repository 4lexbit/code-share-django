from django.core.management.base import BaseCommand
from ..models import Snippet
from datetime import datetime, timedelta


# Was created for use with the cron utility
class PurgeCommand(BaseCommand):
    help = 'Delete objects older than 10 days'

    def handle(self, *args, **options):
        Snippet.objects.filter(date__lte=datetime.now() - timedelta(days=10)).delete()
        self.stdout.write('Deleted objects older than 10 days')
