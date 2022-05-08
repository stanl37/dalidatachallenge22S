# Stanley Gao
# 5/8/22
# quick script to collapse data for vis1

import csv

rows = []
with open("Sample - Superstore.csv", 'r') as file:
    csvreader = csv.reader(file)
    header = next(csvreader)
    for row in csvreader:
        rows.append(row)


sales_dict = {}  # entry: STATE: TOTAL_SALES_VOL(FLOAT)
profit_dict = {}  # entry: STATE: TOTAL_PROFIT_VOL(FLOAT)

state_idx = header.index('State')

sale_idx = header.index('Sales')
for row in rows:
  if row[state_idx] in sales_dict:
    sales_dict[row[state_idx]] += float(row[sale_idx])
  else:
    sales_dict[row[state_idx]] = float(row[sale_idx])

profit_idx = header.index('Profit')
for row in rows:
  if row[state_idx] in profit_dict:
    profit_dict[row[state_idx]] += float(row[profit_idx])
  else:
    profit_dict[row[state_idx]] = float(row[profit_idx])

# convert back to CSV
new_header = ['statename', 'sales', 'profit']
with open('collapsed_vis1.csv', 'w', newline="") as file:
  csvwriter = csv.writer(file)
  csvwriter.writerow(new_header)
  for state in sales_dict:
    data = [state, sales_dict[state], profit_dict[state]]
    csvwriter.writerow(data)
  