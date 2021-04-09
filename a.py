# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import altair as alt
import numpy as np
import pandas as pd

# 0 is undrafted
# 1 is drafted
df = pd.DataFrame(
        [
            [27, 4 + 72, 186, 'Undrafted'],
            [28, 7 + 72, 215, 'Undrafted'],
            [23, 7 + 72, 210, 'Undrafted'],
            [28, 7 + 72, 230, 'Undrafted'],
            [23, 6 + 72, 227, 'Undrafted'],
            [21, 3 + 72, 190, 'Undrafted'],
            [31, 3 + 72, 210, 'Undrafted'],
            [25, 0 + 72, 180, 'Undrafted'],
            [22, 6 + 72, 190, 'Undrafted'],
            [24, 5 + 72, 185, 'Undrafted'],
            [25, 8 + 72, 235, 'First Round'],
            [24, 0 + 72, 185, 'First Round'],
            [21, 5 + 72, 215, 'First Round'],
            [30, 8 + 72, 220, 'First Round'],
            [29, 6 + 72, 214, 'First Round'],
            [27, 10 + 72, 279, 'First Round'],
            [37, 6 + 72, 215, 'First Round'],
            [29, 7 + 72, 210, 'First Round'],
            [21, 3 + 72, 181, 'First Round'],
            [28, 10 + 72, 253, 'First Round'],
        ],
    columns=["age", "height (inches)", "weight (pounds)", "draft"],
)


# %%
alt.Chart(df).mark_point().encode(
    x=alt.X(
        "age",
        scale=alt.Scale(
            domain=[20, 32],
        ),
    ),
    y=alt.Y(
        "height (inches)",
        scale=alt.Scale(
            domain=[70, 85],
        ),
    ),
    color="draft",
).interactive()

# %%

# %%
