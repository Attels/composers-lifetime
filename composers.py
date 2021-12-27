import pandas as pd

df = pd.read_csv("./Composers_by_nationality_Michael_Goncharov.csv")

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
    "Fryderyk Chopin",
    "Sebastian Bach",
    "Wolfgang Amadeus Mozart",
    "Handel",
    "Franz Joseph Haydn",
    "Arvo Pärt",
    "Jean Sibelius",
    "Giuseppe Verdi",
    "Antonín Dvořák",
    "Claude Debussy",
    "Erik Satie",
    "Krzysztof Penderecki",
    "Gioacchino Rossini",
    "Christoph Willibald Gluck",
    "Rimsky-Korsakov",
    "Mikhail Glinka",
    "Alexander Borodin",
    "Modest Mussorgsky",
    "Antonio Vivaldi",
    "Niccolò Paganini"
]

def composers_search(composers_list):
    comp_str = ""
    for i in composers_list:
        comp_str+=i+"|"
    comp_str = comp_str[:-1]
    return comp_str

df_filtered = df[df.name.str.contains(composers_search(composers_list))]

df_final = df_filtered.dropna()
df_final = df_final[df_final["date_of_death"].str.isnumeric()]
df_final = df_final[["name", "date_of_birth", "date_of_death"]]
df_final["date_of_birth"] = df_final["date_of_birth"].astype(str)
df_final["date_of_death"] = df_final["date_of_death"].astype(str)
df_final = df_final.sort_values(by=['date_of_birth'])

# import plotly.express as px

# fig = px.timeline(df_final, x_start="date_of_birth", x_end="date_of_death", y="name")
# fig.update_yaxes(autorange="reversed") # otherwise tasks are listed from the bottom up
# fig.show()

df_final_2 = df_final.set_axis(["Task", "Start", "Finish"], axis='columns', inplace=False)

import plotly.figure_factory as ff
fig = ff.create_gantt(df_final_2, 
                    bar_width = 0.3,
                    height = 900,
                    title = "Composers lifetime")

fig.show()

import plotly.io as pio
pio.write_html(fig, file='index.html', auto_open=True)
