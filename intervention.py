import csv 
import random as r
import statistics as st
import plotly.figure_factory as pf
import plotly.graph_objects as pg
import pandas as p
df = p.read_csv("data1.csv")
data = df["Math_score"].tolist()
mean = st.mean(data)
sd = st.stdev(data)
print(mean)
print(sd)
figure = pf.create_distplot([data],["Math_score"],show_hist = False)
figure.show()