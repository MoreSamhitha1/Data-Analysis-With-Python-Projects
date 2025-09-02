import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset?
    # This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    bachelors_count = df[df['education'] == 'Bachelors'].shape[0]
    total_count = df.shape[0]
    percentage_bachelors = round((bachelors_count / total_count) * 100, 1)

    # What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
    advanced_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    higher_education_rich = round((advanced_education[advanced_education['salary'] == '>50K'].shape[0] / advanced_education.shape[0]) * 100, 1)

    # What percentage of people without advanced education make more than 50K?
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education_rich = round((lower_education[lower_education['salary'] == '>50K'].shape[0] / lower_education.shape[0]) * 100, 1)

    # What is the minimum number of hours a person works per week?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
    min_hours_workers = df[df['hours-per-week'] == min_work_hours]
    num_min_workers = min_hours_workers.shape[0]
    rich_min_workers = min_hours_workers[min_hours_workers['salary'] == '>50K'].shape[0]
    rich_percentage = round((rich_min_workers / num_min_workers) * 100, 1)

    # What country has the highest percentage of people that earn >50K and what is that percentage?
    country_salary_counts = df.groupby('native-country')['salary'].value_counts(normalize=True).unstack()
    country_salary_counts['percentage_rich'] = country_salary_counts['>50K'] * 100
    highest_earning_country = country_salary_counts['percentage_rich'].idxmax()
    highest_earning_country_percentage = round(country_salary_counts['percentage_rich'].max(), 1)

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].mode()[0]

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage of people with Bachelor's degree: {percentage_bachelors}%")
        print(f"Percentage of people with advanced education that earn >50K: {higher_education_rich}%")
        print(f"Percentage of people without advanced education that earn >50K: {lower_education_rich}%")
        print(f"Minimum work hours per week: {min_work_hours}")
        print(f"Percentage of people working minimum hours who earn >50K: {rich_percentage}%")
        print(f"Highest earning country: {highest_earning_country}")
        print(f"Highest earning country percentage: {highest_earning_country_percentage}%")
        print("Top occupation in India for high earners:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
