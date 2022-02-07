import pandas as pd
import seaborn as sns

df = pd.read_excel('Building_energy_efficiency.xlsx')

column_names = {'X1': 'Relative_Compactness', 'X2': 'Surface_Area',
                'X3': 'Wall_Area', 'X4': 'Roof_Area', 'X5': 'Overall_Height',
                'X6': 'Orientation', 'X7': 'Glazing_Area',
                'X8': 'Glazing_Area_Distribution',
                'Y1': 'Heating_Load', 'Y2': 'Cooling_Load'}

df = df.rename(columns=column_names)

simple_linear_reg_df = df[["Relative_Compactness", 'Cooling_Load']].sample(15, random_state=2)

sns.regplot(x="Relative_Compactness", y="Cooling_Load", data=simple_linear_reg_df)
