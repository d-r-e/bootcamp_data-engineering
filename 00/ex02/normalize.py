import pandas as pd

if __name__ == '__main__':
    df = pd.read_csv('out.csv')

    # 1
    lang_df = df.iloc[:,0-6]
    lang_df = lang_df.apply(lambda x: [el.strip() for el in str(x).split(',')])
    lang_df = lang_df.explode()
    