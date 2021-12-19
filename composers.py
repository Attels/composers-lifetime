import pandas as pd

df = pd.read_csv("./Composers_by_nationality_Michael_Goncharov.csv")

#FIXING DATES
df.loc[df["name"]=="Fryderyk Chopin", "date_of_birth"] = "1810"
df.loc[df["name"]=="Fryderyk Chopin", "date_of_death"] = "1849"


composers_list = [
    "Dmitri Shostakovich",
    "Igor Stravinsky",
    "Alexander Scriabin",
    "Schnittke",
    "Robert Schumann",
    "Johannes Brahms",
    "Beethoven",
    "Rachmaninoff",
    "Sergei Prokofiev",
    "Mahler",
    "Schubert",
    "List",
    "Liszt",
    "Richard Wagner",
    "Richard Strauss",
    "Arnold Schoenberg",
    "Ilyich Tchaikovsky",
    "Chopin",
    "Sebastian Bach",
    "Wolfgang Amadeus Mozart",
    "Handel",
    "Franz Joseph Haydn"
]

def composers_search(composers_list):
    comp_str = ""
    for i in composers_list:
        comp_str+=i+"|"
    comp_str = comp_str[:-1]
    return comp_str

df_filtered = df[df.name.str.contains(composers_search(composers_list))]
print(df_filtered.to_string())

df_final = df_filtered.dropna()
df_final = df_final[df_final["date_of_death"].str.isnumeric()]
df_final = df_final[["name", "date_of_birth", "date_of_death"]]
df_final["date_of_birth"] = df_final["date_of_birth"].astype(str)
df_final["date_of_death"] = df_final["date_of_death"].astype(str)
df_final = df_final.sort_values(by=['date_of_birth'])

import plotly.express as px

fig = px.timeline(df_final, x_start="date_of_birth", x_end="date_of_death", y="name")
fig.update_yaxes(autorange="reversed") # otherwise tasks are listed from the bottom up
fig.show()



df_final_2 = df_final.set_axis(["Task", "Start", "Finish"], axis='columns', inplace=False)
df_final_2.head()


import plotly.figure_factory as ff
fig = ff.create_gantt(df_final_2)

fig.show()


import plotly.io as pio
pio.write_html(fig, file='index.html', auto_open=True)
