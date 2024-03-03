from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class Calculator_App(App):
    def build(self):
        #Assign nums and operators
        self.operators=["+","-","/","x"]
        self.nums=["0","1","2","3","4","5","6","7","8","9"]
        #Assign variables
        self.current_operater=None
        self.current_button=None
        #Build the UI first
        #Build the rectangular box that will encompass the entire screen
        screen_box_layout=BoxLayout(
           orientation='vertical'
        )
        #Build the text input that will store the values entered
        self.enter_numbers=TextInput(
            multiline=False,
            readonly=True,
            halign='right',
            font_size=28,
            font_name='Arial'
        )
        screen_box_layout.add_widget(self.enter_numbers)

        #Build the box layout consisting of the buttons
        arr = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            [".", "0", "C", "+"],
            ["Backspace"]
        ]
        for row in arr:
            val_layout = BoxLayout()
            for val in row:
                button = Button(
                    text=val,
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                    font_size=13
                )
                val_layout.add_widget(button)
                #Bind the button
                button.bind(on_press=self.button_clicked)
            screen_box_layout.add_widget(val_layout)

        #Create the equals button
        equals_box_layout=BoxLayout(
            orientation='horizontal'
        )
        equals_button=Button(
            text='=',
            pos_hint={'center_x':.5, 'center_y':.5}
        )
        #Bind the button
        equals_button.bind(on_press=self.equals_button_clicked)
        equals_box_layout.add_widget(equals_button)
        screen_box_layout.add_widget(equals_box_layout)
        #Return box layout
        return screen_box_layout        
    def button_clicked(self, instance):
        #Assign values to variables
        button_text=instance.text
        val=self.enter_numbers.text
        #Check if the command is "Clear"
        if button_text=="C":
            self.enter_numbers.text=""
        elif button_text=="Backspace":
            self.enter_numbers.text=val[:-1]
        else:
            if val and (self.current_button and self.current_operater in self.operators):
                return
            elif val=="" and button_text in self.operators:
                return
            else:
                new_text=val+button_text
                self.enter_numbers.text=new_text
        self.current_button=button_text
        self.current_operater=self.current_button in self.operators
    def equals_button_clicked(self, instance):
        val=self.enter_numbers.text
        if val:
            equals_text=str(eval(val))
            self.enter_numbers.text=equals_text


if __name__=='__main__':
    app=Calculator_App()
    app.run()