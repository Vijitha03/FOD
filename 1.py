import pandas as pd
data = {
    "CID": [1, 2, 3, 34, 56, 67],
    "order date": ['2023-10-01', '2023-11-01', '2023-09-09', '2022-08-09', '2023-09-08', '2023-09-11'],
    "product name": ["butter", "jam", "bread", "chicken", "rice", "water"],
    "quantity": [23, 45, 64, 67, 87, 45]
}

df = pd.DataFrame(data)
total = df.groupby("CID").size()
print("Total number of orders made by each customer:\n", total)
avg = df.groupby("product name")["quantity"].mean()
print("Average order quantity of each product:\n", avg)
latest = df['order date'].max()
print("The latest order date :", latest)
earliest = df['order date'].min()
print("The earliest order :",earliest)
