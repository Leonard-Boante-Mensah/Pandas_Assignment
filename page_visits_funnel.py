import codecademylib
import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])

print(visits.head())
print(cart.head())
print(checkout.head())
print(purchase.head())

visits_cart = pd.merge(visits, cart, how='left')
print(visits_cart.head())
print(len(visits_cart))

num_rows_visits_cart = len(visits_cart)
print(num_rows_visits_cart)

cart_null = visits_cart[visits_cart.cart_time.isnull()]
print(len(cart_null))

print(float(len(cart_null))/num_rows_visits_cart)

cart_checkout = pd.merge(cart, checkout, how='left')
print(cart_checkout.head())

num_rows_cart_checkout = len(cart_checkout)
print(num_rows_cart_checkout)

cart_checkout_null = cart_checkout[cart_checkout.checkout_time.isnull()]
print(len(cart_checkout_null))

print(float(len(cart_checkout_null))/num_rows_cart_checkout)

all_data = visits\
  .merge(cart, how='left')\
  .merge(checkout, how='left')\
  .merge(purchase, how='left')

print(all_data.head())

checkout_purchase = pd.merge(checkout, purchase, how='left')
print(checkout_purchase.head())

percentage_checkout_no_purchase = float(len(checkout_purchase[checkout_purchase.purchase_time.isnull()])) / (len(checkout_purchase))

print('{}%'.format(round(percentage_checkout_no_purchase * 100), 2))
# print("{}%".format(percentage_checkout_no_purchase))

all_data['time_to_purchase'] = \
    all_data.purchase_time - \
    all_data.visit_time

print(all_data.head())

print(all_data.time_to_purchase)

print(all_data.time_to_purchase.mean())