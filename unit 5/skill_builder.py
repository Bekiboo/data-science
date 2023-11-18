# %%
import pandas as pd
import altair as alt
import numpy as np

url = "https://github.com/fivethirtyeight/data/raw/master/star-wars-survey/StarWars.csv"


dat_names = pd.read_csv(url, encoding="ISO-8859-1", nrows=1).melt()
dat = pd.read_csv(url, encoding="ISO-8859-1", skiprows=2, header=None)

column_mapping = {
    "RespondentID": "RespondentID",
    "Have you seen any of the 6 films in the Star Wars franchise?": "Seen_any",
    "Do you consider yourself to be a fan of the Star Wars film franchise?": "Fan",
    "Which of the following Star Wars films have you seen? Please select all that apply.": "Seen_Episodes",
    "Please rank the Star Wars films in order of preference with 1 being your favorite film in the franchise and 6 being your least favorite film.": "Ranking",
    "Please state whether you view the following characters favorably, unfavorably, or are unfamiliar with him/her.": "Character_Feelings",
    "Which character shot first?": "Shot_First",
    "Are you familiar with the Expanded Universe?": "EU_Familiarity",
    "Do you consider yourself to be a fan of the Expanded Universe?��": "EU_Fan",
    "Do you consider yourself to be a fan of the Star Trek franchise?": "Star_Trek_Fan",
    "Gender": "Gender",
    "Age": "Age",
    "Household Income": "Income",
    "Education": "Education",
    "Location (Census Region)": "Region",
}

# Rename columns using the mapping dictionary
dat.rename(columns=column_mapping, inplace=True)

# Display the first few rows to verify the changes
print(dat.head())

# %%
# Rename columns using the mapping dictionary
dat.rename(columns=column_mapping, inplace=True)

# Display the cleaned DataFrame
print(dat)
# %%
