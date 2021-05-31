import numpy as np
import pandas as pd
import re
import justpy as jp

data = pd.read_csv("pokemon.txt", delimiter = "\t")

data["Count"] = 1
data.groupby(["Type 1"]).count()
data["Count"] = 1
ind = data.groupby(["Type 1"])["Count"].count()
#for v1, v2 in zip(ind.index, ind):
    #print(v1,v2)
#data.groupby(["Type 1", "Type 2"]).count()
# I tried different methods of grouping using for loop, but the data isn't big enough.
#new_dataa = pd.DataFrame(columns = data.columns)

#for data in pd.read_csv("new_pokemon.csv", chunksize = 6):
    #result = data.groupby(["Type 1"]).count()
    
    #new_dataa = pd.concat([new_dataa, result])


chart_def = """{
  chart: {
    plotBackgroundColor: null,
    plotBorderWidth: null,
    plotShadow: false,
    type: 'pie'
  },
  title: {
    text: 'Pokemon % per type in gen 1'
  },
  tooltip: {
    pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
  },
  accessibility: {
    point: {
      valueSuffix: '%'
    }
  },
  plotOptions: {
    pie: {
      allowPointSelect: true,
      cursor: 'pointer',
      dataLabels: {
        enabled: true,
        format: '<b>{point.name}</b>: {point.percentage:.1f} %'
      }
    }
  },
  series: [{
    name: 'Brands',
    colorByPoint: true,
    data: [{
      name: 'Chrome',
      y: 61.41,
      sliced: true,
      selected: true
    }, {
      name: 'Internet Explorer',
      y: 11.84
    }, {
      name: 'Firefox',
      y: 10.85
    }, {
      name: 'Edge',
      y: 4.67
    }, {
      name: 'Safari',
      y: 4.18
    }, {
      name: 'Sogou Explorer',
      y: 1.64
    }, {
      name: 'Opera',
      y: 1.6
    }, {
      name: 'QQ',
      y: 1.2
    }, {
      name: 'Other',
      y: 2.61
    }]
  }]
  }
  """


def app():
    page = jp.QuasarPage()
    head = jp.QDiv(a = page, text = "Pokemon Analysis", classes = "text-h1 text-center q-pa-md")
    highc = jp.HighCharts(a = page, options = chart_def)


    highc_data = [{"name":v1, "y":v2} for v1,v2 in zip(ind.index, ind)]
    highc.options.series[0].data = highc_data

    return page


jp.justpy(app)