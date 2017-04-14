import os
import zipfile

rootPath = os.getcwd()  # C:\Users\rory.ferguson\Desktop\Impex Python

moveFileData = []  # Creates an empty list (array)

outPutDir = input("What is the Directory Path?")  # Prompts user for directory path to \Images\ directory

inputVar = input("UK, US or DE?")  # Prompts user for country
inputCountry = inputVar.lower()


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

        def impexuk():
            # Impex Import
            os.chdir(outPutDir + "\\")
            impeximportdata = []
            impeximportstring = "$lang=en;\n$catalog=newContentCatalog_gb-Staging;\n$version=1;\n$catalogVersion=catalogVersion(catalog(id[default=$catalog]), version[default=$version])[unique=true];\n$contentCV=catalogVersion(catalog(id[default=newContentCatalog_gb-Staging]), version[default=$version])[unique=true];\n$productCV=catalogVersion(catalog(id[default=joulesProductCatalog-Staging]), version[default=$version])[unique=true];\n$picture=media(code, $catalogVersion);\n$siteResource=jar:uk.co.eclipsegroup.joules.initialdata.constants.JoulesInitialDataConstants&/joulesinitialdata/import/contentCatalogs/joulesContentCatalog;\n$media=@media[translator=de.hybris.platform.impex.jalo.media.MediaDataTranslator];\nINSERT Media;code[unique=true];$media;mime[default='image/jpg'];$catalogVersion;folder(qualifier);realfilename"
            with open('MassMediaUploader_gb-staged_import.impex', 'w') as file:
                file.write(impeximportstring)
                for i in range(len(moveFileData)):
                    impeximportdata.append(";" + moveFileData[i] + ";images/" + moveFileData[i] + ";;;images;" + moveFileData[i])
                for line in range(len(impeximportdata)):
                    file.write("\n" + str(impeximportdata[line]))
            file.close()

            # Impex Export
            os.chdir(outPutDir + "\\")
            impexexportdata = []
            impexexportstring = "$catalog=newContentCatalog_gb-Staging;\n$version=1;\n\n" + '"#% impex.setTargetFile("' + '"Media_gb_1.csv"' + '");"' + "\n\nINSERT_UPDATE Media;URL;"
            with open('MassMediaUploader_gb-staged_export.impex', 'w') as file:
                file.write(impexexportstring)
                for i in range(len(moveFileData)):
                    impexexportdata.append(
                        '"#% impex.exportItems("' + '"SELECT {M:pk} FROM {Media as M}, {CatalogVersion as CV}, {Catalog as C} WHERE {M:realfilename}=' "'" +
                        moveFileData[
                            i] + "'" + " AND {M:catalogVersion}={CV:pk} AND {CV:catalog}={C:PK} AND {C:id}=" + "'$catalog' AND {CV:version}='$version'" + '"", Collections.EMPTY_MAP, Collections.singletonList(Item.class), true, true, -1, -1);"')
                for line in range(len(impexexportdata)):
                    file.write("\n" + str(impexexportdata[line]))
            file.close()

        def impexus():
            # Import
            os.chdir(outPutDir + "\\")
            impeximportdata = []
            impeximportstring = "$lang=en_US;\n$catalog=newContentCatalog_us-Staging;\n$version=1;\n$catalogVersion=catalogVersion(catalog(id[default=$catalog]), version[default=$version])[unique=true];\n$contentCV=catalogVersion(catalog(id[default=newContentCatalog_us-Staging]), version[default=$version])[unique=true];\n$productCV=catalogVersion(catalog(id[default=joulesProductCatalog-Staging]), version[default=$version])[unique=true];\n$picture=media(code, $catalogVersion);\n$siteResource=jar:uk.co.eclipsegroup.joules.initialdata.constants.JoulesInitialDataConstants&/joulesinitialdata/import/contentCatalogs/joulesContentCatalog;\n$media=@media[translator=de.hybris.platform.impex.jalo.media.MediaDataTranslator];\nINSERT Media;code[unique=true];$media;mime[default=" + "'image/jpg'];$catalogVersion;folder(qualifier);realfilename"
            with open('MassMediaUploader_en_US-staged_import.impex', 'w') as file:
                file.write(impeximportstring)
                for i in range(len(moveFileData)):
                    impeximportdata.append(";" + moveFileData[i] + ";images/" + moveFileData[i] + ";;;images;" + moveFileData[i])
                for line in range(len(impeximportdata)):
                    file.write("\n" + str(impeximportdata[line]))
            file.close()

            # Impex Export
            os.chdir(outPutDir + "\\")
            impexexportdata = []
            impexexportstring = "$catalog=newContentCatalog_us-Staging;\n$version=1;\n\n" + '"#% impex.setTargetFile("' + '"Media_en_US_1.csv"' + '");"' + "\n\nINSERT_UPDATE Media;URL;"
            with open('MassMediaUploader_en_US-staged_export.impex', 'w') as file:
                file.write(impexexportstring)
                for i in range(len(moveFileData)):
                    impexexportdata.append(
                        '"#% impex.exportItems("' + '"SELECT {M:pk} FROM {Media as M}, {CatalogVersion as CV}, {Catalog as C} WHERE {M:realfilename}=' "'" +
                        moveFileData[
                            i] + "'" + " AND {M:catalogVersion}={CV:pk} AND {CV:catalog}={C:PK} AND {C:id}=" + "'$catalog' AND {CV:version}='$version'" + '"", Collections.EMPTY_MAP, Collections.singletonList(Item.class), true, true, -1, -1);"')
                for line in range(len(impexexportdata)):
                    file.write("\n" + str(impexexportdata[line]))
            file.close()

        def impexde():
            # Import
            os.chdir(outPutDir + "\\")
            impeximportdata = []
            impeximportstring = "$lang=de;\n$catalog=newContentCatalog_de-Staging;\n$version=1;\n$catalogVersion=catalogVersion(catalog(id[default=$catalog]), version[default=$version])[unique=true];\n$contentCV=catalogVersion(catalog(id[default=newContentCatalog_de-Staging]), version[default=$version])[unique=true];\n$productCV=catalogVersion(catalog(id[default=joulesProductCatalog-Staging]), version[default=$version])[unique=true];\n$picture=media(code, $catalogVersion);\n$siteResource=jar:uk.co.eclipsegroup.joules.initialdata.constants.JoulesInitialDataConstants&/joulesinitialdata/import/contentCatalogs/joulesContentCatalog;\n$media=@media[translator=de.hybris.platform.impex.jalo.media.MediaDataTranslator];\nINSERT Media;code[unique=true];$media;mime[default=" + "'image/jpg'];$catalogVersion;folder(qualifier);realfilename"
            with open('MassMediaUploader_de-staged_import.impex', 'w') as file:
                file.write(impeximportstring)
                for i in range(len(moveFileData)):
                    impeximportdata.append(";" + moveFileData[i] + ";images/" + moveFileData[i] + ";;;images;" + moveFileData[i])
                for line in range(len(impeximportdata)):
                    file.write("\n" + str(impeximportdata[line]))
            file.close()

            # Impex Export
            os.chdir(outPutDir + "\\")
            impexexportdata = []
            impexexportstring = "$catalog=newContentCatalog_de-Staging;\n$version=1;\n\n" + '"#% impex.setTargetFile("' + '"Media_de_1.csv"' + '");"' + "\n\nINSERT_UPDATE Media;URL;"
            with open('MassMediaUploader_de-staged_export.impex', 'w') as file:
                file.write(impexexportstring)
                for i in range(len(moveFileData)):
                    impexexportdata.append(
                        '"#% impex.exportItems("' + '"SELECT {M:pk} FROM {Media as M}, {CatalogVersion as CV}, {Catalog as C} WHERE {M:realfilename}=' "'" +
                        moveFileData[
                            i] + "'" + " AND {M:catalogVersion}={CV:pk} AND {CV:catalog}={C:PK} AND {C:id}=" + "'$catalog' AND {CV:version}='$version'" + '"", Collections.EMPTY_MAP, Collections.singletonList(Item.class), true, true, -1, -1);"')
                for line in range(len(impexexportdata)):
                    file.write("\n" + str(impexexportdata[line]))
            file.close()

        if inputCountry == "uk":
            movefileworker()
            impexuk()
            print("Completed")

        elif inputCountry == "us":
            movefileworker()
            impexus()
            print("Completed")

        elif inputCountry == "de":
            movefileworker()
            impexde()
            print("Completed")

        else:
            print("That didn't work, Please type either UK, US or DE")


mainclass()
