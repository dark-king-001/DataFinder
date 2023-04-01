#%%
import pandas as pd
import os
#%%
output_path = r'C:\Users\piyus\OneDrive\Desktop\CustomServer\datasets\refined\projectdata.csv'
data = pd.read_csv(output_path)
df = pd.DataFrame(data)
df.head()
#%%
#text data processing
def processtext(relativeFolder,fileName):
    path = os.getcwd()+'/'+relativeFolder+'/'+fileName+'.txt'
    raw = open(path,'r',encoding="utf8")

    read = raw.read().split("\n")
    size = len(read)
    print("size of the current working file:",size)
    List = [0,0,0,0,0,0]
    data_stream = False
    count = 0
    for index in range(0,size,1):
        if read[index][0:4] == "B.Te":
            data_stream = True
        if data_stream == True:
            if read[index][0:4] == "B.Te":
                List[1] = read[index]
            elif read[index][0:4] == "Stud":
                List[2] = read[index+2]
            elif read[index][0:4] == "Fath":
                List[3] = read[index+2]
            elif read[index][0:4] == "1218":
                List[0] = read[index]
            elif read[index][0:4] == "1219":
                List[0] = read[index]
            elif read[index][0:4] == "1220":
                List[0] = read[index]
            elif read[index][0:4] == "1221":
                List[0] = read[index]
            elif read[index][0:4] == "Gend":
                List[4] = read[index+2]
            elif read[index][0:4] == "Appe":
                List[5] = read[index+2]
            count += 1
        if count >= 44:
            df.loc[len(df.index)] = List
            data_stream = False
            count = 0
    print("following path is now successfully processed :"+path)
    raw.close()

# %%
df.to_csv(output_path,index=False)
# %%
