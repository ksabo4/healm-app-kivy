from kivy.app import App
from kivy.metrics import dp
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget



class StackLayoutExample(StackLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

        #problem : you can't
        for i in range(100):
            b = Button(text=str(i+1), size_hint=(None,None), size=(dp(100), dp(100))) #remember to add the size_hint or Z is going to take the whole place
            self.add_widget(b)



class GraphScreen(Screen):
    pass

class StatusScreen(Screen):
    pass

class StartingScreen(Screen):
    pass

class WindowManager(ScreenManager):
    pass

class TheDesignApp(App):
    pass

TheDesignApp().run()

