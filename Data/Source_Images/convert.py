import fdsa 
import json 
import os
f = open("data_train.txt","w")
for filename in os.listdir("Training_Images"):
    if filename.endswith("txt") :
        nf = open("./Training_Images/"+filename,'r')
        line = nf.read()
        f.write("/media/mostafa/Mostafa/internship/TrainYourOwnYOLO/Data/Source_Images/Training_Images/vott-csv-export/"+filename[:13] +" "+line)
#/media/mostafa/Mostafa/internship/TrainYourOwnYOLO/Data/Source_Images/Training_Images/vott-csv-export/data_train.txt