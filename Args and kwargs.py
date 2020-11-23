# Compound interest
def final_deposit_amount(*interest, amount=1000):
  for i in interest:
      amount *= 1 + i / 100
  return round(amount, 2)

# function takes several keyword arguments representing musicians and prints the values from the dictionary
'''
tracks = {"Woodkid": {"The Golden Age": "Run Boy Run",
                      "On the Other Side": "Samara"},
          "alt-J": {"This Is All Yours": "Left Hand Free",
                    "RELAXER": "In Cold Blood",
                    "An Awesome Wave": "Breezeblocks"}}
'''
def tracklist(**musicians):
    for musician, albums in musicians.items():
        print(musician)
        for album, track in albums.items():
            print(f"ALBUM: {album} TRACK: {track}")

# Fisher's Iris data set
