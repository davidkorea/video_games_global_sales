import os
import pandas as pd
import matplotlib.pyplot as plt

DATA_FILE = './data_pd/video_games_sales.csv'

def collect_data():
    data_df = pd.read_csv(DATA_FILE)
    return data_df
def inspect_data(data_df):
    print('rows: {}, columns: {}'.format(data_df.shape[0],data_df.shape[1]))
    print('*-' * 30)
    print('===== DataPreview =====')
    print(data_df.head())
    print('*-' * 30)
    print('===== BasicInfo =====')
    print(data_df.info())
    print('*-' * 30)
    print('===== DataStatistic =====')
    print(data_df.describe())

def process_data(data_df):
    cln_data_df = data_df.dropna()

    # filter by year 2005-2017
    condition = (data_df['Year'] >= 2005) & (data_df['Year'] <= 2017)
    filtered_data = cln_data_df[condition]
    filtered_data_df = filtered_data.copy()

    # global sales count
    filtered_data_df['Global_sales'] = filtered_data_df['NA_Sales'] + \
                                       filtered_data_df['EU_Sales'] + \
                                       filtered_data_df['JP_Sales'] + \
                                       filtered_data_df['Other_Sales']

    print('Original Data: {} rows, Filtered Data: {} rows'.format(
        cln_data_df.shape[0],filtered_data_df.shape[0]
    ))
    return filtered_data_df

def analyze_data(filtered_data_df):
    # game name
    top20_games = filtered_data_df.sort_values(by='Global_sales',ascending=False).head(20)
    # game publisher - over 5m 2005-2017 各个游戏厂商销量对比
    over5_data_df = filtered_data_df[filtered_data_df['Global_sales'] > 5]
    grouped_df = over5_data_df.groupby('Publisher')
    sales_comp_results = grouped_df[['NA_Sales','EU_Sales','JP_Sales','Other_Sales']].sum()
    # sales_comp_results 因为要画出堆叠图，所以统计处4个地区的量，堆叠后即为全球销量
    return top20_games,sales_comp_results

def show_results(top20_games,sales_comp_results):
    top20_games.to_csv('./top20_games.csv')
    sales_comp_results.to_csv('./sales_comp_results.csv')

    top20_games.plot(kind='bar',x='Name',y='Global_sales')
    plt.title('top20_games 2005 - 2017')
    plt.tight_layout()
    plt.savefig('./top20_games.png')
    plt.show()

    sales_comp_results.plot.bar(stacked=True)
    # stacked = false 则为grouped bar chart
    plt.title('Game sales comparison')
    plt.tight_layout()
    plt.savefig('./Game sales comparison.png')
    plt.show()



def main():
    data_df = pd.read_csv(DATA_FILE)
    inspect_data(data_df)
    filtered_data_df = process_data(data_df)
    top20_games, sales_comp_results = analyze_data(filtered_data_df)
    show_results(top20_games, sales_comp_results)

main()