import pandas as pd
import datetime
import re


# 1
def df_nan_filter(df):
    """Apply filters on NaN values
    Args:
        df: pandas dataframe.
    Returns:
        Filtered Dataframe.
    Raises:
        This function shouldn't raise any Exception.
    """
    df.dropna(subset=['Size'], inplace=True)
    df['Languages'].fillna(value="EN", inplace=True)
    df['Price'].fillna(value=0.0, inplace=True)
    avg = df['Average User Rating'].notna().mean()
    df['Average User Rating'].fillna(value=avg, inplace=True)
    df['User Rating Count'].fillna(value=1, inplace=True)
    return df


# 2
def change_date_format(date: str):
    """Change date format from dd/mm/yyyy to yyyy-mm-dd
    Args:
        date: a string representing the date.
    Returns:
        The date in the format yyyy-mm-dd.
    Raises:
        This function shouldn't raise any Exception.
    """
    try:
        newdate = datetime.datetime.strptime(date, '%d/%m/%Y')
        newdate = newdate.strftime('%Y/%m/%d')
        return newdate
    except():
        return date


def string_filter(s: str):
    """Apply filters in order to clean the string.
    Args:
      s: string.
    Returns:
      Filtered String.
    Raises:
      This function shouldn't raise any Exception.
    """
    # filter : \\t, \\n, \\U1a1b2c3d4, \\u1a2b, \\x1a
    # turn \' into '
    # replace remaining \\ with \
    # turn multiple spaces into one space
    s = re.sub(r'''\\+(t|n|U[a-z0-9]{8}|u[a-z0-9]{4}|x[a-z0-9]{2}|[\.]{2})''', ' ', s)
    s = s.replace('\\\'', '\'').replace('\\\\', '\\')
    s = re.sub(r' +', ' ', s)
    return (s)


if __name__ == '__main__':
    df = pd.read_csv('../appstore_games.csv')
    # 1
    dff = df_nan_filter(df)
    # 2
    dff["Original Release Date"] = dff["Original Release Date"].apply(lambda x: change_date_format(x))
    # 3
    dff["Description"] = dff["Description"].apply(lambda x: string_filter(x))
    # 4
    dff.drop_duplicates(subset=df.columns[0], inplace=True)
    # 5
    dff['Age Rating'] = dff['Age Rating'].apply(lambda x: re.findall(r'\d+', x)[0] )
    dff['User Rating Count'] = pd.to_numeric(dff['User Rating Count'], downcast='integer')
    dff['Size'] = pd.to_numeric(dff['Size'], downcast='integer')
    # 6
    indexNames = dff[ dff['Name'].apply(len) < 4 ].index
    dff.drop(indexNames, inplace=True)
    dff.to_csv('out.csv')
