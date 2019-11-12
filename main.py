
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtCore import Qt
import pygame.midi
import time
import random
# 54 56 DSGH 82 119 117 98

soundduration = 0
soundvolume = 0
pygame.midi.init()
player = pygame.midi.Output(0)

player.set_instrument(40)

class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)

        self.iter_count = 5

        self.zv = 2


        self.volume = 127

        self.timedur = 0.5

        self.isgen = False

        self.genbut.clicked.connect(self.switchtoon)

        self.A.clicked.connect(self.soundA)

        self.B.clicked.connect(self.soundB)

        self.C.clicked.connect(self.soundC)

        self.D.clicked.connect(self.soundD)

        self.E.clicked.connect(self.soundE)

        self.F.clicked.connect(self.soundF)

        self.G.clicked.connect(self.soundG)

        self.listWidget.itemActivated.connect(self.itemActivated_event)

        # 54 56 DSGH 82 119 117 98
        self.listWidget.addItem("56  ---Оркестровый акцент")
        self.listWidget.addItem("82  ---пилотная волна")
        self.listWidget.addItem("119 ---Электробарабаны")
        self.listWidget.addItem("117 ---Тайко")
        self.listWidget.addItem("98  ---саундтрэк")

        self.listWidget.addItem("1 Акустический рояль")
        self.listWidget.addItem("2 Акустическое пианино")
        self.listWidget.addItem("3 Электрический рояль")
        self.listWidget.addItem("4 Фортепиано")
        self.listWidget.addItem("5 Электрическое пианино")
        self.listWidget.addItem("6 Электрическое пианино")
        self.listWidget.addItem("7 Клавесин")
        self.listWidget.addItem("8 Клавинет")
        self.listWidget.addItem("9 Челеста")
        self.listWidget.addItem("10 Колокольчики")
        self.listWidget.addItem("11 Музыкальная шкатулка")
        self.listWidget.addItem("12 Вибрафон")
        self.listWidget.addItem("13 Маримба")
        self.listWidget.addItem("14 Ксилофон")
        self.listWidget.addItem("15 Колокола")
        self.listWidget.addItem("16 Цимбалы")
        self.listWidget.addItem("17 Орган Хаммонда")
        self.listWidget.addItem("18 Перкуссионный орган")
        self.listWidget.addItem("19 Рок-орган")
        self.listWidget.addItem("20 Церковный орган")
        self.listWidget.addItem("21 Тростниковый орган")
        self.listWidget.addItem("22 Аккордеон")
        self.listWidget.addItem("23 Гармоника")
        self.listWidget.addItem("24 Бандонеон")
        self.listWidget.addItem("25 Акустическая гитара")
        self.listWidget.addItem("26 Акустическая гитара")
        self.listWidget.addItem("27 Электрогитара (джаз)")
        self.listWidget.addItem("28 Электрогитара (чистый звук)")
        self.listWidget.addItem("29 Электрогитара (с приемом palm mute)")
        self.listWidget.addItem("30 Перегруженная электрогитара")
        self.listWidget.addItem("31 Дисторшн-электрогитара")
        self.listWidget.addItem("32 Гитарные флажолеты")
        self.listWidget.addItem("33 Акустический бас")
        self.listWidget.addItem("34 Электрическая бас-гитара (палец)")
        self.listWidget.addItem("35 Электрическая бас-гитара (медиатор)")
        self.listWidget.addItem("36 Безладовый бас")
        self.listWidget.addItem("37 Слэп-бас")
        self.listWidget.addItem("38 Слэп-бас")
        self.listWidget.addItem("39 Синтезаторный бас")
        self.listWidget.addItem("40 Синтезаторный бас")
        self.listWidget.addItem("41 Скрипка")
        self.listWidget.addItem("42 Виола")
        self.listWidget.addItem("43 Виолончель")
        self.listWidget.addItem("44 Контрабас")
        self.listWidget.addItem("45 Скрипичное тремоло")
        self.listWidget.addItem("46 Скрипичное пиццикато")
        self.listWidget.addItem("47 Арфа")
        self.listWidget.addItem("48 Тимпан")
        self.listWidget.addItem("49 Струнный оркестр")
        self.listWidget.addItem("50 Струнный оркестр")
        self.listWidget.addItem("51 Синтезаторный оркестр")
        self.listWidget.addItem("52 Синтезаторный оркестр")
        self.listWidget.addItem("53 Хор, поющий «А»")
        self.listWidget.addItem("54 Голос, поющий «О»")
        self.listWidget.addItem("55 Синтезаторный хор")
        self.listWidget.addItem("56 Оркестровый акцент")
        self.listWidget.addItem("57 Труба")
        self.listWidget.addItem("58 Тромбон")
        self.listWidget.addItem("59 Туба")
        self.listWidget.addItem("60 Приглушенная труба")
        self.listWidget.addItem("61 Валторна")
        self.listWidget.addItem("62 Духовой оркестр")
        self.listWidget.addItem("63 Синтезаторные духовые")
        self.listWidget.addItem("64 Синтезаторные духовые")
        self.listWidget.addItem("65 Сопрано-саксофон")
        self.listWidget.addItem("66 Альт-саксофон")
        self.listWidget.addItem("67 Тенор-саксофон")
        self.listWidget.addItem("68 Баритон-саксофон")
        self.listWidget.addItem("69 Гобой")
        self.listWidget.addItem("70 Английский рожок")
        self.listWidget.addItem("71 Фагот")
        self.listWidget.addItem("72 Кларнет")
        self.listWidget.addItem("73 Пикколо")
        self.listWidget.addItem("74 Флейта")
        self.listWidget.addItem("75 Блокфлейта")
        self.listWidget.addItem("76 Флейта Пана")
        self.listWidget.addItem("77 Бутылочные горлышки")
        self.listWidget.addItem("78 Сякухати")
        self.listWidget.addItem("79 Свисток")
        self.listWidget.addItem("80 Окарина")
        self.listWidget.addItem("81 меандр")
        self.listWidget.addItem("82 пилотная волна")
        self.listWidget.addItem("83 каллиопа")
        self.listWidget.addItem("84 чифф")
        self.listWidget.addItem("85 чаранг")
        self.listWidget.addItem("86 голос")
        self.listWidget.addItem("87 квинта")
        self.listWidget.addItem("88 бас и ведущий голос")
        self.listWidget.addItem("89 Нью Эйдж")
        self.listWidget.addItem("90 теплый звук")
        self.listWidget.addItem("91 полисинтезатор")
        self.listWidget.addItem("92 хор")
        self.listWidget.addItem("93 искривленный звук")
        self.listWidget.addItem("94 металлический звук")
        self.listWidget.addItem("95 гало")
        self.listWidget.addItem("96 свип")
        self.listWidget.addItem("97 дождь")
        self.listWidget.addItem("98 саундтрэк")
        self.listWidget.addItem("99 кристалл")
        self.listWidget.addItem("100 атмосфера")
        self.listWidget.addItem("101 яркость")
        self.listWidget.addItem("102 гоблины")
        self.listWidget.addItem("103 эхо")
        self.listWidget.addItem("104 сай-фай")
        self.listWidget.addItem("105 Ситар")
        self.listWidget.addItem("106 Банджо")
        self.listWidget.addItem("107 Сямисэн")
        self.listWidget.addItem("108 Кото")
        self.listWidget.addItem("109 Калимба")
        self.listWidget.addItem("110 Волынка")
        self.listWidget.addItem("111 Фиддл")
        self.listWidget.addItem("112 Шахнай")
        self.listWidget.addItem("113 Медные колокольчики")
        self.listWidget.addItem("114 Агого")
        self.listWidget.addItem("115 Стальные барабаны")
        self.listWidget.addItem("116 Деревянная коробочка")
        self.listWidget.addItem("117 Тайко")
        self.listWidget.addItem("118 Мелодичный том-том")
        self.listWidget.addItem("119 Электробарабаны")
        self.listWidget.addItem("120 Цимбалы задом наперед")
        self.listWidget.addItem("121 Шум гитарных струн")
        self.listWidget.addItem("122 Дыхание")
        self.listWidget.addItem("123 Шум прибоя")
        self.listWidget.addItem("124 Птичья трель")
        self.listWidget.addItem("125 Телефонный звонок")
        self.listWidget.addItem("126 Шум вертолета")
        self.listWidget.addItem("127 Аплодисменты")
        self.listWidget.addItem("128 Выстрел")
        self.duration_slider.valueChanged[int].connect(self.changeValueDur)
        self.volume_slider.valueChanged[int].connect(self.changeVolume)

        self.iter_slider.valueChanged[int].connect(self.changeValueIter)
        self.zv_slider.valueChanged[int].connect(self.changeValueZv)

    def changeValueIter(self, value):
        self.iter_count = value

    def changeValueZv(self, value):
        self.zv = value

    def changeVolume(self, valur):
        self.volume = valur

    def changeValueDur(self, value):
        self.timedur = value/10

    def itemActivated_event(self, item):
        print(item.text())
        self.your_instrument.setText("Ваш инструмент " + item.text())
        print("еще жив")
        self.instsetter(item.text())

    def instsetter(self, nazvanie):
        print("еще жив пока")
        interr = str(nazvanie).split()
        player.set_instrument(int(interr[0]) - 1)


    def keyPressEvent(self, event):
        if event.key() == Qt.Key_A:
            self.soundA()

        if event.key() == Qt.Key_S:
            self.soundB()

        if event.key() == Qt.Key_D:
            self.soundC()

        if event.key() == Qt.Key_F:
            self.soundD()

        if event.key() == Qt.Key_G:
            self.soundE()

        if event.key() == Qt.Key_H:
            self.soundF()

        if event.key() == Qt.Key_J:
            self.soundG()

    do = pygame.midi.frequency_to_midi(261.63)
    re = pygame.midi.frequency_to_midi(293.66)
    mi = pygame.midi.frequency_to_midi(329.63)
    fa = pygame.midi.frequency_to_midi(349.23)
    sol = pygame.midi.frequency_to_midi(392.00)
    la = pygame.midi.frequency_to_midi(440.00)
    si = pygame.midi.frequency_to_midi(493.88)


    def sounddurup(self):
        if self.timedur + 0.1 > 1:
            self.timedur = 1
        else:
            self.timedur += 0.1
        self.duration_slider.setValue(int(self.timedur))
        print(self.timedur)

    def sounddurdown(self):
        if self.timedur - 0.1 < 0:
            self.timedur = 0
        else:
            self.timedur -= 0.1
        print(self.timedur)
        self.duration_slider.setValue(int(self.timedur))

    def soundA(self):
        player.note_on(self.do, self.volume)
        time.sleep(self.timedur)
        player.note_off(self.do, self.volume)

    def soundB(self):
        player.note_on(self.re, self.volume)
        time.sleep(self.timedur)
        player.note_off(self.re, self.volume)

    def soundC(self):
        player.note_on(self.mi, self.volume)
        time.sleep(self.timedur)
        player.note_off(self.mi, self.volume)

    def soundD(self):
        player.note_on(self.fa, self.volume)
        time.sleep(self.timedur)
        player.note_off(self.fa, self.volume)

    def soundE(self):
        player.note_on(self.sol, self.volume)
        time.sleep(self.timedur)
        player.note_off(self.sol, self.volume)

    def soundF(self):
        player.note_on(self.la, self.volume)
        time.sleep(self.timedur)
        player.note_off(self.la, self.volume)

    def soundG(self):
        player.note_on(self.si, self.volume)
        time.sleep(self.timedur)
        player.note_off(self.si, self.volume)

    def lastnote(self, midinote):
        self.lastnote = midinote

    def makemus(self):
            note = random.randint(1, 7)
            print(note)
            if note == 1:
                self.soundA()

            if note == 2:
                self.soundB()

            if note == 3:
                self.soundC()

            if note == 4:
                self.soundD()

            if note == 5:
                self.soundE()

            if note == 6:
                self.soundF()

            if note == 7:
                self.soundG()


    def switchtoon(self):
        for i in range(self.iter_count):
            for j in range(self.zv):
                self.makemus()
            print("---iter---" + str(i))
            time.sleep(self.timedur)



app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())