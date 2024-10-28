from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

Builder.load_file('layout.kv')

# Load the .kv file
class MainLayout(BoxLayout):
    pass

class BergsTrainingApp(App):
    def build(self):
        return MainLayout()

if __name__ == "__main__":
    BergsTrainingApp().run()