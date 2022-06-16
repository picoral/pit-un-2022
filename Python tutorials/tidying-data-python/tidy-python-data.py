'''
PIT-UN Internship
Working with Messy Data
Week 1
'''

import pandas as pd, os, seaborn as sns, matplotlib.pyplot as plt

# verify that data is where we think it is
# print(os.listdir("data"))

# file we're interested in: 'race_ethnicity_gender_2010.xlsx'
incarc_data_2010 = pd.read_excel('data/race_ethnicity_gender_2010.xlsx',
                                sheet_name = "Total",
                                skiprows = 4)

# filtered based on Arizona
az_data = incarc_data_2010[incarc_data_2010['Geography'] == "Arizona"].copy()

az_incarc_rates = az_data[["Geography"] + 
                            [col_name for col_name in az_data.columns if "Incarceration rate" in col_name]]
# print(az_incarc_rates)

# start by changing the column names in the data
az_incarc_rates.columns = (['geography', 'Population at large'] + 
                            [col_name.replace("Incarceration rate: ", "") for col_name in az_incarc_rates.columns[2:]])
az_incarc_rates_tidy = pd.melt(az_incarc_rates, 
                                id_vars = ["geography"],
                                var_name = "race_ethnicity",
                                value_name = "incarceration_rate")
# change type of incarceration_rate col to float
az_incarc_rates_tidy.incarceration_rate = az_incarc_rates_tidy.incarceration_rate.astype(float)


sns.set_color_codes("pastel")
ax = sns.barplot(x="incarceration_rate", y="race_ethnicity", data=az_incarc_rates_tidy, color="b")
ax.set(xlabel = "Incarceration Rate per 100k",
        ylabel = '',
        title = "Incarceration Rates in AZ per 100k")
plt.savefig('plot.png', bbox_inches='tight')
# plt.show()

az_incarc_rates_tidy.to_csv("data/az_incarceration_rates_2010.csv", 
                            sep= ";",
                            index = False)













