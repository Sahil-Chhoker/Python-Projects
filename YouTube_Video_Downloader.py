from pytube import YouTube

link = input("Enter the YouTube video URL: ")
yt = YouTube(link)

print(f"You selected '{yt.title}' as your file.")

print("Are you sure you want to download this file (yes/no): ")
user_input = input()

if user_input.lower() == "yes":
    resolution = input("Enter the desired resolution: ")

    yd = yt.streams.filter(res=resolution).first()

    if yd is not None:
        print(f"Downloading '{yt.title}' with resolution {resolution}...")
        yd.download('D:\Python\Test')
        print("Download complete!")
    else:
        print(f"No stream found with resolution {resolution}.")
else:
    print("Download canceled.")
