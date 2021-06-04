'''
    time kütüphanesi ve temel işlemlerin tanımlanmış olduğu 
sistem kütüphanesini kullanacağız.
timeSleep(saniye)
print => write benzer komutlardır.
flash() -> belleğin kapatıp yeniden çalışmasını sağlar.
Kullanıcıya Hoş Geldin şeklinmde bir çıktı vereceğiz
kullanıcıyı belirli bir süre bekleteceğiz ve sonra sorularmsoracağız 
sonrasında şıkları sıralayacağız
girilen şıkları değerlendireceğiz
Değerlendirme sonucunda kullanıcıya doğru yanlış şeklinde dönüş yapacağız
'''
import time
import sys
print('''
Değerli Öğrenciler Bahar Dönemi Sınavlarına Hoş Geldiniz
''')
time.sleep(1)
print('''
Matematik sınavı başlatılıyor...
''')
time.sleep(1)
print('''
[Soru-1]

Aşağıdaki sayılardan hangileri asal sayıdır ?

A) 3-5-8 B) 1-2-4 C) 17-19-21 D) 2-5-39 E) 3-5-39

[CEVAP SÜRESİ → SINIRSIZ]
''')
a = time.sleep(5)
cevap = input('''
Cevabınız: 
''')
if cevap.lower()=='c':
    print("CEVAP DEĞERLENDİRİLİYOR...")
    for i in range(3,-1,-1):
        time.sleep(1)
        sys.stdout.write(str(i)+' ')
        sys.stdout.flush() #bellekte tutma işlemini bitirir.
    print("Doğru")   
else:
    print("Yanlış")

