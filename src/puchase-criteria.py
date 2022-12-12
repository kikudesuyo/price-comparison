import math
from util import read_data, evaluate_product

"""秘書問題を基に作成"""
filename_list = read_data()
for i in filename_list:
  print("Product name is : " + i)
  evaluate_product(i)