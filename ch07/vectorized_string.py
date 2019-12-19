#%%
import pandas as pd
import numpy as np

data = {'Dave': 'dave@google.com', 
        'Steve': 'steve@gmail.com',
        'Rob': 'rob@gmail.com',
        'Wes': np.nan}

data = pd.Series(data)
data

# %%
data.isnull()

# %%
data.str.contains('gmail')

# %%
import re

pattern = r'([A-Z0-9._%+-]+)@([A-Z0-9.-]+)\.([A-Z]{2,4})'
data.str.findall(pattern, flags=re.IGNORECASE)

# %%
matches = data.str.match(pattern, flags=re.IGNORECASE)
matches

# %%
data.str[:5]

# %%
