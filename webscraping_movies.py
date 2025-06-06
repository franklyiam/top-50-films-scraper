# Importing Libraries
import requests
import sqlite3
import pandas as pd
from bs4 import BeautifulSoup

# Initialization of known entities
url = 'https://web.archive.org/web/20230902185655/https://en.everybodywiki.com/100_Most_Highly-Ranked_Films'
db_name = 'Movies.db'
table_name = 'Top_50'
csv_path = './top_50_films.csv'
df = pd.DataFrame(columns=["Average Rank","Film","Year"])
count = 0

# Loading the webpage for Webscraping
html_page = requests.get(url).text
data = BeautifulSoup(html_page, 'html.parser')

# Scraping of required information
# The rows of the table needed can be accessed using the find_all() function with the BeautifulSoup object 
tables = data.find_all('tbody')
rows = tables[0].find_all('tr')

# tables gets the body of all the tables in the web page and the variable rows gets all the rows of the first table.
# iterate over the rows to find the required data
for row in rows:
    if count<50:
        col = row.find_all('td')
        if len(col)!=0:
            data_dict = {"Average Rank": col[0].contents[0],
                         "Film": col[1].contents[0],
                         "Year": col[2].contents[0]}
            df1 = pd.DataFrame(data_dict, index=[0])
            df = pd.concat([df,df1], ignore_index=True)
            count+=1
    else:
        break

# Print the contents of the dataframe
print(df)

# Storing the data - dataframe has been created, save it to a CSV file
df.to_csv(csv_path)

# To store the required data in a database, initialize a connection to the database, save the dataframe as a table, and then close the connection
conn = sqlite3.connect(db_name)
df.to_sql(table_name, conn, if_exists='replace', index=False)
conn.close()


