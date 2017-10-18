from kivy.config import Config
Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '300')
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from qlist import QList

class FinishScreen(Screen):
    pass

class MenuScreen(Screen):
    pass

class FlashCard(Screen):
    l = QList()
    qa = l.getFirst()
    question = StringProperty(qa.question)
    answer = StringProperty()
    score = StringProperty(str(qa.score))

    count = 0
    def update(self):
        if self.count % 2 == 0:
            self.answer = self.qa.answer
            self.count = 1
            self.ids.correct_button.background_color = [0, 255, 0, .6]
            self.ids.incorrect_button.background_color = [255, 0, 0, .6]
            self.ids.reveal_button.background_color = [1, 1, 1, .3]

    def next(self):
        self.count = 0
        self.qa = self.qa.next
        self.score = str(self.qa.score)
        self.answer = ""
        self.question = self.qa.question

        self.ids.correct_button.background_color = [0, 255, 0, .1]
        self.ids.incorrect_button.background_color = [255, 0, 0, .1]
        self.ids.reveal_button.background_color = [1, 1, 1, .6]

    def correct(self):
        if self.count % 2 is 1:
            self.qa.score += 1
            if self.qa.score is 3:
                if self.l.delete(self.qa) is True:
                    self.manager.current = "finish"

            self.next()

    def incorrect(self):
        if self.count % 2 is 1:
            if self.qa.score > 0:
                self.qa.score -= 1
            self.next()

class FlashCardApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(FlashCard(name='main'))
        sm.add_widget(FinishScreen(name='finish'))
        return sm

if __name__ == "__main__":
    FlashCardApp().run()
