import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# 1. Use Pandas to import the data from "fcc-forum-pageviews.csv".
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

# 2. Clean the data by filtering out days when the page views were in the top 2.5% of the dataset or bottom 2.5% of the dataset.
df = df[
    (df['value'] >= df['value'].quantile(0.025)) &
    (df['value'] <= df['value'].quantile(0.975))
]

# 3. Create a draw_line_plot function
def draw_line_plot():
    # A copy of the DataFrame is used for the plot.
    df_line = df.copy()

    # Create the figure and axes for the plot.
    fig, ax = plt.subplots(figsize=(15, 6))

    # Plot the data.
    ax.plot(df_line.index, df_line['value'], color='red')

    # Set the title and labels.
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')

    # Save the figure and return it.
    fig.savefig('line_plot.png')
    return fig

# 4. Create a draw_bar_plot function
def draw_bar_plot():
    # A copy of the DataFrame is used for the plot.
    df_bar = df.copy()

    # Create new columns for year and month.
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month

    # Group the data by year and month and calculate the average.
    df_bar = df_bar.groupby(['year', 'month'])['value'].mean().reset_index()

    # Pivot the data for the bar chart.
    df_bar_pivot = df_bar.pivot(index='year', columns='month', values='value')
    
    # Create the figure and axes for the plot.
    fig, ax = plt.subplots(figsize=(15, 10))

    # Plot the bar chart.
    df_bar_pivot.plot(kind='bar', ax=ax)

    # Set the title and labels.
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    ax.legend(title='Months', labels=[
        'January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December'
    ])

    # Save the figure and return it.
    fig.savefig('bar_plot.png')
    return fig

# 5. Create a draw_box_plot function
def draw_box_plot():
    # A copy of the DataFrame is used for the plots.
    df_box = df.copy()

    # Add 'year' and 'month' columns for the box plots.
    df_box['year'] = df_box.index.year
    df_box['month'] = df_box.index.strftime('%b')

    # Create the figure with two subplots.
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(20, 8))

    # Plot the first box plot (Year-wise).
    sns.boxplot(x='year', y='value', data=df_box, ax=ax1)
    ax1.set_title('Year-wise Box Plot (Trend)')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Page Views')

    # Order the months for the second box plot.
    month_order = [
        'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
        'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
    ]
    
    # Plot the second box plot (Month-wise).
    sns.boxplot(x='month', y='value', data=df_box, ax=ax2, order=month_order)
    ax2.set_title('Month-wise Box Plot (Seasonality)')
    ax2.set_xlabel('Month')
    ax2.set_ylabel('Page Views')

    # Save the figure and return it.
    fig.savefig('box_plot.png')
    return fig
