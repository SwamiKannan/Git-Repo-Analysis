import os
import pickle


folderdicts=[]
errors=[]
orig_path1=os.getcwd()


def list_files(startpath):
    for root, dirs, files in os.walk(startpath):
        for f in files:
            if f.endswith('.py'):
                folderdicts.append(os.path.join(root,f))


list_files(os.getcwd())

import_dir={}
for first_file in folderdicts:
    with open(first_file,'r', encoding="utf8") as f:
        trial_file=f.readlines()
    for line in trial_file:
        if line.find('import ')>=0:
            line=line.replace('\n','')
            if first_file in import_dir:
                import_dir[first_file].append(line)
            else:
                import_dir[first_file]=[line]
import_dir.pop('d:\\Python-ai-assistant\\read_folder_struc.py')
import_dir.pop('d:\\Python-ai-assistant\\map.py')
with open('folder_struct','wb') as f:
    pickle.dump(import_dir,f)