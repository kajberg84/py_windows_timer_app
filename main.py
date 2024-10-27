from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
    def build(self):
        # Create a layout to organize widgets
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Add a label to the layoutsource
        self.label = Label(text=" Hello!")
        layout.add_widget(self.label)

        # Add a button to the layout
        button = Button(text="Click me!")
        button.bind(on_press=self.on_button_click)
        layout.add_widget(button)

        return layout

    def on_button_click(self, instance):
        # Update the label text when the button is clicked
        self.label.text = "Hello, Kaj :D !"

if __name__ == "__main__":
    MyApp().run()