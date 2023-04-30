import kivy
from kivy.app import App
from kivy.uix.label import Label


class myAPP(App):
    def build(self):
        return Label(text="blyat")
    

if __name__ == "__main__":
    myAPP().run()   