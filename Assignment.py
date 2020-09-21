#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd    #importing pandas

file=pd.read_csv('Desktop/pcr_testing_table1_location_agg.csv')#reading the csv file
i=0

# while is for, if the user enter wrong postcode
while(i<5): 
    post_code=int(input(' Please enter post code\n'))  
    
#validating the post code
    
    if file.postcode.isin([post_code]).any():  #validating the post code
        print('\n')
        print('The data is available from 2020-01-01\n')
        date=str(input("Enter Date(YYYY-MM-DD) or Press Enter to Continue without Date:\n"))
        
#code for the count test cases without  date

        if date == '' :
            testcount_for_postcode=file.loc[file.postcode==post_code,'test_count']
            print(" The total test count in post code " +str(post_code) +  " is ", +testcount_for_postcode.sum())
            break
            
            
#code for the cout test cases on particular date and postcode
    
        else: 
            if file.test_date.isin([date]).any():                
                testcases_for_datecount =file.loc[(file.postcode==post_code) & (file.test_date==date),'test_count']
                print('The test count on  '+str(date)+ ' and post code ' +str(post_code)+' is '+str(testcases_for_datecount.sum()))
                break
                
#If the user enters wrong or in-valid date

            else:
                j=0
                while (j<2):
                    j=j+1
                    date=input('Plese enter correct date')
                    
                    if file.test_date.isin([date]).any():
                        testcases_for_datecount=file.loc[(file.postcode==post_code) & (file.test_date==date),'test_count']
                        print('The test count on  '+str(date)+ ' and post code ' +str(post_code)+' is '+str(testcases_for_datecount.sum()))
                        i=5
                        break                       
                    if j==2:
                        print('you have reached the limit')
                        
# if user enters wrong postcode

    else:
        print('please enter the correct post code\n')
        i=i+1
        if(i==5):
            print('you have reached the limit\n')
            






