import matplotlib.pyplot as plt
import numpy as np

with open("../data/hoge-date.txt") as f:
  lines = f.readlines()
  s_lines = [line.strip() for line in lines]
  today = s_lines[-1]
  
with open("../data/hoge-price.txt") as file:
  lines = file.readlines()
  s_lines = [line.strip() for line in lines]
  today_price = s_lines[-1]    

date_x_axis = ["12/01", "12/02", "12/03", today]
price_y_axis = [20, 50, 40, int(today_price)]
plt.plot(date_x_axis, price_y_axis)
plt.title("Price Transition")
plt.show()