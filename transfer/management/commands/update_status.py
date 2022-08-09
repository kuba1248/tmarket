# from django.core.management.base import BaseCommand
# from auction.models import Auction
# from django.utils import timezone
#
#
# class Command(BaseCommand):
#     help = 'Updates the status of active auctions to inactive after reaching end time'
#
#     def handle(self, *args, **options):
#         allAuctions = Auction.objects.all()
#         for auction in allAuctions:
#             auction.check_status()
#         print(f"Statuses updated at {timezone.now()}")
#
