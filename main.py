from kivy.app import App
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout


Window.clearcolor = (.40, .32, .63, 1)


class CalculatorApp(App):

    def text_label(self):
        self.ti.text = self.formula

    def add_number(self, instance):
        if (self.formula == '0'):
            self.formula = ''
        self.formula += str(instance.text)
        self.text_label()

    def add_operation(self, instance):
        if (str(instance.text).lower() == '×'):
            self.formula += '*'
        elif (str(instance.text).lower() == '÷'):
            self.formula += '/'
        self.text_label()

    def result(self, instance):
        if (self.formula[-2:] == '/0') or (self.formula[-1:] == '/') or (self.formula[-1:] == '+') or (
                self.formula[-1:] == '-') or (self.formula[-1:] == '.') or (self.formula[-1:] == '*'):
            self.formula = ''
            self.ti.text = 'Eror'
        else:
            self.ti.text = str(eval(self.ti.text))
            self.formula = self.ti.text

    def clear(self, instance):
        self.ti.text = '0'
        self.formula = '0'

    def del_button(self, instance):
        self.formula = self.formula[0:-1]
        self.text_label()

    def build(self):
        self.formula = '0'
        bl = BoxLayout(orientation='vertical')
        bl_1 = BoxLayout(size_hint=(1, .15))
        gl = GridLayout(cols=4, rows=4, size_hint=(1, .70))
        self.ti = TextInput(text='0', size_hint=(1, .15), font_size=35, halign='right',
                            background_color=[.40, .32, .63, 1], background_normal='', foreground_color=(1, 1, 1, 1),
                            multiline=False)
        bl.add_widget(self.ti)

        bl_1.add_widget(Button(text='CLEAR', font_size=10, background_color=[.72, .46, .72, 1], background_normal='',
                               on_press=self.clear))
        bl_1.add_widget(Button(text='DEL', font_size=10, background_color=[.72, .46, .72, 1], background_normal='',
                               on_press=self.del_button))

        gl.add_widget(
            Button(text='7', background_color=[.72, .46, .72, 1], background_normal='', on_press=self.add_number))
        gl.add_widget(
            Button(text='8', background_color=[.72, .46, .72, 1], background_normal='', on_press=self.add_number))
        gl.add_widget(
            Button(text='9', background_color=[.72, .46, .72, 1], background_normal='', on_press=self.add_number))
        gl.add_widget(
            Button(text='÷', background_color=[.72, .46, .72, 1], background_normal='', on_press=self.add_operation))

        gl.add_widget(
            Button(text='4', background_color=[.72, .46, .72, 1], background_normal='', on_press=self.add_number))
        gl.add_widget(
            Button(text='5', background_color=[.72, .46, .72, 1], background_normal='', on_press=self.add_number))
        gl.add_widget(
            Button(text='6', background_color=[.72, .46, .72, 1], background_normal='', on_press=self.add_number))
        gl.add_widget(
            Button(text='×', background_color=[.72, .46, .72, 1], background_normal='', on_press=self.add_operation))

        gl.add_widget(
            Button(text='1', background_color=[.72, .46, .72, 1], background_normal='', on_press=self.add_number))
        gl.add_widget(
            Button(text='2', background_color=[.72, .46, .72, 1], background_normal='', on_press=self.add_number))
        gl.add_widget(
            Button(text='3', background_color=[.72, .46, .72, 1], background_normal='', on_press=self.add_number))
        gl.add_widget(
            Button(text='-', background_color=[.72, .46, .72, 1], background_normal='', on_press=self.add_number))

        gl.add_widget(
            Button(text='0', background_color=[.72, .46, .72, 1], background_normal='', on_press=self.add_number))
        gl.add_widget(Button(text='.', font_size=25, background_color=[.72, .46, .72, 1],
                             background_normal='', on_press=self.add_number))
        gl.add_widget(Button(text='=', background_color=[.72, .46, .72, 1], background_normal='', on_press=self.result))
        gl.add_widget(
            Button(text='+', background_color=[.72, .46, .72, 1], background_normal='', on_press=self.add_number))

        bl.add_widget(bl_1)
        bl.add_widget(gl)
        return bl


if __name__ == '__main__':
    CalculatorApp().run()
