import matplotlib.pyplot as plt
import numpy as np
from util import read_csv

dubble_list = read_csv("/data/mouse.csv")
today = dubble_list[0]
today_price = dubble_list[1]
today_price = list(map(int, today_price))
plt.plot(today, today_price)
# Price Transition は 商品名を取り出し変更する .csvファイル名から取り出すのが良い気がする
plt.title("Price Transition")
plt.show()