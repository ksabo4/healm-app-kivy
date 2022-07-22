from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button


#how you can see the layout box from the python file
class BoxLayoutExample(BoxLayout):
    pass

#main interface
class MainWidget(Widget):
    pass

class TheLabApp(App):
    pass

TheLabApp().run()

#how do we comment in the kv file?


'''
class BoxLayoutExample(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


        self.orientation = "horizontal" #you can also make it vertical (but that would change the orientation of the buttons

        #making buttons:
        b1 = Button(text = "button A")
        b2 = Button(text = "button B")

        #adding the widget in the layout
        self.add_widget(b1)
        self.add_widget(b2)

'''
