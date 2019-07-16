from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView

from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout

#размер окна
from kivy.config import Config
Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '500')
Config.set('graphics', 'height', '600')

# Контакты
def contactim():
    f = open('contact.txt', 'r')
    imena = f.readlines()[5::2]
    for i in range(0, len (imena)):
        imena[i] = imena[i][:-1]
    f.close()
    return imena

def contactem():
    f = open('contact.txt', 'r')
    ema = f.readlines()[6::2]
    for i in range(0, len (ema)):
        ema[i] = ema[i][:-1]
    f.close()
    return ema


class Contacti(App):
    def build(self):
        self.anx = AnchorLayout()

        self.osn = Image(source='Fonn.jpg')
        self.anx.add_widget(self.osn)
        self.bl = BoxLayout( orientation='vertical', padding=[15, 10], spacing=5)

        self.gll = GridLayout(minimum_height= 20, cols=1, size_hint=(1 , None) , height=100)
        self.gll.bind(minimum_height=self.gll.setter('height'))

        self.scrol = ScrollView(bar_width= 10, bar_color= [1, 0, 0, 1], effect_cls= "ScrollEffect", scroll_type= ['bars'], size_hint=(1, None), do_scroll_y=True,)

        self.pcontactim = contactim()
        self.pcontactem = contactem()

        for x in range(0, len(self.pcontactim)):
            self.gll.add_widget(Label(text=self.pcontactim[x] + ":   " + self.pcontactem[x], height=40,halign="right", size_hint=(1, None), font_size=20 ))

        self.scrol.add_widget(self.gll)

        self.gl = GridLayout( rows = 2, spacing=3, size_hint=(1, None) , width=0, row_default_height=10)

        self.bl.add_widget(Label(text = "Список контактов", font_size='50sp', size_hint=(1, .5)))# назв

        self.bl.add_widget(self.scrol)# списки

        self.bl.add_widget(Label(text = "Добавить контакт",font_size='40sp', size_hint=(1, .5)))

        self.txima = TextInput(hint_text = "имя", height=60)
        self.txema = TextInput(hint_text = "@email", height=60)
        self.btn = Button(text="Сохранить" ,on_press =self.soxrcont, background_color= [0.2, .8, 0.3, 1], background_normal= '')

        self.gl.add_widget(self.txima)
        self.gl.add_widget(self.txema)
        self.gl.add_widget(Label(text = "       "))
        self.gl.add_widget(self.btn)
        self.bl.add_widget(self.gl)

        self.bl.add_widget(BoxLayout())
        self.anx.add_widget(self.bl)
        return self.anx

    def soxrcont(self, instance):
        f = open('contact.txt', 'a')
        if self.txima.text != "" and self.txema.text != "" and "@" in self.txema.text and "." in self.txema.text:
            f.write(self.txima.text + "\n")
            f.write(self.txema.text + "\n")
            self.txima.text = ""
            self.txema.text = ""
            self.btn.text = "Сохранено"
        f.close()

if __name__ == "__main__":
    Contacti().run()