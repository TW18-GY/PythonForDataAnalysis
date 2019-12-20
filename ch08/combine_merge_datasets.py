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

# %%
left2 = pd.DataFrame([[1., 2.], [3., 4.], [5., 6.]],
                     index=['a', 'c', 'e'],
                     columns=['Ohio', 'Nevada'])
left2                     

# %%
right2 = pd.DataFrame([[7., 8.], [9., 10.], [11., 12.], [13, 14]],
                      index=['b', 'c', 'd', 'e'],
                      columns=['Missouri', 'Alabama'])
right2                      

# %%
pd.merge(left2, right2, how='outer', left_index=True, right_index=True)

# %%
left2.join(right2, how='outer')

# %%
another = pd.DataFrame([[7., 8.], [9., 10.], [11., 12.], [16., 17.]],
                       index=['a', 'c', 'e', 'f'],
                       columns=['New York', 'Oregon'])
another                       

# %%
left2.join([right2, another])

# %%
left2.join([right2, another], how='outer')

# %%
arr = np.arange(12).reshape((3, 4))
arr

# %%
np.concatenate([arr, arr], axis=1)

# %%
s1 = pd.Series([0, 1], index=['a', 'b'])
s2 = pd.Series([2, 3, 4], index=['c', 'd', 'e'])
s3 = pd.Series([5, 6], index=['f', 'g'])

pd.concat([s1, s2, s3])

# %%
pd.concat([s1, s2, s3], axis=1)

# %%
s4 = pd.concat([s1, s3])
s4

# %%
pd.concat([s1, s4], axis=1)

# %%
pd.concat([s1, s4], axis=1, join='inner')

# %%
pd.concat([s1, s4], axis=1, join_axes=[['a', 'c', 'b', 'e']])

# %%
result = pd.concat([s1, s2, s3], keys=['one', 'two', 'three'])
result

# %%
result.unstack()

# %%
df1 = pd.DataFrame(np.arange(6).reshape(3, 2), index=['a', 'b', 'c'],
                   columns=['one', 'two'])
df1                   

# %%
df2 = pd.DataFrame(5 + np.arange(4).reshape(2, 2), index=['a', 'c'],
                   columns=['three', 'four'])
df2                   

# %%
pd.concat([df1, df2], axis=1, keys=['level1', 'level2'])

# %%
pd.concat({'level1': df1, 'level2': df2}, axis=1)

# %%
a = pd.Series([np.nan, 2.5, np.nan, 3.5, 4.5, np.nan],
              index=['f', 'e', 'd', 'c', 'b', 'a'])
a              

# %%
b = pd.Series(np.arange(len(a), dtype=np.float64),
              index=['f', 'e', 'd', 'c', 'b', 'a'])
b[-1] = np.nan
b

# %%
np.where(pd.isnull(a), b, a)

# %%
b[:-2].combine_first(a[2:])