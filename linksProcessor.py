from utility import *

# go through each directory
# open each of the files
# parse the relevant portions
# append that portion to a relevant file
# write the contents to a file
folders = getFoldersInDirectory()

directoryFiles = getFilesInDirectory()
for folder in folders:
    # skip if pdf already exists
    pdfFilename = folder + ".pdf"
    htmlFilename = folder + "-scratch.html"
    if pdfFilename in directoryFiles:
        continue
    

    f = open(htmlFilename, "w")
    os.chdir(folder)
    files = getFilesInDirectory()
    files.sort()
    print("Processing files...")
    numFiles = len(files)
    
    for number, file in enumerate(files):
        print("Processing file " + str(number + 1) + " of " + str(numFiles))
        # parse relevant portions
        try:
            text = removeBackslashes(removeEmptyLines(str(findText(getLocalSoup(file)))))
        except:
            print("Error: " + file + " has difficulty converting")
        # append the portion to relevant files
        f.write(text)
        
        # write contents to a file
        # convert to pdf
    f.close()
    os.chdir("..")
    print("Converting " + folder + ".")
    convertHtmlToPdf(htmlFilename, pdfFilename)

    

    

