# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 13:49:08 2019

@author: n882049
"""

import pandas as pd
ice_cream = pd.read_excel("C://Users//n882049//Documents//YinDiWeiJiu//杰布亨廷//wayfair_da_oa//Wayfair bia oa//IceCreamDataSet.xlsx")
ice_cream.reset_index(inplace =True)
ice_cream.drop("index", axis=1, inplace=True)

#Some calculation
ice_cream['Weekday']=ice_cream['Date'].dt.dayofweek
ice_cream['Cost']=ice_cream['Revenue'] - ice_cream['Profit']
ice_cream['Profit_Margin']=ice_cream['Profit'] / ice_cream['Revenue']

['Customer', 'Date', 'Flavor', 'Revenue', 'Profit', 'weekday', 'Cost', 'Profit_Margin']


#Overview

#Aggregate by Date
aggregation_date = {
                       'Revenue': ['sum', 'mean'],
                       'Profit': ['sum', 'mean']
                       }
ice_cream_date = ice_cream.groupby('Date').agg(aggregation_date)

# clean up the column name: from 2 layer to 1
ice_cream_date.columns = ["_".join(x) for x in ice_cream_date.columns.ravel()]
# sort by 
ice_cream_date.sort_values(['Revenue_count'],ascending=False)

#Aggregate by Weekday
aggregation_weekday = {
                       'Revenue': ['sum', 'mean'],
                       'Profit': ['sum', 'mean']
                       }
ice_cream_weekday = ice_cream.groupby('Weekday').agg(aggregation_weekday)

# clean up the column name: from 2 layer to 1
ice_cream_weekday.columns = ["_".join(x) for x in ice_cream_weekday.columns.ravel()]
# sort by 
ice_cream_weekday.sort_values(['Revenue_count'],ascending=False)


#Aggregate by Customer
aggregation_customer = {
                       'Revenue': ['count', 'mean'],
                       'Profit': 'mean'
                       }
ice_cream_customer = ice_cream.groupby('Customer').agg(aggregation_customer)

# clean up the column name: from 2 layer to 1
ice_cream_customer.columns = ["_".join(x) for x in ice_cream_customer.columns.ravel()]
# sort by 
ice_cream_customer.sort_values(['Revenue_count'],ascending=False)
# if did not clean up the column names, need to sort by two layer column name like this:
#ice_cream_customer.sort_values([('Revenue', 'count')],ascending=False)


test1 = ice_cream[,1:]


#Programming 1: sum of two-digit number
test1 = [1,10000,80,-91]
test1 = [47,1900,1,90,45]
test1 = [-13,1900,1,100,45]

def Ntwo(mylist):
    sum = 0
    for ele in mylist:
        if len(str(abs(ele))) == 2:
            sum = sum + ele
    return(sum)
    
print(Ntwo(mylist=test1))
        
#Programming 2: print string that divisible by 2/3/5
def printstr(N):
    print_2 = "Codility"
    print_3 = "Test"
    print_5 = "Coders"
    for number in range(1,N+1):
        str_print = ""
        if number % 2 == 0:
            str_print = str_print + print_2
        if number % 3 == 0:
            str_print = str_print + print_3
        if number % 5 == 0:
            str_print = str_print + print_5
        if str_print == "":
            str_print = number
        print(str_print)

printstr(24)

#Programming 3: flip coins
test1 = [1,0,0,1,0,0]
test1 = [0,0,1,0,1,0,0,1]
test1 = [0,0,0,1,0,0]
def coin_flip_times(mylist):
    head_sum = 0
    tail_sum = 0
    for ele in mylist:
        if ele == 0:
            head_sum+=1
        elif ele == 1:
            tail_sum+=1
        else:
            print ("Error elements!")
    return (min(head_sum,tail_sum))

print(coin_flip_times(test1))














