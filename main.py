import os 
import math
from columnar import columnar



def get_size_name(Filebytes):
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")

    
    i = int(math.floor(math.log(Filebytes, 1024)))
    p = math.pow(1024, i)
    s = round(Filebytes / p, 2)

    return s, size_name[i] 


def get_directory_size(directory):

    total = 0
    try:
        for entry in os.scandir(directory):
            if entry.is_file():
                total += entry.stat().st_size

            elif entry.is_dir():
                total += get_directory_size(entry.path)

    except NotADirectoryError:

        return os.path.getsize(directory)
    except PermissionError:
        
        return 0
    return total


total_size = 0
data = []


for fileName in os.listdir(os.getcwd()):
 

    if os.path.isdir(fileName):

        raw_size = get_directory_size(fileName)
        size ,size_name = get_size_name(raw_size)
        total_size = total_size + raw_size


        data.append([size,size_name,fileName])


    else :

        raw_size = os.path.getsize(fileName)
        size ,size_name  = get_size_name(fileName)
        total_size = total_size + raw_size


        data.append([size,size_name,fileName])


headers = ["size", "size_name", "Name"]
table = columnar(data, headers)
print(table)

size ,size_name  = get_size_name(total_size)

print(f"{size} {size_name} total size")



