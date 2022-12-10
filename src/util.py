from pathlib import Path
from urllib import request
import re

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
    
    Returns:
        dates(str):
        price(str): 
    """
    path = generate_path("/" + product_file)
    with open(path, 'r') as data:
      dates = []
      prices = []
      for line in data:
        [date, price] = line.split(',')
        dates.append(date)
        prices.append(price)  
    return [dates, prices]