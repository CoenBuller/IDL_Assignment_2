"""This code can be used to load in the data from the website"""

import requests
import io
import zipfile

#The data comes in two resolutions, one of 75x75 img. and one of 150x150 img.
url_75 = 'https://surfdrive.surf.nl/index.php/s/Nznt5c48Mzlb2HY/download?path=%2F&files=A1_data_75.zip'
url_150 = 'https://surfdrive.surf.nl/index.php/s/Nznt5c48Mzlb2HY/download?path=%2F&files=A1_data_150.zip'

r = requests.get(url=url_150) #Specify which data you want to load in
z = zipfile.ZipFile(io.BytesIO(r.content))
z.extractall("./task_2/data_150") #Specify which directory to store the data in 
