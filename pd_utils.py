import pandas as pd

def utils(DATA_FILE):
    data_df = pd.read_csv(DATA_FILE)
    print('rows: {}, columns: {}'.format(data_df.shape[0], data_df.shape[1]))
    print('*-' * 30)
    print('===== DataPreview =====')
    print(data_df.head())
    print('*-' * 30)
    print('===== BasicInfo =====')
    print(data_df.info())
    print('*-' * 30)
    print('===== DataStatistic =====')
    print(data_df.describe())
