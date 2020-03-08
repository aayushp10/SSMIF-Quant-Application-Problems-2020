#!/usr/bin/env python
# coding: utf-8

# In[36]:


#Create a function called sum_ssmif
def sum_ssmif(nested_list):

    #Loop through the nested list to find the position of the sublists
    #Loop through this process for every sublist within the nested list
    for index in range(len(nested_list)):
        
        #Check to see if the index is odd by using the % operator
        if index % 2 == 0:
            
            #Use a temporary value for nine to represent the index of the position 9
            nine = -1
            
            #Loop through the sub list to look for the index where the first 9 appears
            #Once this is found, assign that index value to the variable nine and break
            for i in list(range(len(nested_list[index]))):
                if nested_list[index][i] == 9:
                    nine = i
                    break
                    
            #Use a temporary value for nine to represent the index of the position 6
            six = -1
            
            #Loop through the sub list to look for the index where the first 6 appears
            #Once this is found, assign that index value to the variable six and break
            for i in list(range(len(nested_list[index]))):
                if nested_list[index][i] == 6:
                    six = i
                    break
            
            #Set the value of the sum of the sublist to be equal to 0
            sum_of_sublist = 0
            
            #Check to see if both nine and six have a value that is an index and not still -1
            if nine >= 0 and six >= 0:
                
                #Loop through the sublist and to sum the numbers up
                for i in list(range(len(nested_list[index]))):
                    
                    #For each index between nine and six, multiply the value by 2 and add it to the value of sum_of_sublist
                    if nine <= i <= six:
                        sum_of_sublist = sum_of_sublist + nested_list[index][i] * 2
                    
                    #For each index that isn't between nine and six, add them regularly to the value of sum_of_sublist
                    else: 
                        sum_of_sublist = sum_of_sublist + nested_list[index][i]
            
            #If the values of nine and six are still negative one run this else statement
            else: 
                
                #Loop through the sublist and to sum the numbers up
                for i in list(range(len(nested_list[index]))):
                    
                    #Add the numbers regularly to the value of sum_of_sublist
                    sum_of_sublist = sum_of_sublist + nested_list[index][i]
        
            #Replace the value of the list with the calculated sum_of_sublist
            nested_list[index] = sum_of_sublist
        
        #If the index of the sublist is odd, it will run this else statement
        else:
            
            #Use a temporary value for seven to represent the index of the position 7
            seven = -1
            
            #Loop through the sub list to look for the index where the first 7 appears
            #Once this is found, assign that index value to the variable seven and break
            for i in list(range(len(nested_list[index]))):
                if nested_list[index][i] == 7:
                    seven = i
                    break
                    
            #Use a temporary value for seven to represent the index of the position 4
            four = -1
            
            #Loop through the sub list to look for the index where the first 4 appears
            #Once this is found, assign that index value to the variable four and break
            for i in list(range(len(nested_list[index]))):
                if nested_list[index][i] == 4:
                    four = i
                    break
                    
            #Set the value of the sum of the sublist to be equal to 0
            sum_of_sublist = 0
            
            #Check to see if both seven and four have a value that is an index and not still -1
            if seven >= 0 and four >= 0:
                
                #Loop through the sublist and to sum the numbers up
                for i in list(range(len(nested_list[index]))):
                    
                    #For each index between seven and four, multiply the value by 3 and add it to the value of sum_of_sublist
                    if seven <= i <= four:
                        sum_of_sublist = sum_of_sublist + nested_list[index][i] * 3
                    
                    #For each index that isn't between seven and four, add them regularly to the value of sum_of_sublist
                    else: 
                        sum_of_sublist = sum_of_sublist + nested_list[index][i]
            
            #If the values of seven and four are still negative one run this else statement            
            else: 
                
                #Loop through the sublist and to sum the numbers up
                for i in list(range(len(nested_list[index]))):
                    
                    #Add the numbers regularly to the value of sum_of_sublist
                    sum_of_sublist = sum_of_sublist + nested_list[index][i]
            
            #Replace the value of the list with the calculated sum_of_sublist
            nested_list[index] = sum_of_sublist 
            
    #Use a temporary value for seven to represent the index of the position 4        
    four = -1
    
    #Loop through the final list to look for the index where the first 4 appears
    #Once this is found, assign that index value to the variable four and break 
    for i in list(range(len(nested_list))):
        if nested_list[i] == 4:
            four = i
            break
    
    #Use a temporary value for seven to represent the index of the position 5
    five = -1
    
    #Loop through the final list to look for the index where the first 5 appears
    #Once this is found, assign that index value to the variable five and break
    for i in list(range(len(nested_list))):
        if nested_list[i] == 5:
            five = i
            break
            
    #Check to see if both seven and four have a value that is an index and not still -1
    if four >= 0 and five >= 0:
        
        #Loop through the final list and to change the values to 0
        for i in list(range(len(nested_list))):
            
            #For each index between four and five, change the values to 0
            if four <= i <= five:
                nested_list[i] = 0
    
    #Return the sum of the nested list
    return sum(nested_list)

