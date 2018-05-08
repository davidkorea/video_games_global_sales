import pandas as pd
import matplotlib.pyplot as plt

def main():
    data_df = pd.read_csv('./Beijing_PM.csv')
    cln_data_df = data_df.dropna()
    cln_data_df['diff'] = abs(cln_data_df['PM_China'] - cln_data_df['PM_US'])

    # diff > 10
    diff10 = cln_data_df.sort_values('diff',ascending=False).head(10)
    print(diff10)
    diff10.plot(kind='bar',x='year',y='diff')
    plt.title('TOP 10 diff')
    plt.tight_layout()
    plt.show()

    # groupby year
    grouped_year_mean = cln_data_df.groupby('year')[ ['PM_China','PM_US'] ].mean()
    print(grouped_year_mean)
    grouped_year_mean.plot.bar()
    plt.title('China VS US PM2.5')
    plt.tight_layout()
    plt.show()
    
main()