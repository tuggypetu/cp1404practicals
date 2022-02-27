"""Temperature kivy"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty


class TemperatureConvert(App):
    """Kivy app to convert Fahrenheit and Celsius temperatures"""
    temp_message = StringProperty()

    def __init__(self, **kwargs):
        """Construct main app"""
        super().__init__(**kwargs)

    def build(self):
        """Build Kivy GUI"""
        self.title = 'Convert Fahrenheit and Celsius Temperatures'
        self.root = Builder.load_file('temperatures2.kv')
        self.temp_message = 'Enter temperature to convert'
        return self.root

    def show_temp(self, temp):
        """Calculate and show temperature"""
        try:
            temp = float(temp)
        except ValueError:
            self.temp_message = 'Enter a valid temperature number\nClick button to choose which temperature to convert'
        else:
            show_temp = f"{temp}°C  =       {temp * 9.0 / 5 + 32}°F\n\n" \
                        f"{temp}°F  =       {((temp - 32) * 5) / 9}°C"
            self.temp_message = show_temp

    def handle_up_down(self, value, up_down):
        """handle when up or down is clicked in kivy app"""
        try:
            result = float(value) + up_down
            self.root.ids.temp_input.text = str(result)
        except ValueError:
            value = 0
            result = float(value) + up_down
            self.root.ids.temp_input.text = str(result)


TemperatureConvert().run()
