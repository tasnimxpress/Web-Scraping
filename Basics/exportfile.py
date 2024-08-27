# Basics to Start Web Scraping
import pandas as pd

list_a = ['A', 'B', 'C', 'D']
list_b = [2, 5, 1, 8]

list_dict = {'a': list_a, 'b': list_b}

# Method one to export data
with open('Basics/data.txt', 'w') as file:
    file.write('File scraped successfully')


# Method two to export data with pandas
df_list = pd.DataFrame.from_dict(list_dict)
# convert the dataframe to a csv file - to remove the index number we can make it false
df_list.to_csv("Basics/data.csv", index=False)
print(df_list)
