from pytube import YouTube

url = 'https://www.youtube.com/watch?v=ZFsHrySUAwc'

video = YouTube(url)
"""
print(video.title) # video başlığı
print(video.thumbnail_url) # küçük resim
print(video.streams.get_highest_resolution())
"""
video.streams.get_highest_resolution().download()
