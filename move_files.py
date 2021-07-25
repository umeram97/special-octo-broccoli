import os

folders = os.listdir()[2:]
#os.rename(filename,parentdirectoy_filename) #
for folder in folders: # interating through the main directory
    path1 = './/' + folder
    sub1 = os.listdir(path = path1)
    
    for subfolder in sub1: # 1st subs
        path2 = './/' + folder + '//' + subfolder
        files = os.listdir(path = path2)
        for file in files:
            source = path2 + '//' + file
            destination = path1 + '//' + subfolder + '_' + file
            os.rename(src = source, dst = destination)