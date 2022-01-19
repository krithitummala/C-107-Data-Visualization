import csv
import pandas as pd
import plotly.graph_objects as go
import plotly_express as px

df = pd.read_csv("data.csv")
students = df.groupby(["student_id","level"], as_index= False)["attempt"].mean()
print(students)
fig = px.scatter(students, x = "student_id", y = "level", color = "attempt", size = "attempt")
fig.show()