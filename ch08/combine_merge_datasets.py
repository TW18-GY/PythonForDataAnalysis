#%%
import pandas as pd

df1 = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
                    'data1': range(7)})
df1                    

# %%
df2 = pd.DataFrame({'key': ['a', 'b', 'd'],
                    'data2': range(3)})
df2                    

# %%
pd.merge(df1, df2)

# %%
pd.merge(df1, df2, on='key')

# %%
df3 = pd.DataFrame({'lkey': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
                    'data1': range(7)})
df3                    

# %%
df4 = pd.DataFrame({'rkey': ['a', 'b', 'd'],
                    'data2': range(3)})
df4                    

# %%
pd.merge(df3, df4, left_on='lkey', right_on='rkey')

# %%
pd.merge(df1, df2, how='outer')

# %%
df1 = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'b'],
                    'data1': range(6)})
df2 = pd.DataFrame({'key': ['a', 'b', 'a', 'b', 'd'],
                    'data2': range(5)})                    

pd.merge(df1, df2, on='key', how='left')                    

# %%
pd.merge(df1, df2, how='inner')

# %%
left = pd.DataFrame({'key1': ['foo', 'foo', 'bar'],
                     'key2': ['one', 'two', 'one'],
                     'lval': [1, 2, 3]})
right = pd.DataFrame({'key1': ['foo', 'foo', 'bar', 'bar'],
                      'key2': ['one', 'one', 'one', 'two'],
                      'rval': [4, 5, 6, 7]})                     
pd.merge(left, right, on=['key1', 'key2'], how='outer')                      

# %%
left1 = pd.DataFrame({'key': ['a', 'b', 'a', 'a', 'b', 'c'],
                      'value': range(6)})
right1 = pd.DataFrame({'group_val': [3.5, 7]}, index=['a', 'b'])

# %%
left1

# %%
right1

# %%
pd.merge(left1, right1, left_on='key', right_index=True)

# %%
pd.merge(left1, right1, left_on='key', right_index=True, how='outer')

# %%
import numpy as np

lefth = pd.DataFrame({'key1': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
                      'key2': [2000, 2001, 2002, 2001, 2002],
                      'data': np.arange(5.)})
righth = pd.DataFrame(np.arange(12).reshape((6, 2)),
                      index=[['Nevada', 'Nevada', 'Ohio', 'Ohio', 'Ohio', 'Ohio'],
                             [2001, 2000, 2000, 2000, 2001, 2002]],
                      columns=['event1', 'event2'])                      

# %%
lefth

# %%
righth

# %%
pd.merge(lefth, righth, left_on=['key1', 'key2'], right_index=True)