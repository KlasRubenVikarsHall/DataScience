from database import engine, Base
import models
import pandas as pd
import numpy as np



# df = pd.read_csv("world_population_by_country_2026.csv")

query = "SELECT * FROM world_population" # Exports entire 
data = pd.read_sql(query, con=engine)

data.columns = data.columns.str.lower()
print(data.columns)

data.to_sql(
    name="world_population",   # table name in postgres
    con=engine,
    if_exists="replace",       # or "append" / "fail"
    index=False,
)

print(pd.read_sql("SELECT Country FROM world_population WHERE Migrants_Net > 0", con=engine))
