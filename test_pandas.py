import pandas as pd

df = pd.DataFrame({
    'nom': ['Alice', 'Bob', 'Charly', 'David', 'Emilie'],
    'age': [25, 30, 35, 27, 29],
    'city': ['Paris', 'Londre', 'New York', 'Berlin', 'Tokyo'],
})

noms = df['nom']
#print(noms)

filtered_df = df[df["age"] > 28]
#print(filtered_df)

df["salary"] = [50000, 60000, 70000, 55000, 65000]
#print(df)

df.sort_values(by='age', inplace=True)
#print(df)

moyenen_age = df['age'].mean()
#print(moyenen_age)

mediane_age = df['age'].median()
#print(mediane_age)

ecart_type_age = df['age'].std()
#print(ecart_type_age)

file = pd.read_csv('DataBase/students.csv', sep=',')
print(file)

grouped_list = file.groupby('Gender').agg({'Grade': 'mean'})
print(grouped_list)

export_csv = grouped_list.to_csv('DataBase/student_grades_avg.csv', header=True)