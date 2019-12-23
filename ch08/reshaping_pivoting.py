#%%
import pandas as pd
import numpy as np

data = pd.DataFrame(np.arange(6).reshape((2, 3)),
                    index=pd.Index(['Ohio', 'Colorado'], name='state'),
                    columns=pd.Index(['one', 'two', 'three'],
                    name='number'))
data                    

# %%
result = data.stack()
result

# %%
result.unstack()

# %%
result.unstack(0)

# %%
result.unstack('state')

# %%
s1 = pd.Series([0, 1, 2, 3], index=['a', 'b', 'c', 'd'])
s2 = pd.Series([4, 5, 6], index=['c', 'd', 'e'])
data2 = pd.concat([s1, s2], keys=['one', 'two'])
data2

# %%
data2.unstack()

# %%
data2.unstack(1)

# %%
df = pd.DataFrame({'left': result, 'right': result + 5},
                  columns=pd.Index(['left', 'right'], name='side'))
df                  

# %%
df.unstack('state')

# %%
df.unstack('state').stack('side')

# %%
data = pd.read_csv('examples/macrodata.csv')
data.head()

# %%
periods = pd.PeriodIndex(year = data.year, quarter=data.quarter, name='date')
columns = pd.Index(['realgdp', 'infl', 'unemp'], name='item')
data = data.reindex(columns=columns)
data.index = periods.to_timestamp('D', 'end')
ldata = data.stack().reset_index().rename(columns={0: 'value'})

# %%
ldata[:10]

# %%
df = pd.DataFrame({'key': ['foo', 'bar', 'baz'],
                   'A': [1, 2, 3],
                   'B': [4, 5, 6],
                   'C': [7, 8, 9]})
df                   

# %%
melted = pd.melt(df, ['key'])
melted

# %%
reshaped = melted.pivot('key', 'variable', 'value')
reshaped

# %%
reshaped.reset_index()

# %%
pd.melt(df, id_vars=['key'], value_vars=['A', 'B'])

# %%
pd.melt(df, value_vars=['A', 'B', 'C'])

# %%
pd.melt(df, value_vars=['key', 'A', 'B'])