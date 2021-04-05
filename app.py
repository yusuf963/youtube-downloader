from pytube import YouTube
print('\n')
url = input("Enter url here: ")
video = YouTube(url)
#  .streams.first().download()
# print(video.titlrle)

for vid in video.streams:
    print(vid)
