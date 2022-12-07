import matplotlib.pyplot as plt
import numpy as np

with open("../temp/hoge-date.txt") as f:
  lines = f.readlines()
  s_lines = [line.strip() for line in lines]
  today = s_lines[-1]
  
with open("../temp/hoge-price.txt") as file:
  lines = file.readlines()
  s_lines = [line.strip() for line in lines]
  today_price_data = s_lines[-1]    

data_x_axis = ["12/01", "12/02", "12/03", today]
price_y_axis = [20, 50, 40, int(today_price_data)]
plt.plot(data_x_axis, price_y_axis)
plt.title("Price Transition")
plt.show()
