#%%
val = 'a,b,     guido'
val.split(',')

# %%
pieces = [x.strip() for x in val.split(',')]
pieces

# %%
first, second, third = pieces
first + '::' + second + '::' + third

# %%
'::'.join(pieces)