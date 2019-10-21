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
                print("The level was not saved, so we are going to download it")
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


# # TODO: Find out the elements corresponding

#         # find the elements, and their
#         # corresponding urls
# 	paragraphs = findParagraphs(soup)
# 	sections = findSections(paragraphs)
        
# 	# go through all of the links
# 	existingFiles = os.listdir(path='.')
# 	for number, section in enum(sections):

# 		# check if the file already exists
#                 sectionFilename = section.title + ".html"
#                 if section.title + ".html" in existingFiles:
#                         continue
#                 saveWebPage(section.link, section.title + ".html")


# 	os.chdir('..')


