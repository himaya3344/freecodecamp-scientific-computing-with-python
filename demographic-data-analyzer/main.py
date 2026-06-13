import pandas as pd

column_names = [
    'age', 'workclass', 'fnlwgt', 'education',
    'education-num', 'marital-status', 'occupation',
    'relationship', 'race', 'sex',
    'capital-gain', 'capital-loss',
    'hours-per-week', 'native-country', 'salary'
]

df = pd.read_csv("adult.data",
                  names=column_names,
                  skipinitialspace=True)


print(df["race"].value_counts())
average_age_men = round(
    df[df["sex"] == "Male"]["age"].mean(),
    1
)
print(average_age_men) 

percentage_bachelors = round(
   (len(df[df["education"] == "Bachelors"]) / len(df)) * 100,
    1
) 
print(percentage_bachelors) 

higher_education = df[
    df["education"].isin(["Bachelors", "Masters", "Doctorate"])
]

higher_education_rich = higher_education[
    higher_education["salary"] == ">50K"
]

higher_education_rich_percentage = round(
    (len(higher_education_rich) / len(higher_education)) * 100,
    1
)

print(higher_education_rich_percentage)

lower_education = df[
    ~df["education"].isin(["Bachelors", "Masters", "Doctorate"])
]

lower_education_rich = lower_education[
    lower_education["salary"] == ">50K"
]

lower_education_rich_percentage = round(
    (len(lower_education_rich) / len(lower_education)) * 100,
    1
)

print(lower_education_rich_percentage)

min_work_hours = df["hours-per-week"].min()

print(min_work_hours)

num_min_workers = df[
    df["hours-per-week"] == min_work_hours
]

rich_min_workers = num_min_workers[
    num_min_workers["salary"] == ">50K"
]

rich_percentage = round(
    (len(rich_min_workers) / len(num_min_workers)) * 100,
    1
)

print(rich_percentage)

country_percentages = (
    df[df["salary"] == ">50K"]["native-country"].value_counts()
    /
    df["native-country"].value_counts()
) * 100

highest_earning_country = country_percentages.idxmax()
highest_earning_country_percentage = round(
    country_percentages.max(),
    1
)

print(highest_earning_country)
print(highest_earning_country_percentage)

india_rich = df[
    (df["native-country"] == "India") &
    (df["salary"] == ">50K")
]

print(india_rich["occupation"].value_counts())

top_IN_occupation = (
    india_rich["occupation"]
    .value_counts()
    .idxmax()
)

print(top_IN_occupation)

