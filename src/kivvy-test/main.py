from kivy.app import App
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button


class WidgetsExample(GridLayout):
    count = 0

    counter_on = BooleanProperty(False)#this variable would be if the counter_on is true, you can increment!

    my_text = StringProperty("Hello!")

    slider_on = BooleanProperty(False)

    text_input_from_user = StringProperty("input from user again! ")

    def on_toggle_button_state(self, widget):
        print("toggle state" + widget.state)
        if widget.state == "normal" :
            widget.text = "OFF"
            self.counter_on = False
        else:
            widget.text = "ON"
            self.counter_on = True

    def on_button_click(self):
        if self.counter_on == True:
            self.count = self.count + 1

            #remember the str() function to convert to string
            self.my_text = "You clicked : " + str(self.count)+ " times!" #changing the text once the button is clicked


    def on_switch_active(self, widget):
        print("Switch state: " + str(widget.active))
        if widget.active == "True":
            self.slider_on = True
        else:
            self.slider_on = False

    def on_slider_value(self,widget):
        self.slider_value_txt = str(int(widget.value))


    def on_text_validate(self,widget):
        self.text_input_from_user = widget.text







class StackLayoutExample(StackLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

        #problem : you can't
        for i in range(100):
            b = Button(text=str(i+1), size_hint=(None,None), size=(dp(100), dp(100))) #remember to add the size_hint or Z is going to take the whole place
            self.add_widget(b)


# class GridLayoutExample(GridLayout):
#     pass #instead of doing this, you can define in the kv file: GridLayoutExample@GridLayout


#AnchorLayout
class AnchorLayoutExample(AnchorLayout):
    pass

#BoxLayout
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
