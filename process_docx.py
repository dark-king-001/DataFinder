import pandas as pd
import docx
import io
def dataLoad(path):
    data = pd.read_csv(path)
    df = pd.DataFrame(data)
    return df
def datasave(path,df):
    df.to_csv(path,index=False)
def Load_docx(path):
    print(docx.Document(path).paragraphs[].text)

Load_docx("/home/piyush/Desktop/CustomServer/DataFinder/List of companies for Summer Training Program 2022.docx")