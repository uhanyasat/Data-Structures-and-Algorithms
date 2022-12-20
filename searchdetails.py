# use following Commands to check
"""
sortByDate_Amount(data)
searchByCustomer(data,'Joe')
searchByorder_date(data,'2021-01-09')
searchPrior_date(data,'2021-05-09')
searchAfter_date(data,'2021-05-09')
zip=99530
Check_avalibility_store(zip,papa_ZIP)
"""
import pandas as pds
data = pds.read_excel('pizza.xlsx')
print('**************PIZZA ORDER DETAILS**************')
print(data) 
papa_ZIP=[99501,99502,99505,99507,99510,99515,99518,99524]
def sortByDate_Amount(data):             
    data.sort_values(["Date", "Amount"], axis=0,
                 ascending=True, inplace=True)
    print('**************Sorted by Date and Amount**************')
    print(data) 
def searchByCustomer(data,cus):             
    cus_order = data.loc[data['Customer'] == cus] 
    
    print('**************Result by Customer**************')
    print(cus_order)
def searchByorder_date(data,dat):             
    dat_order = data.loc[data['Date'] == dat] 
    
    print('**************Result by Ordered Date**************')
    print(dat_order)
def searchPrior_date(data,dat):             
    dat_prior = data.loc[data['Date'] < dat] 
    
    print('**************Result by Prior Ordered Date**************')
    print(dat_prior)
def searchAfter_date(data,dat):             
    dat_after = data.loc[data['Date'] > dat] 
    
    print('**************Result by After Ordered Date**************')
    print(dat_after)
def Check_avalibility_store(zip,papa_ZIP):
    if zip in papa_ZIP:
        print('You have store in your location!')
    else:
        print('No Matches found!')
        
