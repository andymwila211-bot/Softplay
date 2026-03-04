from kivymd.app import MDApp
from kivy.lang import Builder

KV = '''
MDScreen:
    md_bg_color: 0, 0, 0, 1
    MDCard:
        size_hint: .8, .6
        pos_hint: {"center_x": .5, "center_y": .5}
        elevation: 4
        md_bg_color: 1, 1, 1, 0.1 
        radius: [25, 25, 25, 25]
        MDLabel:
            text: "Softplay Glass Active"
            halign: "center"
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 0.8
'''

class MainApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

MainApp().run()
