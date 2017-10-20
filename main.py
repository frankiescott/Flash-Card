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
    qlist = QList() #create list and populate with question/answer nodes
    itr = qlist.iter() #iterator handle for the list
    qa = itr.next() #grabs first qa node from the list

    #populate the display information
    question_display = StringProperty(qa.question)
    answer_display = StringProperty()
    score_display = StringProperty(str(qa.score))

    count = 0
    def reveal_answer(self):
        if self.count % 2 == 0:
            self.count = 1
            self.answer_display = self.qa.answer
            self.ids.correct_button.background_color = [0, 255, 0, .6]
            self.ids.incorrect_button.background_color = [255, 0, 0, .6]
            self.ids.reveal_button.background_color = [1, 1, 1, .05]

    #prompt the next question
    def next(self):
        self.count = 0
        self.qa = self.itr.next() #advance the iterator to get the next qa node

        #update display labels
        self.score_display = str(self.qa.score)
        self.answer_display = ""
        self.question_display = self.qa.question
        #adjust button colors
        self.ids.correct_button.background_color = [0, 255, 0, .05]
        self.ids.incorrect_button.background_color = [255, 0, 0, .05]
        self.ids.reveal_button.background_color = [1, 1, 1, .6]

    def correct(self):
        if self.count % 2 is 1: #disables the use of the correct button if the answer hasn't been revealed
            self.qa.score += 1
            if self.qa.score is 2:
                self.qa.hidden = True #hide the question if the user answers correctly twice
                if self.qlist.allhidden() is True: #if all questions are hidden, the set is done
                    self.qlist.reset()
                    self.manager.current = "finish"
            self.next() #go to the next question

    def incorrect(self):
        if self.count % 2 is 1: #disables the use of the incorrect button if the answer hasn't been revealed
            if self.qa.score > 0: #score can't go below 0
                self.qa.score -= 1
            self.next() #go to the next question

    def fontsize(self, text):
        length = len(text)
        if length > 75:
            return "20dp"
        elif length < 20:
            return "80dp"
        dp = 100
        for x in range(1, length):
            dp -= 1

        return "{}dp".format(dp)


class FlashCardApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(FlashCard(name='main'))
        sm.add_widget(FinishScreen(name='finish'))
        return sm

if __name__ == "__main__":
    FlashCardApp().run()
