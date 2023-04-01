#%%
import pandas as pd
import os
#%%
output_path = r'C:\Users\piyus\OneDrive\Desktop\CustomServer\datasets\refined\projectdata.csv'
data = pd.read_csv(output_path)
df = pd.DataFrame(data)
df.head()

#%%
#excel data processing
def processExcel(relativeFolder,fileName):
    path = os.getcwd()+'/'+relativeFolder+'/'+fileName+'.xlsx'
    raw = pd.DataFrame(pd.read_excel(path))
    selected = raw[["Team member3- Name",
                    "Team member3- Roll No.",
                    "Team member3- Contact no",
                    "Title of project",
                    "Project Guides"]]
    for index in range(0,len(raw.index),1):
        print("rows inserted",index)
        data = list(selected.loc[index])
        if not pd.isnull(data[0]):
            df.loc[len(df.index)] = data
    
    print(df.head(5))
processExcel('raw/Excel','guide_list_a')

# %%
df.to_csv(output_path,index=False)