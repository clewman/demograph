
import pandas as pd


df_sample = pd.read_csv('laucnty16.csv')
df_sample['State FIPS Code'] = df_sample['State FIPS Code'].apply(lambda x: str(x).zfill(2))
df_sample['County FIPS Code'] = df_sample['County FIPS Code'].apply(lambda x: str(x).zfill(3))
df_sample['FIPS'] = df_sample['State FIPS Code'] + df_sample['County FIPS Code']


# County Name/State Abbreviation
fips = df_sample['FIPS'].tolist()


county_names = []
state_abbrs = []
county_data = df_sample['County Name/State Abbreviation'].tolist()
for i in range(len(county_data)):
    state_abbrs.append(county_data[i][len(county_data[i])-2:])
    county_names.append(county_data[i][:len(county_data[i])-4])


for i in range(len(fips)):
    print(f'{state_abbrs[i]} {county_names[i]} {fips[i]}')




