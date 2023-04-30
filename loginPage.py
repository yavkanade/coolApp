# login_page.py
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class LoginPage(BoxLayout):
    def __init__(self, switch_to_create_account, login_callback, **kwargs):
        super(LoginPage, self).__init__(**kwargs)
        self.orientation = "vertical"

        self.switch_to_create_account = switch_to_create_account
        self.login_callback = login_callback

        self.add_widget(Label(text="Login"))

        self.email_input = TextInput(hint_text="Email", multiline=False)
        self.add_widget(self.email_input)

        self.password_input = TextInput(hint_text="Password", multiline=False, password=True)
        self.add_widget(self.password_input)

        login_button = Button(text="Login")
        login_button.bind(on_press=self.login)
        self.add_widget(login_button)

        create_account_button = Button(text="Create Account")
        create_account_button.bind(on_press=self.switch_to_create_account)
        self.add_widget(create_account_button)

    def login(self, instance):
        email = self.email_input.text
        password = self.password_input.text

        self.login_callback(email, password)
