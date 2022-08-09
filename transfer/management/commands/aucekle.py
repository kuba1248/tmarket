# from django.core.management.base import BaseCommand
# # from website.models import Auction, user
# from transfer.models import Market, Myteam
#
# from django.utils import timezone
# from datetime import timedelta
# from django.core.management import call_command
# import datetime
# import random
#
# #
# class Command(BaseCommand):
#     help = 'creates 500 randomly generated auctions'
#
#     def handle(self, *args, **options):
#         markets = Market.objects.all()
#         for i in range(1, 20):
#             now = timezone.now()
#             number_of_bids = random.randint(1,10)
#             time_starting = timezone.now() + timedelta(minutes=1)
#             time_ending = timezone.now() + timedelta(days=20) + timedelta(hours=2) + timedelta(minutes=5)
#             newAuction = Auction(product_id=product_id,
#                                  number_of_bids=number_of_bids,
#                                  time_starting=time_starting,
#                                  time_ending=time_ending)
#             newAuction.save()
#
# #    python3 manage.py aucekle
#
# #
# # VALUES ('messi', 'images/game-05.png', 'FWD', '1', '2022-08-03 17:45:25.053226','CON' ),
