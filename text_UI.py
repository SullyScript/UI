# ECOR 1042 Lab 6 - Template text UI
# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Emily Causi"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101236902"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-55"

#==========================================#
# Place your script for your text_UI after this line
"""
Allows user to access loading, sorting, graphing, and calculating the function of the line of best fit for given parameters.
"""

# Importing necessary files and libraries for referencing
import load_data as ld
import sort as srt
import curve_fit as cf
import histogram as hg

import string
import math
import csv

database = True

valid_dict_values = {"L": "l", "S": "s", "C": "c", "H": "h", "E": "e"}
valid_list_values = list(valid_dict_values.items())

while database:
    load_data_inputs = valid_list_values[0]
    sort_data_inputs = valid_list_values[1]
    curve_fit_inputs = valid_list_values[2]
    histogram_inputs = valid_list_values[3]
    exit_inputs = valid_list_values[4]   

    command = input('The available commands are:\nL)oad Data\nS)ort Data\nC)urve Fit\nH)istogram\nE)xit \n\nPlease type your Command:')

    if command in load_data_inputs:
        file_name = input('Please enter the name of the file:')
        attribute = input('Please enter the attribute to use as a filter:')
        attribute_value = input('Please enter the value of the attribute:')
        load_tuple = (attribute, attribute_value)

        try:
            loaded_list = ld.load_data(file_name, load_tuple)
            print('Data loaded.')

        except:
            loaded_list = ld.load_data(file_name, load_tuple)
            print('Data loaded.')

    elif command in sort_data_inputs:
        attribute = input('Please enter the attribute you want to use for sorting (Agility, Armor, Intelligence, Health): ')
        sort_order = input('Ascending (A) or Descending (D) order:')
        sort_order = sort_order.upper()

        try:
            srt.sort(loaded_list, sort_order, attribute)

        except:
            print('File not loaded.')
            continue

        display = input('Data Sorted. Do you want to display the data?(Y/N):')
        display = display.upper()

        if display == 'Y':
            print(loaded_list)

        else:
            print('Data loaded, not displayed.')

    elif command in curve_fit_inputs:
        attribute = input('Please enter the attribute you want to use to find the best fit for Health:')
        poly_order = input('Please enter the order of the polynomial to be fitted:')
        deg = int(poly_order)
        ld.calculate_health(loaded_list)

        try:
            print(cf.curve_fit(loaded_list, attribute, deg))

        except:
            print('Data not loaded.')

    elif command in histogram_inputs:
        attribute = input('Please enter the attribute you want to use for plotting:')
        hg.histogram(loaded_list, attribute)

    elif command in exit_inputs:
        print('Exited program.')
        break

    else:
        print('Invalid command.')