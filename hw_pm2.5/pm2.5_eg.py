# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt


# 读取csv数据文件
data_df = pd.read_csv('./Beijing_PM.csv')

# 1. 处理空值记录
data_df.dropna(inplace=True)

# 2. 为数据添加列
data_df['diff'] = data_df['PM_China'] - data_df['PM_US']

# 3. 进行绝对值操作
data_df['diff'] = data_df['diff'].abs()

# 4. 数据排序
top_10_diff = data_df.sort_values(by='diff', ascending=False).head(10)
print('相差最大的10条记录：')
print(top_10_diff)

# 5. 绘制分组柱状图
year_average_pm = data_df.groupby('year')[['PM_China', 'PM_US']].mean()
year_average_pm.plot(kind='bar')
plt.tight_layout()
plt.show()
