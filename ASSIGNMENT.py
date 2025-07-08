class File:
    
    def __init__(self, file_name, file_size):
        self.file_name=file_name
        self.file_size=file_size

class Directory:
    
    def __init__(self, directory_name, parent_directory=None):
        self.directory_name = directory_name
        self.parent_directory = parent_directory
        self.directory_files=[]
        self.sub_directories={}

    def subdirectory_addition(self, sub_directory_name):
        if sub_directory_name not in self.sub_directories:
            new_directory_name=Directory(sub_directory_name,parent_directory=self)
            self.sub_directories[sub_directory_name]= new_directory_name
        return self.sub_directories[sub_directory_name]

    def get_details_subdirectory(self,sub_directory_name):
        return self.sub_directories.get(sub_directory_name, None)

    def file_addition(self,file_name):
        self.directory_files.append(file_name)

    def calculate_size(self):
        size = sum(n.file_size for n in self.directory_files)
        for n1 in self.sub_directories.values():
            size+=n1.calculate_size()
        return size

    def print_directory(self):
        for n in self.directory_files:
            print(f"File Name: {n.file_name} and Size: {n.file_size} KB")
        for n1,n2 in self.sub_directories.items():
            print(f"{n1}/")
            for n3 in n2.directory_files:
                print(f"\tFile Name: {n3.file_name} and Size: {n3.file_size} KB")

class Execution:
    def __init__(self):
        self.root = Directory("root")
        self.cwd = self.root
        self.test_data()

    def test_data(self):
        self.root.file_addition(File("sample_docs.csv", 2))
        photos=self.root.subdirectory_addition("Niteesh")
        photos.file_addition(File("Masters_Certificate.pdf",3))
        photos.file_addition(File("Bachelors_Certificate.pdf",4))
        docs=self.root.subdirectory_addition("Work")
        docs.file_addition(File("testcases.txt",1))
        docs.file_addition(File("results.xlsx",3))

    def call_command_functions(self):
        while True:
            i=input(f"{self.cwd.directory_name}> ").strip().split()
            if not i:
                continue
            command = i[0]
            args = i[1:]

            if command =="cd":
                self.change_directory(args)
            elif command == "ls":
                self.cwd.print_directory()
            elif command == "size":
                print(f"Total Size: {self.cwd.calculate_size()} KB")
            elif command == "mkdir":
                for name in args:
                    self.cwd.subdirectory_addition(name)
            elif command =="cd..":
                if self.cwd.parent_directory:
                    self.cwd = self.cwd.parent_directory
            elif command == "exit":
                break
            else:
                print("Unknown Command")

    def change_directory(self, args):
            if len(args)!=1:
                print("Unknown Command")
                return
            next_dir = self.cwd.get_details_subdirectory(args[0])
            if next_dir:
                self.cwd=next_dir
            else:
                print("Directory not found")
                
    

if __name__=="__main__":
    print("Directory Size Calculator Application: ")
    print("Available Commands: cd, cd.. , ls, size, mkdir,exit: ")
    fs=Execution()
    fs.call_command_functions()
    

    
