import os
from code_challenge_06_functions import *

os.system("clear")

alba_url = "http://www.alba.co.kr"

links = []

links = get_link(alba_url)

employment_info = []

for link in links:
    employment_info=get_info(link[1])
    save_to_file(link[0], employment_info)




    




