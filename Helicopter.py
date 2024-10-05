from pydub import AudioSegment
from pydub.playback import play
import time

class Helicopter():


    def __init__(self, nomi, brendi, narxi, max_tezligi = 900, rangi = "white", yolovchilar_soni = 200):
        self.name = nomi
        self.brend = brendi
        self.price = narxi
        self.max_speed = max_tezligi
        self.color = rangi
        self.passengers = yolovchilar_soni
        self.speed = 0

    def info(self):

        print(f"Vertolyot nomi: {self.name}, Brendi: {self.brend}, Narxi: {self.price}, "
              f"Rangi: {self.color}, Yo'lovchilar soni: {self.passengers}")

    def start(self):

        try:

            if self.speed > 0:
                print("Vertolyot allaqachon havoga ko'tarilgan!")
                return

            sound = AudioSegment.from_mp3('uyga vazifa/uyga vazifa_9/boshlash.mp3') 
            print("Vertolyot ishga tushdi...")
            play(sound)
            self.speed = 300
            time.sleep(3)

        except Exception as e:
            self.avariyaa(e)

    def take_off(self):

        try:

            if self.speed < 300:
                print("Vertolyot tezligi oshmoqda!")
                return

            sound = AudioSegment.from_mp3('uyga vazifa/uyga vazifa_9/start.mp3') 
            print("Vertolyot uchmoqda...")
            play(sound)
            self.speed = 600
            time.sleep(3)

        except Exception as e:
            self.avariyaa(e)

    def stop(self):

        try:

            if self.speed == 0:
                print("Vertolyot allaqachon to'xtagan.")
            else:
                sound = AudioSegment.from_mp3('uyga vazifa/uyga vazifa_9/avariya.mp3') 
                print("Vertolyot to'xtadi.")
                play(sound)
                self.speed = 0
                time.sleep(3)

        except Exception as e:
            self.avariyaa(e)

    def tezlik(self, a):

        try:

            if self.speed + a > self.max_speed:
                self.speed = self.max_speed
                print(f"Tezlik oshdi, lekin {self.max_speed} km/soatdan oshib ketdi.")
            else:
                self.speed += a
            print("Tezlik oshdi:", self.speed, "km/soat")

        except Exception as e:
            self.avariyaa(e)

    def tezlik2(self, a):

        try:

            if self.speed - a < 0:
                self.speed = 0
                print("Vertolyot to'xtadi.")
            else:
                self.speed -= a
            print("Vertolyot sekinlashmoqda... Tezlik:", self.speed, "km/soat")

        except Exception as e:
            self.avariyaa(e)

    def avariyaa(self, e):

        print("Vertolyot qulayapti!")
        crash_sound = AudioSegment.from_mp3('uyga vazifa/uyga vazifa_9/avariya.mp3')
        play(crash_sound)
        print(e)

helicopters = []
n = int(input("Nechta vertolyotni uchirmoqchisiz? "))


for i in range(n):
    try:

        nomi = input("Qaysi vertolyotni: ")
        brend = input("Qaysi brenddagisini: ")
        narx = int(input("Qaysi narxdagisini (son kiritishingiz kerak!): "))  
        yolovchi_soni = int(input("Yo'lovchilar soni (son kiritishingiz kerak!): "))  
        helicopters.append(Helicopter(nomi, brend, narx, yolovchilar_soni = yolovchi_soni))

    except ValueError as e:
        print("Noto'g'ri kiritdiz! Faqat son kiritishingiz kerak!")
        crash_sound = AudioSegment.from_mp3('uyga vazifa/uyga vazifa_9/avariya.mp3')
        play(crash_sound)
        print(e)

for index, helicopter in enumerate(helicopters):
    helicopter.info()
    if index == 0:
        helicopter.start()  
        helicopter.take_off() 
        helicopter.stop()
        helicopter.info()


