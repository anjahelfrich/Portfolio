import os

dir = "./gpxFILES"
with open('gpxFileList.txt', 'w') as f:
    for file in os.listdir(dir):
        path = os.path.join(dir, file)
        f.write(f"{path}\n")