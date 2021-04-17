import csv
import statistics
import pandas as pd

df=pd.read_csv("height-weight.csv")
height_list=df["Height(Inches)"].tolist()
weight_list=df["Weight(Pounds)"].tolist()
height_mean=statistics.mean(height_list)
weight_mean=statistics.mean(weight_list)
height_sd=statistics.stdev(height_list)
weight_sd=statistics.stdev(weight_list)

print("mean of height is -->",height_mean)
print("mean of weight is -->",weight_mean)
print("standard deviation is -->",height_sd)
print("standard deviation is -->",weight_sd)

height_first_sd_start,height_first_sd_end=height_mean-height_sd,height_mean+height_sd
height_second_sd_start,height_second_sd_end=height_mean-(2*height_sd),height_mean+(2*height_sd)
height_third_sd_start,height_third_sd_end=height_mean-(3*height_sd),height_mean+(3*height_sd)

weight_first_sd_start,weight_first_sd_end=weight_mean-weight_sd,weight_mean+weight_sd
weight_second_sd_start,weight_second_sd_end=weight_mean-(2*weight_sd),weight_mean+(2*weight_sd)
weight_third_sd_start,weight_third_sd_end=weight_mean-(3*weight_sd),weight_mean+(3*weight_sd)

height_list_of_data_within_1_sd=[result for result in height_list if result>height_first_sd_start and result < height_first_sd_end]
height_list_of_data_within_2_sd=[result for result in height_list if result>height_second_sd_start and result < height_second_sd_end]
height_list_of_data_within_3_sd=[result for result in height_list if result>height_third_sd_start and result < height_third_sd_end]

weight_list_of_data_within_1_sd=[result for result in weight_list if result>weight_first_sd_start and result < weight_first_sd_end]
weight_list_of_data_within_2_sd=[result for result in weight_list if result>weight_second_sd_start and result < weight_second_sd_end]
weight_list_of_data_within_3_sd=[result for result in weight_list if result>weight_third_sd_start and result < weight_third_sd_end]

print("{}% of data for height lies within 1 standard deviation".format(len(height_list_of_data_within_1_sd)*100.0/len(height_list)))
print("{}% of data for height lies within 2 standard deviation".format(len(height_list_of_data_within_2_sd)*100.0/len(height_list)))
print("{}% of data for height lies within 3 standard deviation".format(len(height_list_of_data_within_3_sd)*100.0/len(height_list)))

print("{}% of data for weight lies within 1 standard deviation".format(len(weight_list_of_data_within_1_sd)*100.0/len(weight_list)))
print("{}% of data for weight lies within 2 standard deviation".format(len(weight_list_of_data_within_2_sd)*100.0/len(weight_list)))
print("{}% of data for weight lies within 3 standard deviation".format(len(weight_list_of_data_within_3_sd)*100.0/len(weight_list)))

