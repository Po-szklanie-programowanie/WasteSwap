import pandas as pd

data = pd.read_csv('openfoodfacts_export.csv', sep="\t")

print(list(data.columns))

new_data = data[['product_name_en', 'packaging_tags', 'categories_tags']]

print(new_data.head())