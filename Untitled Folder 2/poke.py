import numpy as np
import pandas as pd
import re
import justpy as jp

data = pd.read_csv("pokemon.txt", delimiter = "\t")

#read rows
#data.iloc[1:4]

#read a specific location
#data.iloc[2,3]

#for index, row in data.iterrows():
   # print(index, row["Name"])

#data.loc[data["Type 1"] == "Fire"]

#data.describe()

data["Total"] = data.iloc[:, 4:10].sum(axis = 1)

#this makes the column Total go to the front
columns = list(data.columns.values)
data = data[columns[0:4] + [columns[-1]] + columns[4:12]]

#removes the names containing Mega
data.loc[~data["Name"].str.contains("Mega")]

#filters data
#new_data = data.loc[(data["Type 1"]== "Fire") & (data["Type 2"] == "Flying")]
#new_data = new_data.reset_index(drop = True)
#new_data.to_csv("Filtered_data.csv")


#data.loc[data["Type 1"].str.contains("Water|Psychic", regex= True)]

#grouping by stats
datagroup = data.groupby(["Type 1"]).mean().sort_values("Attack", ascending = False)



chart_definition = """{
    chart: {
        type: 'cylinder',
        options3d: {
            enabled: true,
            alpha: 15,
            beta: 15,
            depth: 50,
            viewDistance: 25
        }
    },
    title: {
        text: 'Pokemon Power Level by type - Cylinder Chart'
    },
    plotOptions: {
        series: {
            depth: 25,
            colorByPoint: true
        }
    },
    series: [{
        data: [29.9, 71.5, 106.4, 129.2, 144.0, 176.0, 135.6, 148.5, 216.4, 194.1, 95.6, 54.4],
        name: 'Avg Power Level',
        showInLegend: false
    }]
    }
    """

#if we want to have full info
def app():
    page = jp.QuasarPage()
    head = jp.QDiv(a = page, text = "Pokemon Analysis", classes = "text-h1 text-center q-pa-md")
    highc = jp.HighCharts(a = page, options = chart_definition)

    highc.options.series[0].data = list(zip(datagroup.index, data["Total"]))
    #highc.options.series[0].name = list(zip(datagroup.index, data["Type 1"]))

    return page


jp.justpy(app)