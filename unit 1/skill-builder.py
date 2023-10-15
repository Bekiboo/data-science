# %% package import
import numpy as np
import pandas as pd
import altair as al

# data import
dat = pd.read_csv("https://vincentarelbundock.github.io/Rdatasets/csv/AER/Guns.csv")

# %%
adat = dat.drop(columns=["rownames"])
# %%
bdat = dat.query("state == 'Idaho'")
# %%
bdat = bdat.assign(murder_to_violent=dat.murder / dat.violent)
bdat

# %%
# make a scatterplot
# dat.plot(kind='scatter', x='murder', y='violent')
(
    al.Chart(bdat)
    .encode(
        x=al.X("murder", scale=al.Scale(zero=False)),
        y=al.Y("violent", scale=al.Scale(zero=False)),
        tooltip=["year", "murder", "prisoners", "male", "state"],
    )
    .mark_circle()
)
# %%
states = ["Idaho", "Utah", "Oregon"]

cdat = dat.query("state in @states")

(
    al.Chart(cdat)
    .encode(x=al.X("year", axis=al.Axis(format="d")), y="prisoners", color="state")
    .mark_line()
    .properties(title="Prisoner number in the three states")
)
# %%
