import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput


class YadhardhaApp(App):
    def build(self):
        self.icon = "1011863.png"
        self.ops = ["/", "**", "%", "*", "-", "+", "//","^","<",">"]
        self.last = None
        self.last_button = None

        main_layout = BoxLayout(orientation="vertical")
        self.solution = TextInput(background_color="white", foreground_color="black",multiline=False,halign="right",font_size=45)
        main_layout.add_widget(self.solution)

        buttons = [
            ["7", "8", "9", "/","//","&"],
            ["4", "5", "6", "*","**","|"],
            ["1", "2", "3", "-","%",">"],
            ["0", ".", "C", "+","^","<"],


        ]

        for r in buttons:
            h_layout = BoxLayout()
            for label in r:
                button = Button(
                    text=label, font_size=30, background_color="black",
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                )
                button.bind(on_press=self.on_button)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)

        equal_button = Button(
            text="=", font_size=30, background_color="grey",
            pos_hint={"center_x": 0.5, "center_y": 0.5},
        )
        equal_button.bind(on_press=self.on_solution)
        main_layout.add_widget(equal_button)

        return main_layout

    def on_button(self, instance):
        current = self.solution.text
        button_text = instance.text

        if button_text == 'C':
            self.solution.text = ""
        else:
            if current and (
                    self.last and button_text in self.ops):
                return
            elif current == "" and button_text in self.ops:
                return
            else:
                new_text = current + button_text
                self.solution.text = new_text
            self.last_button = button_text
            self.last = self.last_button in self.ops

    def on_solution(self, instance):
        text = self.solution.text
        if text:
            solution = str(eval(self.solution.text))
            self.solution.text = solution


if __name__ == '__main__':
    YadhardhaApp().run()
