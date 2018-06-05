import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
pd.core.common.is_list_like = pd.api.types.is_list_like
import pandas_datareader.data as web

style.use('ggplot')

#start = dt.datetime(2015, 1, 1)
#end = dt.datetime.now()
#df = web.DataReader("TSLA", 'morningstar', start, end)
#df.reset_index(inplace=True)
#df.set_index("Date", inplace=True)
#df = df.drop("Symbol", axis=1)
#df.to_csv('tsla.csv')

df = pd.read_csv('tsla.csv', parse_dates=True, index_col=0)


df['100ma'] = df['Close'].rolling(window=100, min_periods=0).mean()
df.dropna(inplace=True)

print(df.head())

ax1 = plt.subplot2grid((6,1),(0,0),rowspan=5,colspan=1)
ax2 = plt.subplot2grid((6,1),(0,0),rowspan=5,colspan=1,sharex=ax1)

ax1.plot(df.index, df['Close'])
ax1.plot(df.index, df['100ma'])
ax2.bar(df.index, df['Volume'])

plt.show()