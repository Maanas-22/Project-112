import os 
import shutil

from_dir="C:/Users/user/Downloads/Demo"
to_dir="C:/Users/user/Downloads/Demo"

files_list=os.listdir(from_dir)

for file_name in files_list:
    name, ext=os.path.splitext(file_name)
    if(ext==""):
        continue
    elif ext in ['.jpg', '.jpeg', '.jfif', '.png', '.webp']:
        source_path=from_dir+'/'+file_name
        folder_path=to_dir+'/'+'Images_Folder'
        destination_path=folder_path+'/'+file_name

        if(os.path.exists(folder_path)):
            print("Moving ", file_name," to Images Folder ...")
            shutil.move(source_path, destination_path)
        else:
            os.mkdir(folder_path)
            print("Moving ", file_name," to Images Folder ...")
            shutil.move(source_path, destination_path)

'''
Output

Moving  image 1.jfif  to Images Folder ...
Moving  image 2.jfif  to Images Folder ...
Moving  image 3.jfif  to Images Folder ...
Moving  image 4.jfif  to Images Folder ...
'''