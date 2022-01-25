#!/usr/bin/env python3

import pandas as pd

csv_df = pd.read_csv('csv1.csv', encoding="ISO-8859-1")

#Q11
sum_animal_fat_2014 = csv_df.groupby('Item')['Y2014'].sum()['Animal fats']
sum_animal_fat_2017 = csv_df.groupby('Item')['Y2017'].sum()['Animal fats']
print("Answer 11: {} and {}".format(sum_animal_fat_2014, sum_animal_fat_2017))
print("")

#Q12
mean_2015 = csv_df['Y2015'].mean()
sd_2015 = csv_df['Y2015'].std()
print("Answer 12: {} and {}".format(mean_2015, sd_2015))
print("")

#Q13
total_missing_data_2016 = csv_df['Y2016'].isnull().sum().sum()
percentage_missing_data_2016 = total_missing_data_2016/csv_df["Item"].count() * 100
print("Answer 13: {} and {}".format(total_missing_data_2016, percentage_missing_data_2016))
print("")

#Q14: Don't know how to solve so guessed answer

#Q15
sum_elements = csv_df.groupby("Element")['Y2014', 'Y2015', 'Y2016', 'Y2017', 'Y2018'].sum()
sum_import_quantity = sum_elements.filter(like='Import Quantity', axis=0)
print(sum_import_quantity)
print("Answer 15 is: 2017")
print("")

#Q16
print(sum_elements.filter(like="Production", axis=0)['Y2014'])
print("Answer 16 is: 1931287.75")
print("")

#Q17
sum_elements_2018 = sum_elements['Y2018']
print(sum_elements_2018.sort_values(ascending=False))
print("Answer 17 is Domestic supply quantity")
print("")

#Q18
print(sum_elements_2018.sort_values())
print("Answer 18 is Protein supply quantity (g/capita/day)")
print("")

#Q19
grouped = csv_df.groupby(["Area", "Element"])["Y2018"].sum()
filter1 = grouped.filter(like="Algeria", axis=0)
print(filter1)
print("Answer 19 is 36238.29")
print("")

#Q20
countries_df = csv_df.groupby("Area").count()
total_rows = countries_df["Area Code"].count()
print("Answer 20 : {}".format(total_rows))