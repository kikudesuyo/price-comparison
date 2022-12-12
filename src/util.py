from pathlib import Path
from urllib import request
import glob
import math
def generate_path(path):
    """絶対パスを生成する

    Args:
      path (str): price-comparison/からの絶対パス

    Return:
        str: 引数pathへの絶対パス
    """
    return str(Path(__file__).parents[1]) + path

def read_csv(product_file):
    """日付と価格を出力
    
    Args:
      procuct_file(str): 対象のファイル
    
    Return:
      dubble_list(list): 日付と値段の2重リスト  
    """
    path = generate_path("/" + product_file)
    with open(path, 'r') as data:
      dates = []
      prices = []
      dubble_list = [dates, prices]
      for line in data:
        [date, price] = line.split(',')
        dates.append(date)
        prices.append(price)  
    return dubble_list

def read_data():
    """dataにある.csvファイルの名前をリスト化"
    Return:
      filename_list(list): e.g.) [desk.csv, laptop,csv]
    
    """
    sloppy_files = glob.glob('data/*.csv')
    filename_list = []
    for data_number in sloppy_files:
      sloppy_files_list = data_number.split("\\")
      sloppy_name = sloppy_files_list[1]
      filename_list.append(sloppy_name)
    return filename_list
  
def evaluate_product(filename):
    """秘書問題をもとに購入するべきか判定
    
    
    Arg:
      filename(str): 商品のファイル名 e.g.) desk.csv
      
    """
    dubble_list = read_csv("data/" + filename)
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
