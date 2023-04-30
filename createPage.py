from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class CreateAccountPage(BoxLayout):
    def __init__(self, create_account_callback, go_back_callback, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        self.create_account_callback = create_account_callback
        self.go_back_callback = go_back_callback

        self.add_widget(Label(text='Create Account'))

        self.email_input = TextInput(hint_text='Email', multiline=False)
        self.add_widget(self.email_input)

        self.name_input = TextInput(hint_text='Name', multiline=False)
        self.add_widget(self.name_input)

        self.age_input = TextInput(hint_text='Age', multiline=False)
        self.add_widget(self.age_input)

        self.neighbourhood_input = TextInput(hint_text='Neighbourhood', multiline=False)
        self.add_widget(self.neighbourhood_input)

        self.password_input = TextInput(hint_text='Password', multiline=False, password=True)
        self.add_widget(self.password_input)

        create_account_button = Button(text='Create Account')
        create_account_button.bind(on_release=self.create_account)
        self.add_widget(create_account_button)

        go_back_button = Button(text='Go Back')
        go_back_button.bind(on_release=self.go_back)
        self.add_widget(go_back_button)

    def create_account(self, instance):
        email = self.email_input.text
        name = self.name_input.text
        age = self.age_input.text
        neighbourhood = self.neighbourhood_input.text
        password = self.password_input.text

        self.create_account_callback(email, name, age, neighbourhood, password)

    def go_back(self, instance):
        self.go_back_callback()
