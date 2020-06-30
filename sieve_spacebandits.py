# Sieve space startups based on interest
import pandas as pd
df = pd.read_excel('./datasets/spacebandits.xlsx')

# I want small startups not in USA (cause they've got an unfavorable policy for foreigners).
mask1 = df['country']!='usa'
mask2 = (df['employees']=='1-10') & (df['total_funding']>=100000)
mask3 = df['employees']=='11-50'
mask4 = df['employees']=='51-200'
interest = df[mask1 & (mask2 | mask3 | mask4)].sort_values(by='employees')

print('Saving {}/{} startups to file (datasets/prospect_spacebandits.xlsx)'.format(interest.shape[0], df.shape[0]))
interest.to_excel('./datasets/prospect_spacebandits.xlsx', index=False)
print('COMPLETED')