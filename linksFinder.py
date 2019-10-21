from utility import *


# iterate through all of the urls
for levelUrl in levelUrls:


        # name folders containing the urls
        # according to urls
        level = findUrlId(levelUrl)

        folders = getFoldersInDirectory()
        
        # check if folder already exists
        if not folders or level not in folders:
                os.mkdir(level)
                
        os.chdir(level)

        existingFiles = getFilesInDirectory()

        # retrieve the page

        if level + ".html" not in getFilesInDirectory(".."):
                print("Level: " + level + " was not saved.")
                print("Now downloading.")
                saveWebPage(levelUrl, ".." + level + ".html")
        
        levelSoup = getLocalSoup(".." + level + ".html")
        

        # iterate through each section
        # and save the corresponding web page

        # sectionLinks = findSectionLinks(levelSoup)
        paragraphs = findParagraphs(levelSoup)
        sectionLinks = findSectionLinks(paragraphs)
        print("Currently going through " + level  + ".")
        
        numLinks = len(sectionLinks)

        for order, sectionLink in enumerate(sectionLinks):
                try:
                        sectionFilename = defineOrderedFilename(order,
                                                                sectionLink)
                except:
                        print("Invalid link: " + sectionLink + ".")
                print("Link " + str(order + 1) + " of " + str(numLinks) + ".")

                
                if sectionFilename in existingFiles:
                        continue
                try: 
                        saveWebPage(sectionLink, sectionFilename)
                except:
                        print("Page does not exist!")
                print("Saved webpage as name: " + sectionFilename + ".")

        # go back into base directory
        os.chdir("..")

        


