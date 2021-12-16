#########################
#Description
#########################
#Name: Modifying HTML attributes with beautiful Soup
#Version: 1.0
#Creator: Jorge Martinez Santiago

# Description: 
#This script allows you to load HTML files in batch mode from a source folder.
#From this you can modify an attribute to change the working path.

# Instructions:
    # insert the html files in the source folder
    # Add the path according to the container type
    # Launch the application
    # Check the result in the modify folder


#########################
#Import the libraries
#########################
# Libraries for file handling
import os
import os.path
import sys
#Libraries of web scrapping
from bs4 import BeautifulSoup

#########################
#Variables
#########################

folder_origin = 'origin'
folder_modify='modify'
#List of extensions to be handled by the script
file_ext=('html')

#########################
# Locate files origin
#########################

#List of the files that are located inside the origin folder. 
#It takes the path where the script is located and adds the 
#path of the folder origin variable to it.
root_origin = os.path.join(os.path.dirname(__file__), folder_origin)
root_modify = os.path.join(os.path.dirname(__file__), folder_modify)
files_origin = os.listdir(root_origin)
for file_ori in files_origin:
    # We check that the file belongs to the list of extensions we want to check
    # We normalise to lower case to avoid case sensitive.
    if file_ori.lower().endswith(file_ext):
        try:
            html = open(root_origin+'/'+file_ori)
            soup = BeautifulSoup(html, 'html.parser')
            
            img_source = soup.find_all('img')
            link_source = soup.find_all('link')
            
            #You can add the type of element and the attribute you want to change
            if link_source:
                for item in link_source:
                    item_href = item.attrs['href']    
                    # print(item_href)
                    item['href'] = 'prueba/'+item_href
            
            with open(root_modify+'/'+file_ori, "wb") as f_output:
                f_output.write(soup.prettify("utf-8"))
                print('Processed:', file_ori)
        except:
            print('Error processing file: ',file_ori)
        
