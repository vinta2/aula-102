import os
import shutil 

from_dir="teste-1"
to_dir="teste-2"


list_of_file=os.listdir(from_dir)
print(list_of_file)

for file_name in list_of_file:
    name,extesion=os.path.splitext(file_name)
    print(extesion)
    if extesion=="":
        continue
    if extesion in[".gif",".png",".jpg",".jfif"]:
        path1=from_dir+"/"+file_name
        path2=to_dir+"/"+"image"
        path3=to_dir+"/"+"image"+"/"+file_name

    if os.path.exists(path2):
        print("movendo"+file_name)
        shutil.move(path1,path3)
    else:
        os.makedirs(path2)
        print("movendo"+file_name)
        shutil.move(path1,path3)