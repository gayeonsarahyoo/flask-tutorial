import pandas as pd
from json import dumps
from datetime import datetime

def get_us_cum_deaths():
    df = pd.read_csv("https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv")
    df = df.loc[df['Country/Region'] == 'US']
    df = df.drop(['Province/State', 'Country/Region', 'Lat', 'Long'], axis=1)
    df.reset_index(drop=True, inplace=True)
    cases_dict = dict()
    for col in df.columns:
        d = datetime.strptime(col, "%m/%d/%y")
        d = d.strftime("%Y-%m-%d")
        cases_dict[d] = str(df.at[0, col])
    return cases_dict
