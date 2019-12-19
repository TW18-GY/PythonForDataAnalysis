#%%
import pandas as pd
import numpy as np

df = pd.DataFrame(np.arange(5 * 4).reshape((5, 4)))
sampler = np.random.permutation(5)

sampler

# %%
df

# %%
df.take(sampler)

# %%
df.sample(n=3)

# %%
choices = pd.Series([5, 7, -1, 6, 4])
draws = choices.sample(n=10, replace=True)
draws