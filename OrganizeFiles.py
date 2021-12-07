import os
def createIfNotExist(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)
def move(foldername,files):
    for file in files:
        os.replace(file,f'{foldername}/{file}')
        print(len(files),"Files Are Moved")



if __name__=='__main__':
    files=os.listdir()
    files.remove('OrganizeFiles.py')
    imgextn=['.jpg','.png','.jpeg','.gif']
    Images=[file for file in files if os.path.splitext(file)[1].lower() in imgextn]

    Docsextn=['.txt','.pdf','.doc','.docx','.xlsx']
    Documents=[file for file in files if os.path.splitext(file)[1] in Docsextn]

    Mediaextn=['.mp3','.mp4','.mkv']
    Media=[file for file in files if os.path.splitext(file)[1].lower() in Mediaextn]

    Zipextn=['.zip']
    Zip=[file for file in files if os.path.splitext(file)[1].lower() in Zipextn]

    Scriptextn=['.php','.html','.js','.css','.py']
    Script=[file for file in files if os.path.splitext(file)[1].lower() in Scriptextn]

    Softwareextn=['.exe']
    Software=[file for file in files if os.path.splitext(file)[1].lower() in Softwareextn]

    Others=[]
    for file in files:
        if os.path.splitext(file)[1].lower() not in imgextn + Docsextn + Zipextn + Scriptextn + Softwareextn and os.path.isfile(file) :
            Others.append(file)
    lst=['Images','Documents','Media','Zip','Script','Software','Others']
    
    for i in lst:
        if len(eval(i)) != 0:
            createIfNotExist(i)
            move(i,eval(i))
