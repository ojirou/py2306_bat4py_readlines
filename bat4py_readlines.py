import subprocess
def MakeBatFile(pyfile, BatDir):
    Template=r'C:\\Users\\user\\anaconda3\\Scripts\\xxxxx.bat'
    with open(Template) as f:
        s=f.read()
        # print(type(s))
        # print(s)    
    s=s.replace('xxxxx', pyfile)
    path_w=BatDir+pyfile+'.bat'
    with open(path_w, mode='w') as f:
        f.write(s)
    # with open(path_w) as f:
    #     print(f.read())
    # subprocess.Popen(["notepad", path_w])
if __name__ == "__main__":
    FileList=r'C:\\Users\\user\\python\\FILE\\output.txt'
    PyDir=r'C:\\Users\\user\\git\\py\\'
    BatDir=r'C:\\Users\\user\\Downloads\\output_bat\\'
    with open(FileList, "r") as file:
        input_lines=file.readlines()
    input_list=[line.strip() for line in input_lines]
    for pyfile in input_list:
        MakeBatFile(pyfile, BatDir)