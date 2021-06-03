import pandas as pd
import statistics
import csv
df= pd.read_csv("data.csv")
height_list= df["Height(Inches)"].to_list()
weight_list= df["Weight(Pounds)"].to_list()
height_mean= statistics.mean(height_list)
weight_mean= statistics.mean(weight_list)
height_median= statistics.median(height_list)
weight_median= statistics.median(weight_list)
height_mode= statistics.mode(height_list)
weight_mode= statistics.mode(weight_list)
print("Mean, Median and Mode of height is {}, {} and {} respectively".format(height_mean, height_median, height_mode)) 
print("Mean, Median and Mode of weight is {}, {} and {} respectively".format(weight_mean, weight_median, weight_mode))