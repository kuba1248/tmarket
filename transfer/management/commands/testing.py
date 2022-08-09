# from django.core.management.base import BaseCommand
# # from website.models import Auction, user
# from website.models import Product, UserDetails, Auction
#
# from django.utils import timezone
# from django.core.management import call_command
# import datetime
# import random
#
# class Command(BaseCommand):
#     help = 'creates 500 randomly generated products'
#
#     def handle(self, *args, **options):
#         for i in range(9, 100):
#             # now = timezone.now()
#             # date_posted = now + datetime.timedelta(seconds=random.randint(0, 90))
#             # title = random.choice(player_list)
#             # image = random.choice(image_list)
#             # quantity = random.randint(1, 10)
#             # description = random.choice(position_list)
#             # category = random.choice(category_list)
#             d = Product.objects.filter(id=i)
#             print(d)
#             # product_id = d[0]