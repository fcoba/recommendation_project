import pandas as pd
df = pd.read_csv("data/users.dat", delimiter=":")
df = df.drop(columns=["Unnamed: 1", "Unnamed: 3", "Unnamed: 5", "Unnamed: 7"])
df.columns=["id", "gender", "age", "occupation", "zipcode"]

age_map = {
1:  "Under 18",
18:  "18-24",
25:  "25-34",
35:  "35-44",
45:  "45-49",
50:  "50-55",
56:  "56+" 
}

occupation_map = {
0:  "other",
1:  "academic/educator",
2:  "artist",
3:  "clerical/admin",
4:  "college/grad student",
5:  "customer service",
6:  "doctor/health care",
7:  "executive/managerial",
8:  "farmer",
9:  "homemaker",
10:  "K-12 student",
11:  "lawyer",
12:  "programmer",
13:  "retired",
14:  "sales/marketing",
15:  "scientist",
16:  "self-employed",
17:  "technician/engineer",
18:  "tradesman/craftsman",
19:  "unemployed",
20:  "writer"
}

df['age'] = df['age'].apply(lambda x: age_map[x])
df['occupation'] = df['occupation'].apply(lambda x: occupation_map[x])

####  Now import movies.dat and export as csv

df = pd.read_csv("data/movies.dat", delimiter="::")
df.columns = ['movie_id', 'title', 'genres']
df.to_csv("data/movies.csv")