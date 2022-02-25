"""Kivy to show JCU grade of score"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class JCUGrade(App):
    """Kivy app to JCU grade the score"""

    def build(self):
        """Build the Kivy GUI"""
        Window.size = (400, 200)
        self.title = "JCU Grade teller"
        self.root = Builder.load_file('jcu_grade.kv')
        return self.root

    def tell_grade(self, input_score):
        """Grade Calculator"""
        try:
            value = int(input_score)
        except ValueError:
            print('trash')
            self.root.ids.output_grade.text = 'Enter a valid score to find your JCU Grade!'
        else:
            if value < 0:
                print('trash')
                self.root.ids.output_grade.text = 'Enter a valid score to find your JCU Grade!'
            elif value < 50:
                self.root.ids.output_grade.text = 'Fail!\nYour grade is N.'
            elif value < 100:
                if value < 65:
                    self.root.ids.output_grade.text = 'Pass!\nYour grade is P (Pass).'
                elif value < 75:
                    self.root.ids.output_grade.text = 'Pass!\nYour grade is C (Credit).'
                elif value < 85:
                    self.root.ids.output_grade.text = 'Pass!\nYour grade is D (Distinction).'
                else:
                    self.root.ids.output_grade.text = 'Pass!\nYour grade is HD (High Distinction).'
            else:
                self.root.ids.output_grade.text = 'Enter a valid score to find your JCU Grade!'


JCUGrade().run()
