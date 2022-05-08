# Stanley Gao
# 5/8/22
# quick script to collapse data for vis2

import csv
from statistics import fmean, median

rows = []
with open("Sample - Superstore.csv", 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        rows.append(row)

profit_dict = {}  # entry: SUBCATEGORY: [PROFIT_LIST]

subcat_idx = header.index('Sub-Category')
profit_idx = header.index('Profit')

for row in rows:
  if row[subcat_idx] in profit_dict:
    profit_dict[row[subcat_idx]].append(float(row[profit_idx]))
  else:
    profit_dict[row[subcat_idx]] = [float(row[profit_idx])]


profit_dict2 = {} # entry: SUBCATEGORY: [TOTAL_PROFIT, PROFIT_COUNT, MEAN_PROFIT, MEDIAN_PROFIT]

for subcat in profit_dict:
  profits = profit_dict[subcat]
  total = sum(profits)
  count = len(profits)
  mean_ = fmean(profits)
  median_ = median(profits)
  profit_dict2[subcat] = [total, count, mean_, median_]

# convert back to CSV
new_header = ['Sub-Category', 'Total Profit', 'Count', 'Mean Profit', 'Median Profit']
with open('vis2.csv', 'w', newline="") as file:
  csvwriter = csv.writer(file)
  csvwriter.writerow(new_header)
  for subcat in profit_dict2:
    data = [subcat] + profit_dict2[subcat]
    csvwriter.writerow(data)
  