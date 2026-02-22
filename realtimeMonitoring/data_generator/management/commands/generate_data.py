from django.core.management.base import BaseCommand
from realtimeMonitoring import utils


class Command(BaseCommand):
    help = 'Generates mock data for testing the database performance'

    def add_arguments(self, parser):
        parser.add_argument(
            'count',
            nargs='?',
            type=int,
            default=500000,
            help='Number of data points to generate (default: 500000)',
        )

    def handle(self, *args, **kwargs):
        data_qty = kwargs['count']
        utils.register_users()
        utils.generateMockData(data_qty)
