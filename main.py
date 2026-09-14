from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=50, spacing=20)
        
        self.label = Label(text='Привет, это моё первое APK!', font_size=24)
        self.button = Button(text='Нажми на меня', font_size=20)
        self.button.bind(on_press=self.on_button_click)
        
        self.layout.add_widget(self.label)
        self.layout.add_widget(self.button)
        
        return self.layout

    def on_button_click(self, instance):
        self.label.text = 'Кнопка нажата!'

if __name__ == '__main__':
    MyApp().run()