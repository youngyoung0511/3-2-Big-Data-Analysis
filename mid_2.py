
import pandas as pd
import numpy as np

#csv 파일 불러오기
data = pd.read_csv("kbo_baseball_test.csv")


data["Rating"] = data["Win"] / (data["Win"] + data["Lose"])
b = data.sort_values(by="Rating", ascending=False)
print("Top 5 of Winning Percentage")

for i in range(0,5):
    print("{}, {}".format(b["Team"].iloc[i], b["Rating"].iloc[i]))
