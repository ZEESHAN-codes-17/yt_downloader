from pytubefix import YouTube
import os

# Create downloads folder if not exists
if not os.path.exists("downloads"):
    os.makedirs("downloads")

# Step 1: Take video link
link = input("🎥 Enter YouTube video link: ")
yt = YouTube(link)

# Step 2: Show details
print("\n📌 Video Details:")
print("Title:", yt.title)
print("Channel:", yt.author)
print("Duration (min):", round(yt.length / 60, 2))

# Step 3: Ask for format
choice = input("\nDo you want to download Video (max 720p) or Audio? (v/a): ").lower()

if choice == "v":
    print("\nDownloading best available video (up to 720p)... ⏳")
    stream = yt.streams.get_highest_resolution()  # progressive stream (video+audio)
    stream.download("downloads")
    print("✅ Video Downloaded! Saved in 'downloads' folder")

elif choice == "a":
    print("\nDownloading audio... ⏳")
    audio_stream = yt.streams.filter(only_audio=True).first()
    out_file = audio_stream.download("downloads")

    # Convert to .mp3
    base, ext = os.path.splitext(out_file)
    new_file = base + ".mp3" 
    os.rename(out_file, new_file)

    print("✅ Audio Downloaded! Saved in 'downloads' folder")

else:
    print("❌ Invalid choice. Run again.")




