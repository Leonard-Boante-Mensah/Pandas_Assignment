import codecademylib
import pandas as pd

inventory = pd.read_csv('inventory.csv')

# print(inventory.head(10))

staten_island = inventory.head(10)
product_request = staten_island['product_description']
# print(product_request)

inventory['in_stock'] = inventory.apply(lambda x: True if x['quantity'] > 0 else False, axis = 1)
# print(inventory.head())

inventory['total_value'] = inventory.price * inventory.quantity

combine_lambda = lambda row: \
    '{} - {}'.format(row.product_type,
                     row.product_description)

inventory['full_description'] = inventory.apply(combine_lambda, axis=1)

print(inventory.head())