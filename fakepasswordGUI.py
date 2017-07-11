from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class LoginScreen(GridLayout): # use a grid layout

    # overload the __init__ method so we can add widgets
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)

        # 2 columns, with each widget created left to right in each row:
        self.cols = 2

        # 4 widgets:
        self.add_widget(Label(text='User Name'))

        self.username = TextInput(multiline=False)
        self.add_widget(self.username)

        self.add_widget(Label(text='password'))

        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)


class MyApp(App):

    def build(self):
        return LoginScreen()


if __name__ == '__main__':
    MyApp().run()
