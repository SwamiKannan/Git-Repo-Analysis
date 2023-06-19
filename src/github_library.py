from stdlib_list import stdlib_list
import pickle
import os

libraries=stdlib_list("3.9")

class GH_Library():
    def __init__(self,path,write=False):
        self.folderdicts=[]
        self.errors=[]
        self.orig_path1=os.getcwd()
        self.write=write
        self.path=path

    def list_files(self,startpath):
        '''
        Walkthrough the startpath and document all the files and folders along with their path
        write is an optional parameter that allows you to save the list of .py files along with their path to disk
        '''
        for root, dirs, files in os.walk(startpath):
            for f in files:
                if f.endswith('.py'):
                    self.folderdicts.append(os.path.join(root,f))
        if self.write:    
            with open('folder_struct','wb') as p:
                pickle.dump(self.folderdicts,p)
        


    
    def identify_libraries(self):
        '''
        From the files and folders provided in list_files identify which the lines of code contain the import statements and create a dictionary with {path:import line statements}
        '''
        
        self.import_dir={}
        for first_file in self.folderdicts:
            with open(first_file,'r', encoding="utf8") as f:
                trial_file=f.readlines()
            for line in trial_file:
                if line.find('import ')>=0:
                    line=line.replace('\n','')
                    if first_file in self.import_dir:
                        self.import_dir[first_file].append(line)
                    else:
                        self.import_dir[first_file]=[line]
        self.import_dir.pop('d:\\Python-ai-assistant\\read_folder_struc.py')
        self.import_dir.pop('d:\\Python-ai-assistant\\map.py')
        if self.write:
            with open('folder_struct','wb') as f:
                pickle.dump(self.import_dir,f)

    def extract_libraries(self):
        '''
        Get all the libraries by finding those words where the words that precede them are "import" or "from".
        In any case check if this word selected has a "." e.g. from matplotlib.pyplot. If so, extract only the first term 'matplotlib'
        Create a dictionary saying filename:[library1, library2]
        '''
        self.dict_libraries={}
        for keys, values in self.import_dir.items():
            file1=self.import_dir[keys]
            for import1 in file1:
                libs=import1.split(' ')[1]
                if libs in libraries or libs=='':
                    continue
                if libs.find('.')>0:
                    libs=libs.split('.')[0]
                if keys in self.dict_libraries:
                    self.dict_libraries[keys].append(libs)
                else:
                    self.dict_libraries[keys]=[libs]
            self.dict_libraries={k:set(v) for k,v in self.dict_libraries.items()}

    def get_library(self):
        self.list_files(self.path)
        self.identify_libraries()
        self.extract_libraries()