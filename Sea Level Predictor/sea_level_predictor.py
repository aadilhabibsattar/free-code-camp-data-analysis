import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    best_fit = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    slope = best_fit.slope
    intercept = best_fit.intercept
    x = [n for n in range(1880, 2051)]
    y = [((n*slope)+intercept) for n in x]

    plt.plot(x, y, linewidth=1, color="black")

    # Create second line of best fit
    df_recent = df[df['Year'] >= 2000]
    best_fit = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    slope = best_fit.slope
    intercept = best_fit.intercept
    x = [n for n in range(2000, 2051)]
    y = [((n*slope)+intercept) for n in x]

    plt.plot(x, y, linewidth=1, color="red")


    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

draw_plot()