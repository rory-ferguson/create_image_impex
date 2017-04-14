# ImpexPython
small script to create an impex import/export file to import images into Hybris hMC

File types supported are JPG, PNG & GIF

# Code Example
This is a small code snippet

```python
def mainclass():

        def movefileworker():
            os.chdir(rootPath)  # Changes current working directory (cwd)

            imgPath = os.path.dirname(outPutDir + '\\Images\\')
            imgDirectory = os.listdir(imgPath)

            for filename in imgDirectory:
                if filename.endswith('.jpg') or filename.endswith('.png') or filename.endswith('.gif'):
                    moveFileData.append(filename)

            os.chdir(outPutDir + "\\") # Zip \Images\ and contents

            def zipdir(path, ziph):
                for root, dirs, files in os.walk(path):
                    for file in files:
                        ziph.write(os.path.relpath(os.path.join(root, file), os.path.join(path, '..')))

            if __name__ == '__main__':
                zipf = zipfile.ZipFile('images.zip', 'w', zipfile.ZIP_DEFLATED)
                zipdir('images/', zipf)
                zipf.close()
```

# Usage

```
python CreateImpexAtPath.py
```
Copy the directory path where the images folder can be found (note that the images must be inside a folder called images)

```
What is the Directory Path?
```
Paste the path in the shell

```
UK, US or DE?
```
Choose which hMC env the impex is related to
