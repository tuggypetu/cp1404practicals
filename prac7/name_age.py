"""Name and age kivy - Dynamically create buttons based on content of dictionary"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty


class DynamicWidgetsApp(App):
    """App to create dynamic widgets on kivy"""
    status_output = StringProperty()

    def __init__(self, **kwargs):
        """Construct main app"""
        super().__init__(**kwargs)
        self.chelsea_player_name_age_dict = {'Kai Havertz': '22', 'Mason Mount': '23', 'Antonio Rudiger': '28',
                                             'Ngolo Kante': '30', 'Jorginho': '30'}

    def build(self):
        """Build the Kivy GUI"""
        self.title = "Create Dynamic Widgets"
        self.root = Builder.load_file('name_age.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Create the widgets"""
        for name in self.chelsea_player_name_age_dict:
            temp_button = Button(text=name)
            temp_button.bind(on_release=self.show_widget_status)
            self.root.ids.new_widgets_box.add_widget(temp_button)

    def show_widget_status(self, name):
        """Show the status of the widgets"""
        name = name.text
        self.status_output = "{}'s age is {}.".format(name, self.chelsea_player_name_age_dict[name])

    def clear_widgets(self):
        """Clear added widgets"""
        self.root.ids.new_widgets_box.clear_widgets()


DynamicWidgetsApp().run()
