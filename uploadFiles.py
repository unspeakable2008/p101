import dropbox
import os
from dropbox.files import WriteMode
class Box :
    def __init__(self, accessToken):
        self.accessToken = accessToken
    
    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.accessToken)
        for root, dirs, files in os.walk(file_from):
            for fileName in files:
                print (fileName)
                localPath = os.path.join(root,fileName)
                relativePath = os.path.relpath(localPath, file_from)
                dropboxPath = os.path.join (file_to, relativePath)
                with open(localPath,"rb") as f:
                    dbx.files_upload(f.read(),dropboxPath)
def main():
    accessToken = "RCGVshM00JEAAAAAAAAAAZVUZbGFpyLOS-XkxSB75dFOwUWy0pFu5wDt2gvNMnaK"
    box = Box(accessToken)
    file_from = input("enter the folder name: ")
    file_to = input("enter the folder name: ")
    box.upload_file(file_from, file_to)
    print("Your folder has been moved")
main()
