from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.config import Config
from kivy.properties import ObjectProperty
from kivy.uix.widget import Widget
from qlist import QList

Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '500')

class MainView(BoxLayout):
    l = QList()
    qa = l.getFirst()
    question = StringProperty(qa.question)
    answer = StringProperty()

    count = 0
    def update(self):
        if self.count % 2 == 0:
            self.answer = self.qa.answer
            self.count = 1
            self.ids.correct_button.background_color = [0, 255, 0, 1]
            self.ids.incorrect_button.background_color = [255, 0, 0, 1]
            self.ids.reveal_button.background_color = [1, 1, 1, 0]

    def next(self):
        self.count = 0
        self.qa = self.qa.next
        self.answer = ""
        self.question = self.qa.question

        self.ids.correct_button.background_color = [0, 255, 0, 0]
        self.ids.incorrect_button.background_color = [255, 0, 0, 0]
        self.ids.reveal_button.background_color = [1, 1, 1, 1]

    def correct(self):
        if self.count % 2 is 1:
            print("correct")
            self.next()

    def incorrect(self):
        if self.count % 2 is 1:
            print("incorrect")
            self.next()

class FlashCardApp(App):
    def build(self):
        return MainView()

if __name__ == "__main__":
    FlashCardApp().run()
