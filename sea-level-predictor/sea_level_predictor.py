import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    print(df.head())

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])
    plt.show()

    # Create first line of best fit
    slope, intercept, _ ,_ , _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_1880 = range(1880, 2051)
    plt.plot(x_1880, intercept + slope*x_1880)

    # Create second line of best fit
    slope, intercept, _ ,_ , _ = linregress(df.query('Year >= 2000')['Year'], df.query('Year >= 2000')['CSIRO Adjusted Sea Level'])
    x_2000 = range(2000, 2051)
    plt.plot(x_2000, intercept + slope*x_2000)

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()