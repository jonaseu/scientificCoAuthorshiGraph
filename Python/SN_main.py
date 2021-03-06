from SN_Analysis import *
from SN_Preprocessing import *
import time 						#For counting the run time

#MAIN
start_time = time.time()

easyChairFileTable 	= getTableFromEasyChair('author_list.xlsx','accepted.html')
authorsList 		= removeAlikeAuthors(easyChairFileTable)
createSocialNetwork(authorsList)
print("--- %s seconds ---" % (time.time() - start_time))