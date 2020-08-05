import csv
import random as rnd

## Random Song List
genre_list = [  "HipHop", "Hindi Jazz", "English Pop", "Hindi Pop", "Bhajan", 
                "Bengali Classical", "Bengali Jazz", "English Jazz", "EDM", 
                "Classical", "Dance Street", "Bhojpuri", "Hindi Lite", "English Lite"
             ]

## Create a CSV for data processing and ML Training.
with open("genre_detect.csv", mode="w") as genre :
    genre_writer = csv.writer(genre, delimiter=',')
    for i in range(1000) :
    
    ## Generate some data randomly. CSV list of ==> {age}, {gender}, {genre}
        age = rnd.randint(15, 65)
        gender = rnd.randint(0, 1)
        index = rnd.randint(0, len(genre_list)-1)
        
        ## Write out to CSV File. 
        genre_writer.writerow([f'{age}', f'{gender}', f'{genre_list[index]}'])
