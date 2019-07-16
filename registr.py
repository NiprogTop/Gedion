from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput

from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout

#размер окна
from kivy.config import Config
Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '500')
Config.set('graphics', 'height', '600')

class Contacti(App):
    def build(self):
        self.anx = AnchorLayout()

        self.osn = Image(source='Fonn.jpg')
        self.anx.add_widget(self.osn)
        self.bl = BoxLayout(orientation='vertical', padding=[15, 10], spacing=5, size_hint=(.5, .5))

        self.bl.add_widget(Label(text="Упраление акаунтом", font_size='50sp', size_hint=(1, 1), valign ="center"))  # назв

        self.txima = TextInput(hint_text="Ваш email:", height=60)
        self.txema = TextInput(hint_text="Пароль:", height=60)
        self.btn = Button(text="Сохранить",font_size='30sp',
                          on_press=self.soxronpar,
                          background_color=[0.2, .8, 0.3, 1], background_normal='')

        self.bl.add_widget(self.txima)
        self.bl.add_widget(self.txema)
        self.bl.add_widget(self.btn)

        self.anx.add_widget(self.bl)

        return self.anx
    def soxronpar(self, instance):
        #f = open('dobav.txt', 'w')
        if self.txima.text != "" and self.txema.text != "" and "@" in self.txima.text and "." in self.txima.text:
            f = open('dobav.txt', 'w')
            f.write(self.txima.text + "\n")
            f.write(self.txema.text + "\n")
            self.txima.text = ""
            self.txema.text = ""
            self.btn.text = "Сохранено"
            f.close()

if __name__ == "__main__":
    Contacti().run()