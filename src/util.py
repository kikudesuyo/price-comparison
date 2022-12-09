from pathlib import Path
from urllib import request

def generate_path(path):
    """絶対パスを生成する

    Args:
      path (str): locator/からの絶対パス

    Return:
        str: 引数pathへの絶対パス
    """
    return str(Path(__file__).parents[1]) + path


def read_csv(name):
  path = generate_path("/data/hoge.csv")
  with open(path, 'r') as data:
    dates = []
    prices = []
    for line in data:
      [date, price] = line.split(',')
      dates.append(date)
      prices.append(price)       
  return [dates, prices]

