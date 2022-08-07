import pandas
import json

# Open the CSV file and convert it into a pandas dataframe
df = pandas.read_csv('combined_csv.csv')

# Convert the csv file's contents into  data into a json file
df.to_json("deals.json", orient='records')

# Fill null values with an empty string
df.fillna('', inplace=True)

# Optional output to console
print(df)

# update the dataframe contents to the json file
with open("deals.json", "w") as f:
    json.dump({'deals': df.to_dict(orient='records')}, f, indent=4)


