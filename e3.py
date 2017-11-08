#!/usr/bin/env python

import pandas as pd
lines = []
for line in open("ELECTION_ID.txt", "r"):
    lines.append(line.split()[0])

lines.reverse()

dictionary = {}
counties = ["Accomack County","Albemarle County","Alexandria City","Alleghany County"]

for x in counties:
    dictionary[x] = {"year" : [], "vote_share" : []}

for i in lines:

    file_name = "year" + i + ".csv"
    header = pd.read_csv(file_name, nrows = 1).dropna(axis = 1)
    d = header.iloc[0].to_dict()
    df = pd.read_csv(file_name, index_col = 0, thousands = ",", skiprows = [1])
    df.rename(inplace = True, columns = d)
    df.dropna(inplace = True, axis = 1)
    df["year"] = int(i)
    df["vote_share"] = df["Republican"] /df["Total Votes Cast"]

    for x in counties:
        if x in df.index:
            dictionary[x]["year"].append(int(i))
            dictionary[x]["vote_share"].append(df.loc[x]["vote_share"])

for x in counties:
    df = pd.DataFrame(dictionary[x])
    graph = df.plot(x="year", y="vote_share")
    graph.figure.savefig(x.lower().replace(" ", "_") + ".pdf")
