import csv
import random as rnd

# Random Song List
genre_list = ["HipHop", "Hindi Jazz", "English Pop", "Hindi Pop", "Bhajan",
              "Bengali Classical", "Bengali Jazz", "English Jazz", "EDM",
              "Classical", "Dance Street", "Bhojpuri", "Hindi Lite", "English Lite",
              "Indie Pop", "English Classical"
              ]

# Create a CSV for data processing and ML Training.
with open("genre_detect.csv", mode="w") as genre:
    genre_writer = csv.writer(genre, delimiter=',')
    for i in range(10000):

        # Generate some data randomly. It doesn't have much of a pattern.
        # CSV list of ==> {age}, {gender}, {genre}
        age = rnd.randint(15, 55)
        gender = rnd.randint(0, 1)
        index = rnd.randint(0, len(genre_list)-1)

        # Write out to CSV File.
        genre_writer.writerow([f'{age}', f'{gender}', f'{genre_list[index]}'])
