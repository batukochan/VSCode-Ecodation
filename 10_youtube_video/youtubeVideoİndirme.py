from pytube import YouTube

url = 'https://www.youtube.com/watch?v=AMpkXMU0IkI'

video = YouTube(url)
"""
print(video.title) # video başlığı
print(video.thumbnail_url) # küçük resim
print(video.streams.get_highest_resolution())
"""
video.streams.get_highest_resolution().download()

path = 'C:\Users\batuh\Desktop\VSCode-Python Dersleri\JavaScript ile Güncel Hava Durumu Uygulaması - OpenWeather API Kullanımı.mp4'