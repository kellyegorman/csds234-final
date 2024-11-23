import pandas as pd

def parse_amazon_meta(filepath):
    data = []
    with open(filepath, 'r') as file:
        current_item = {}
        for line in file:
            line = line.strip()
            if line.startswith("Id:"):
                if current_item: 
                    data.append(current_item)
                    current_item = {}
                current_item['Id'] = line.split(":", 1)[1].strip()
            elif line.startswith("ASIN:"):
                current_item['ASIN'] = line.split(":", 1)[1].strip()
            elif line.startswith("title:"):
                current_item['title'] = line.split(":", 1)[1].strip()
            elif line.startswith("group:"):
                current_item['group'] = line.split(":", 1)[1].strip()
            elif line.startswith("salesrank:"):
                current_item['salesrank'] = line.split(":", 1)[1].strip()
            elif line.startswith("categories:"):
                current_item['categories'] = int(line.split(":", 1)[1].strip())
            elif line.startswith("reviews:"):
                current_item['reviews'] = line.split(":", 1)[1].strip()
        if current_item:
            data.append(current_item)
    return pd.DataFrame(data)

# parse
filepath = '/Users/kellyg/csds234-proj/amazon-meta.txt'
df = parse_amazon_meta(filepath)
print(df.head())

initial_non_nan_values = df.count().sum()
#drop NaN
df_cleaned = df.dropna()
final_non_nan_values = df_cleaned.count().sum()
print(f"number of non-null products: {final_non_nan_values}")
