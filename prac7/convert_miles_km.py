"""Kivy - convert miles to km"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.609344


class ConvertMilesToKMApp(App):
    """ConvertMilesToKMApp is a kivy app to convert miles to km"""
    message = StringProperty()

    def build(self):
        """build the Kivy app from the kv file"""
        self.title = "Convert Miles to Km"
        self.root = Builder.load_file('convert_miles_km.kv')
        self.message = 'Enter miles value in input and click "Convert miles to km" to convert it to km.\n' \
                       'Click up to increase input by 1.\n' \
                       'Click down to decrease input by 1.'
        return self.root

    def handle_convert(self, miles):
        """handle conversion calculation (could be button press or other call), output result to label widget"""
        print('convert miles to km')
        try:
            km = float(miles) * MILES_TO_KM
            self.root.ids.km_output.text = str(km)
        except ValueError:
            self.root.ids.km_output.text = '0.0'

    def handle_up_down(self, value, up_down):
        """handle when up is clicked in kivy app"""
        print('handle up/down')
        try:
            result = float(value) + up_down
            self.root.ids.miles_input.text = str(result)
        except ValueError:
            value = 0
            result = float(value) + up_down
            self.root.ids.miles_input.text = str(result)


ConvertMilesToKMApp().run()
