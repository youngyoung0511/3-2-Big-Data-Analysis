#20221333 김서영
#Assignment 1-2

import numpy as np
import pandas as pd

x = np.arange(62500)

x = x.reshape(10, 10, 625)  # 10x10x625로 reshape.
x_avg = np.mean(x, axis=2)  # depth(625) 차원을 따라 평균냄.
df = pd.DataFrame(x_avg)  # DataFrame으로 변환한다.
df.to_csv('test.csv', index=False, header=False)  # 'test.csv' 파일명으로 저장한다.

