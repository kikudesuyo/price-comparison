import math
from util import read_csv, read_data

"""秘書問題を基に作成"""
filename_list = read_data()
for i in filename_list:
  dubble_list = read_csv("data/" + i)
  purchase_deadline  = 100
  price = dubble_list[1]
  day_number = len(dubble_list[0])
  criteria = purchase_deadline / math.e
  if day_number > criteria:
    if min(price) == price[-1]:
      print("You should buy this product")
  elif min(price) == price[-1]:
    print(" you may buy this product")
  else:
    print("you should not buy ths product")  


# dubble_list = read_csv("data/mouse.csv")
# purchase_deadline  = 100
# price = dubble_list[1]
# day_number = len(dubble_list[0])
# criteria = purchase_deadline / math.e
# if day_number > criteria:
#   if min(price) == price[-1]:
#     print("You should buy this product")
# elif min(price) == price[-1]:
#   print(" you may buy this product")
# else:
#   print("you should not buy ths product")