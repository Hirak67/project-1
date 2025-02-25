from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = FloatLayout()

        # Background Image
        self.bg = Image(source='background.jpg', allow_stretch=True, keep_ratio=False)
        layout.add_widget(self.bg)

        # Text Section
        title = Label(text="[b]Fall in Love with\nCoffee in Blissful Delight![/b]",
                      markup=True,
                      font_size='24sp',
                      bold=True,
                      color=(1, 1, 1, 1),
                      pos_hint={'center_x': 0.5, 'center_y': 0.55})
        layout.add_widget(title)

        description = Label(text="Welcome to our cozy coffee corner, where\nevery cup is a delightful journey.",
                            font_size='16sp',
                            color=(1, 1, 1, 0.8),
                            pos_hint={'center_x': 0.5, 'center_y': 0.48})
        layout.add_widget(description)

        # Button
        get_started_button = Button(text="Get Started",
                                    size_hint=(0.6, 0.08),
                                    pos_hint={'center_x': 0.5, 'center_y': 0.35},
                                    background_color=(0.5, 0.3, 0.2, 1))
        layout.add_widget(get_started_button)
        
        self.add_widget(layout)

class LunaApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name='home'))
        return sm

if __name__ == '__main__':
    LunaApp().run()
