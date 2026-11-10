from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.utils import get_color_from_hex

Window.clearcolor = get_color_from_hex("#FF7F00")

class NarutoApp(App):
    def build(self):
        utama = BoxLayout(orientation="vertical", padding=20, spacing=15)

        judul = Label(
            text="NARUTO APP",
            font_size=38,
            bold=True,
            color=(1, 1, 1, 1),
            size_hint=(1, 0.15)
        )
        utama.add_widget(judul)

        sub = Label(
            text="Dattebayo! Pilih karakter favoritmu!",
            font_size=18,
            color=(1, 1, 1, 1),
            size_hint=(1, 0.1)
        )
        utama.add_widget(sub)

        self.info = Label(
            text="Pencet salah satu karakter di bawah!",
            font_size=20,
            bold=True,
            color=(0, 0, 0, 1),
            size_hint=(1, 0.2)
        )
        utama.add_widget(self.info)

        scroll = ScrollView(size_hint=(1, 0.55))
        daftar = GridLayout(cols=1, spacing=12, size_hint_y=None)
        daftar.bind(minimum_height=daftar.setter("height"))

        karakter = [
            ("Naruto Uzumaki", "Hokage ke-7, Jinchuriki Kurama!"),
            ("Sasuke Uchiha", "Rival Naruto, pengguna Sharingan!"),
            ("Sakura Haruno", "Ninja medis terkuat!"),
            ("Kakashi Hatake", "Guru Tim 7, si Ninja Peniru!"),
            ("Hinata Hyuga", "Pengguna Byakugan!"),
            ("Itachi Uchiha", "Kakak Sasuke!"),
            ("Jiraiya", "Sannin Legendaris, guru Naruto!"),
            ("Madara Uchiha", "Legenda Uchiha!"),
        ]

        for nama, deskripsi in karakter:
            tombol = Button(
                text=nama,
                font_size=22,
                bold=True,
                background_color=get_color_from_hex("#1A1A1A"),
                color=(1, 1, 1, 1),
                size_hint_y=None,
                height=60
            )
            tombol.bind(on_press=lambda x, d=deskripsi, n=nama: self.pilih(n, d))
            daftar.add_widget(tombol)

        scroll.add_widget(daftar)
        utama.add_widget(scroll)
        return utama

    def pilih(self, nama, deskripsi):
        self.info.text = nama + "\n" + deskripsi

if __name__ == "__main__":
    NarutoApp().run()
