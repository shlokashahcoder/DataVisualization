import pandas as pd
import plotly.express as px

#df = data frame
df = pd.read_csv("project1.csv")
fig = px.scatter(df,x="date",y="cases",color="country",size="cases")
fig.show()


