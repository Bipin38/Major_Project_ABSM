import os 
import pandas as pd 


label_types = os.listdir("data")
dataset_path = label_types 



poses = [] 
for item in dataset_path:
    all_poses = os.listdir('data' + '/' + item  )
    

    for pose in all_poses:
        poses.append((item,str('data'+'/'+ item )+ '/' + pose ))


df = pd.DataFrame(data=poses, columns = ['tag' , 'video_name'])


df.to_csv("data.csv")



print(df)