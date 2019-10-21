


# iterate through each folder
folders = getFoldersInDirectory()
for folder in folders:
        files = getFilesInDirectory(folder)
        # sort each of the file in the folder
        # according to regexp
        files.sort(reNumber)
        with folder + ".html" as writeFile:
        # get the soup for the web page
                for file in files:
                        soup = getLocalSoup(file)
                        # find relevant portions
                        relevantText = findText(soup)
                        # write values to a file
                        writeFile.write(relevantText)
        # delete the temporary file?
        # conver the html file to pdf
        writeFile.close()

        convertToPdf(folder)
        
