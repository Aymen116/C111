import csv 
import pandas as p
import statistics as st
import plotly.figure_factory as pf
import plotly.graph_objects as pg
import random as r
df = p.read_csv("data3.csv")
data = df["Math_score"].tolist()
mean = st.mean(data)
sd = st.stdev(data)
print(mean)
print(sd)
figure = pf.create_distplot([data],["Math_score"],show_hist = False)
figure.show()