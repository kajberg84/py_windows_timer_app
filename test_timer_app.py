import kivy
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

kivy.require('2.3.0')  # Specify the Kivy version

class TimerApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Label to display the timer
        self.timer_label = Label(text='00:00:00', font_size=50)
        self.layout.add_widget(self.timer_label)

        # Start, Stop, Reset buttons
        self.start_button = Button(text='Start', on_press=self.start_timer)
        self.stop_button = Button(text='Stop', on_press=self.stop_timer)
        self.reset_button = Button(text='Reset', on_press=self.reset_timer)

        # Add buttons to layout
        self.layout.add_widget(self.start_button)
        self.layout.add_widget(self.stop_button)
        self.layout.add_widget(self.reset_button)

        # Timer variables
        self.running = False
        self.elapsed_time = 0  # in seconds
        self.timer_event = None

        return self.layout

    def update_timer(self, dt):
        if self.running:
            self.elapsed_time += 1
            self.timer_label.text = self.format_time(self.elapsed_time)

    def start_timer(self, instance):
        if not self.running:
            self.running = True
            self.timer_event = Clock.schedule_interval(self.update_timer, 1)

    def stop_timer(self, instance):
        if self.running:
            self.running = False
            Clock.unschedule(self.timer_event)

    def reset_timer(self, instance):
        self.running = False
        Clock.unschedule(self.timer_event)
        self.elapsed_time = 0
        self.timer_label.text = '00:00:00'

    def format_time(self, seconds):
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        seconds = seconds % 60
        return f"{hours:02}:{minutes:02}:{seconds:02}"

if __name__ == '__main__':
    TimerApp().run()
