# from django.core.management.base import BaseCommand
# from auction.models import Auction, user
# from django.utils import timezone
# from django.core.management import call_command
# import datetime
# import random
#
#
#
#
# class Command(BaseCommand):
#     help = 'creates 50 randomly generated auctions'
#
#     def handle(self, *args, **options):
#         users = user.objects.all()
#         nUsers = len(users)
#         if nUsers<=0:
#             call_command('addUsers')
#             users = user.objects.all()
#             nUsers = len(users)
#
#         for i in range(0,50):
#             now = timezone.now()
#             endTime = now + datetime.timedelta(seconds=random.randint(0, 90))
#             itemName = f'item {random.randint(100,500)}'
#             startPrice = random.randint(1,10000)
#             highestBid = startPrice+random.randint(1,1000)
#             bidderIndex = random.randint(0,nUsers-1)
#             bidderID = users[bidderIndex].userID
#             newAuction = Auction(itemName=itemName, startTime=now, endTime=endTime,startPrice=startPrice,highestBid=highestBid,highestBidder=bidderID, isActive=True)
#             newAuction.save()
