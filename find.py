#%%
import pandas as pd
def dataLoad(path):
    data = pd.read_csv(path)
    df = pd.DataFrame(data)
    return df
def search_by_roll(df,query):
    return df.loc[df['roll_number'] == query]
def search_by_phone(df,query):
    return df.loc[df['phone_number'] == query]
biodata = dataLoad(r'refined/registerationdata.csv')
projectdata = dataLoad(r'refined/projectdata.csv')
print("starting python runtime...")
query = input("Enter the search Query:")
if len(query) == 7:
    print("Searching for roll numbers...")
    print('project Data==========================================')
    print(search_by_roll(projectdata,query))
    print('registeration Data====================================')
    print(search_by_roll(biodata,int(query)))
elif len(query) == 10:
    print("searching for phone numbers...")
    data = search_by_phone(projectdata,query)
    print('project Data==========================================')
    print(data)
    print('registeration Data====================================')
    print(search_by_roll(biodata,int(data['roll_number'])))
else:
    print("invalid query")