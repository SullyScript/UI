# ECOR 1042 Lab 6 - Template Individual submission for batch_UI

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Emily Causi"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "10123902"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-55"

#==========================================#
# Place your script for your batch_UI after this line
"""
Allows user to provide a batch file for loading, sorting, graphing, and calculating the function of the line of best fit for given parameters.
"""
import load_data as ld
import sort as srt
import curve_fit as cf
import histogram as hg

import string
import math
import numpy as np
import csv
   
# Referencing the test_batch.txt file to test units                                                                                                                                                                                 
file_name = input("Please enter the file where your commands are stored:")
batch_file = open(file_name)

for line in batch_file:
   item = line.strip("\n").split(";")

   if item[0].lower() == 'l':
      loaded_dic_list = ld.load_data(item[1], (item[2], item[3]))
      print('Data loaded.')

   elif item[0].lower() == 's':
      sorted_data = srt.sort(loaded_dic_list, item[2], item[1])
      
      if item[-1].lower() == 'n':
         print('Data loaded, not displayed.')

      elif item[-1].lower() == 'y':
         print("Data loaded.")
         print(sorted_data)

   elif item[0].lower() == 'c':
      health_dic_list = calculate_health(loaded_dic_list)
      curved_data = cf.curve_fit(health_dic_list, item[1], int(item[2]))
      print(curved_data)

   elif item[0].lower() == 'h':
      hist_graph = hg.histogram(loaded_dic_list, item[1])

   elif item[0].lower() == 'e':
      break
   
# Closing the file
batch_file.close()