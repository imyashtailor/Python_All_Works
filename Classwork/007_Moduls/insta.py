import instaloader

#create an instance
L = instaloader.Instaloader()

#Target profile
target = "marvellatam"

#download profile
L.download_profile(target, profile_pic_only=True)
print(f"Profile Data for {target} Downloaded!")
