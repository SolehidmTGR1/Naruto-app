
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.graphics import Color, Rectangle
from kivy.clock import Clock
import os, math

class PapanPutih(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas.before:
            Color(1, 1, 1, 1)
            self.rect = Rectangle(pos=self.pos, size=self.size)
        self.bind(pos=self.update, size=self.update)
    def update(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size

class KalkulatorApp(App):
    def build(self):
        self.angka = ""
        self.root_layout = FloatLayout()
        self.waktu = 0

        self.daftar_gambar = ['sasuke.jpg', 'naruto.jpg', 'sakura.jpg', 'kakashi.jpg', 'itachi.jpg', 'khoir.jpg']
        self.daftar_nama = ['SASUKE - Chidori!', 'NARUTO - Rasengan!', 'SAKURA - Pukulan Kuat!', 'KAKASHI - Sharingan!', 'ITACHI - Genjutsu!', 'KHOIR - Hokage ke-9!']
        self.daftar_pos_y = [0.35, 0.68, 0.68, 0.35, 0.35, 0.68]

        gambar_ok = []
        nama_ok = []
        pos_ok = []
        for g, n, p in zip(self.daftar_gambar, self.daftar_nama, self.daftar_pos_y):
            if os.path.exists(g):
                gambar_ok.append(g)
                nama_ok.append(n)
                pos_ok.append(p)
        self.daftar_gambar = gambar_ok
        self.daftar_nama = nama_ok
        self.daftar_pos_y = pos_ok

        self.index_gambar = 0
        self.pos_y_saat_ini = self.daftar_pos_y[0]
        self.bg = Image(source=self.daftar_gambar[0], allow_stretch=True, keep_ratio=False, opacity=0.65, size_hint=(1.35, 1.35), pos_hint={'center_x': 0.5, 'center_y': self.pos_y_saat_ini})
        self.root_layout.add_widget(self.bg)

        utama = BoxLayout(orientation='vertical', padding=12, spacing=8, size_hint=(0.96, 0.90), pos_hint={'center_x': 0.5, 'center_y': 0.56})
        self.label_pemeran = Label(text=self.daftar_nama[0] + '  (1/' + str(len(self.daftar_gambar)) + ')', font_size=20, bold=True, color=(0, 0.9, 1, 1), size_hint_y=None, height=38)
        utama.add_widget(self.label_pemeran)

        baris_animasi = BoxLayout(orientation='horizontal', spacing=8, size_hint_y=None, height=45)
        btn_next = Button(text='GANTI ➜', font_size=18, bold=True, background_color=(0, 0.6, 1, 1), color=(1,1,1,1), background_normal='')
        btn_next.bind(on_press=self.ganti_gambar)
        baris_animasi.add_widget(btn_next)
        self.btn_auto = Button(text='AUTO: HIDUP', font_size=16, bold=True, background_color=(0, 0.8, 0.3, 1), color=(1,1,1,1), background_normal='')
        self.btn_auto.bind(on_press=self.atur_auto)
        baris_animasi.add_widget(self.btn_auto)
        utama.add_widget(baris_animasi)

        self.label_riwayat = Label(text='', font_size=16, bold=True, color=(1, 1, 0, 1), size_hint_y=None, height=24)
        utama.add_widget(self.label_riwayat)

        papan = PapanPutih(size_hint_y=None, height=80, padding=5)
        self.layar = Label(text='0', font_size=48, bold=True, color=(0, 0, 0, 1))
        papan.add_widget(self.layar)
        utama.add_widget(papan)

        tombol_grid = GridLayout(cols=4, spacing=10, size_hint_y=None, height=380)
        daftar = [
            ('C', (1, 0.1, 0.1, 1), (1, 1, 1, 1)),
            ('Hapus', (1, 0.55, 0, 1), (1, 1, 1, 1)),
            ('%', (0.6, 0.1, 1, 1), (1, 1, 1, 1)),
            ('/', (0, 0.5, 1, 1), (1, 1, 1, 1)),
            ('7', (1, 1, 1, 1), (0, 0, 0, 1)),
            ('8', (1, 1, 1, 1), (0, 0, 0, 1)),
            ('9', (1, 1, 1, 1), (0, 0, 0, 1)),
            ('x', (1, 0.7, 0, 1), (0, 0, 0, 1)),
            ('4', (1, 1, 1, 1), (0, 0, 0, 1)),
            ('5', (1, 1, 1, 1), (0, 0, 0, 1)),
            ('6', (1, 1, 1, 1), (0, 0, 0, 1)),
            ('-', (1, 0.9, 0, 1), (0, 0, 0, 1)),
            ('1', (1, 1, 1, 1), (0, 0, 0, 1)),
            ('2', (1, 1, 1, 1), (0, 0, 0, 1)),
            ('3', (1, 1, 1, 1), (0, 0, 0, 1)),
            ('+', (0, 0.9, 0.3, 1), (1, 1, 1, 1)),
            ('0', (1, 1, 1, 1), (0, 0, 0, 1)),
            ('00', (1, 1, 1, 1), (0, 0, 0, 1)),
            ('.', (1, 1, 1, 1), (0, 0, 0, 1)),
            ('=', (0, 0.8, 0.1, 1), (1, 1, 1, 1)),
        ]
        for teks, warna, warna_tulisan in daftar:
            t = Button(text=teks, font_size=28, bold=True, background_color=warna, color=warna_tulisan, background_normal='')
            t.bind(on_press=self.pencet)
            tombol_grid.add_widget(t)

        utama.add_widget(tombol_grid)
        self.root_layout.add_widget(utama)

        tulisan_bawah = Label(text='Kalkulator dari Hokage ke-9 KHOIR', font_size=17, bold=True, color=(1, 1, 0, 1), size_hint=(0.96, None), height=30, pos_hint={'center_x': 0.5, 'y': 0.01})
        self.root_layout.add_widget(tulisan_bawah)

        self.auto_hidup = True
        self.jadwal = Clock.schedule_interval(self.ganti_gambar, 3)
        Clock.schedule_interval(self.goyang, 0.05)
        return self.root_layout

    def goyang(self, *args):
        self.waktu += 0.05
        geser_x = 0.5 + 0.02 * math.sin(self.waktu * 2)
        self.bg.pos_hint = {'center_x': geser_x, 'center_y': self.pos_y_saat_ini}
        terang = 0.7 + 0.3 * math.sin(self.waktu * 4)
        self.label_pemeran.color = (0, terang, 1, 1)

    def ganti_gambar(self, *args):
        self.index_gambar = (self.index_gambar + 1) % len(self.daftar_gambar)
        self.bg.source = self.daftar_gambar[self.index_gambar]
        self.pos_y_saat_ini = self.daftar_pos_y[self.index_gambar]
        self.bg.pos_hint = {'center_x': 0.5, 'center_y': self.pos_y_saat_ini}
        self.label_pemeran.text = self.daftar_nama[self.index_gambar] + '  (' + str(self.index_gambar+1) + '/' + str(len(self.daftar_gambar)) + ')'

    def atur_auto(self, tombol):
        if self.auto_hidup:
            self.jadwal.cancel()
            self.auto_hidup = False
            self.btn_auto.text = 'AUTO: MATI'
            self.btn_auto.background_color = (1, 0.2, 0.2, 1)
        else:
            self.jadwal = Clock.schedule_interval(self.ganti_gambar, 3)
            self.auto_hidup = True
            self.btn_auto.text = 'AUTO: HIDUP'
            self.btn_auto.background_color = (0, 0.8, 0.3, 1)

    def pencet(self, tombol):
        teks = tombol.text
        if teks == 'C':
            self.angka = ""
            self.layar.text = "0"
            self.label_riwayat.text = ""
        elif teks == 'Hapus':
            self.angka = self.angka[:-1]
            self.layar.text = self.angka if self.angka else "0"
        elif teks == '=':
            # Kalau masih kosong, jangan dihitung
            if not self.angka:
                return
            try:
                # Perbaiki hitungan: x jadi *, % jadi /100
                # Jadi 9%x6 jadi 9/100*6 = 0.54, tidak error lagi
                hitung = self.angka.replace('x', '*')
                hitung = hitung.replace('%', '/100')
                # Kalau terakhirnya masih + - x / , buang dulu
                while hitung and hitung[-1] in ['+', '-', '*', '/']:
                    hitung = hitung[:-1]
                hasil = eval(hitung)
                # Kalau hasilnya bulat, tampilkan tanpa .0, misal 5.0 jadi 5
                if isinstance(hasil, float) and hasil.is_integer():
                    hasil = int(hasil)
                self.label_riwayat.text = self.angka + " ="
                self.layar.text = str(hasil)
                self.angka = str(hasil)
            except:
                self.layar.text = "Coba Lagi Ya!"
                self.angka = ""
        else:
            # Cegah + - x / % dobel, misal 9++6 tidak boleh
            if teks in ['+', '-', 'x', '/', '%'] and self.angka and self.angka[-1] in ['+', '-', 'x', '/', '%', '.']:
                # Ganti yang terakhir saja, jadi tidak dobel
                self.angka = self.angka[:-1] + teks
            elif teks in ['+', '-', 'x', '/', '%'] and not self.angka:
                return
            else:
                self.angka += teks
            self.layar.text = self.angka

KalkulatorApp().run()
