import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import pandas as pd
import seaborn as sns


kiva = pd.read_csv('kiva_data.csv')
# print(kiva.head())
food_prod = kiva[kiva.activity == 'Food Production/Sales'].loan_amount
gen_store = kiva[kiva.activity == 'General Store'].loan_amount
farming = kiva[kiva.activity == 'Farming'].loan_amount
fmt = '${x:,.2f}'
tick = mtick.StrMethodFormatter(fmt)


fig1, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 10))
sns.barplot(x='country', y='loan_amount', data=kiva, ax=ax1)
sns.barplot(data=kiva, x="country", y="loan_amount", hue='gender', ax=ax2)
ax1.yaxis.set_major_formatter(tick)
ax2.yaxis.set_major_formatter(tick)
sns.despine()


sns.set_style('whitegrid')
fig2, (ax1, ax2) = plt.subplots(2, 1, figsize=(16, 10))
sns.set_palette('Set1')
sns.boxplot(data=kiva, x='country', y='loan_amount', ax=ax1)
sns.set_palette('dark')
sns.boxplot(data=kiva, x='activity', y='loan_amount', ax=ax2)
sns.despine()


sns.set_style('ticks')
fig3, (ax1, ax2) = plt.subplots(2, 2, figsize=(16, 10))
ax1[0].set_xlabel('loan_amount')
sns.kdeplot(food_prod, shade=True, shade_lowest=False,
            label='Food Productions/Sales', ax=ax1[0])
sns.kdeplot(gen_store, shade=True, shade_lowest=False,
            label='General Store', ax=ax1[0])
sns.kdeplot(farming, shade=True, shade_lowest=False,
            label='farming', ax=ax1[0])
sns.violinplot(data=kiva, x="activity", y="loan_amount", ax=ax1[1])
sns.set_palette("Spectral")
sns.violinplot(data=kiva, x='country', y='loan_amount',
               hue='gender', split=True, ax=ax2[0])
sns.set_palette("Accent")
sns.violinplot(data=kiva, x='activity', y='loan_amount',
               hue='gender', split=True, ax=ax2[1])
sns.despine()

plt.show()
