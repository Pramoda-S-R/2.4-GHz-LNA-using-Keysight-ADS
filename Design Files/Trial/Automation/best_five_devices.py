import pandas as pd

df = pd.read_excel('transistors.xlsx')

df['NFmin_2.4GHz_Rank'] = df['NFmin at 2.4GHz'].rank()
df['Gain_2.4GHz_Rank'] = df['Gain at 2.4GHz'].rank(ascending=False)
df['NFmin_4GHz_Rank'] = df['NFmin at 4GHz'].rank()
df['Gain_4GHz_Rank'] = df['Gain at 4GHz'].rank(ascending=False)

df['Total_Rank'] = df[['NFmin_2.4GHz_Rank', 'Gain_2.4GHz_Rank', 'NFmin_4GHz_Rank', 'Gain_4GHz_Rank']].sum(axis=1)

top_5_devices = df.sort_values(by='Total_Rank').head(5)

top_5_devices_output = top_5_devices[['Device name', 'Total_Rank']]

print("Top 5 devices based on combined NFmin and Gain performance:")
print(top_5_devices_output)
