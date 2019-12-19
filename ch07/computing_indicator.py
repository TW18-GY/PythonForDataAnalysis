#%%
import pandas as pd

df = pd.DataFrame({'key': ['b','b','a','c','a','b'],
                   'data1': range(6)})
pd.get_dummies(df['key'])

# %%
df

# %%
dummies = pd.get_dummies(df['key'], prefix='key')
df_with_dummy = df[['data1']].join(dummies)
df_with_dummy

# %%
import numpy as np

np.random.seed(12345)
values = np.random.rand(10)
values

# %%
bins = [0, 0.2, 0.4, 0.6, 0.8, 1]
pd.get_dummies(pd.cut(values, bins))