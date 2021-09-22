import codecademylib
import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')

print(ad_clicks.head())

print(ad_clicks.groupby('utm_source').user_id.count())

ad_clicks['is_click'] = ~ad_clicks['ad_click_timestamp'].isnull()
print(ad_clicks)

clicks_by_source = ad_clicks.groupby(['utm_source', 'is_click']).user_id.count().reset_index()
print(clicks_by_source)


clicks_pivot = clicks_by_source.pivot(
  columns = 'is_click',
  index = 'utm_source',
  values = 'user_id'
)

clicks_pivot['percent_clicked'] = clicks_pivot[True] / (clicks_pivot[True] + clicks_pivot[False] 
) * 100
print(clicks_pivot)

print(ad_clicks.groupby('experimental_group').user_id.count())

print(ad_clicks.groupby(['experimental_group', 'is_click']).user_id.count().reset_index())


a_clicks = ad_clicks[ad_clicks['experimental_group'] == 'A']
b_clicks = ad_clicks[ad_clicks['experimental_group'] == 'B']
print(a_clicks)


a_click_by_day = a_clicks.groupby(['is_click','day']).user_id.count().reset_index()
b_click_by_day = b_clicks.groupby(['is_click','day']).user_id.count().reset_index()

p_a_click_by_day = a_click_by_day.pivot(
  columns = 'is_click',
  index = 'day', 
  values = 'user_id'
).reset_index()

p_b_click_by_day = b_click_by_day.pivot(
  columns = 'is_click',
  index = 'day', 
  values = 'user_id'
).reset_index()

print(p_a_click_by_day)
print(p_b_click_by_day)
