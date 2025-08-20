import time

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.clock import Clock
import random
from kivy.uix.button import Button

#Window.size = (1080, 2400)
Window.borderless = False
class BlackScreen(FloatLayout):  # наследуемся от FloatLayout
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.label = Label(
            text="Приложение Макс",
            font_size=Window.width * 0.075,
            color=(1, 1, 1, 1),
            pos_hint={"center_x": 0.5, "center_y": 0.95},  # теперь работает
        )
        self.add_widget(self.label)

        self.label2 = Label(
            text="",
            font_size=Window.width * 0.04,
            halign="left",
            valign="top",
            color=(1, 1, 1, 1),
            size_hint=(0.9, 0.9),
            pos_hint={"x": 0.05, "y": 0.001}  # теперь работает
        )
        self.label2.bind(size=lambda inst, val: setattr(inst, "text_size", val))
        self.add_widget(self.label2)

        self.label3 = Label(
            text="",
            font_size=Window.width * 0.04,
            halign="left",
            valign="top",
            color=(1, 1, 1, 1),
            size_hint=(0.8, 0.8),
            pos_hint={"x": 0.05, "y": 0.001}  # теперь работает
        )
        self.label3.bind(size=lambda inst, val: setattr(inst, "text_size", val))
        self.add_widget(self.label3)

        self.label4 = Label(
            text="",
            font_size=Window.width * 0.04,
            halign="left",
            valign="top",
            color=(1, 1, 1, 0.5),
            size_hint=(0.6, 0.6),
            pos_hint={"x": 0.05, "y": 0.001}  # теперь работает
        )
        self.label4.bind(size=lambda inst, val: setattr(inst, "text_size", val))
        self.add_widget(self.label4)

        self.label5 = Label(
            text="",
            font_size=Window.width * 0.04,
            halign="left",
            valign="top",
            color=(1, 1, 1, 1),
            size_hint=(0.7, 0.7),
            pos_hint={"x": 0.05, "y": 0.001}  # теперь работает
        )
        self.label5.bind(size=lambda inst, val: setattr(inst, "text_size", val))
        self.add_widget(self.label5)

        self.button = Button(
            text="Гойда",
            font_size=24,
            size_hint=(0.5, 0.15),
            pos_hint={"center_x": 0.5, "y": 0.1},
            on_release=self.on_button_release,
            on_press=self.on_button_press

        )

        # через 5 секунд добавляем кнопку на экран
        Clock.schedule_once(self.show_button, 15)

    def update_text(self, new_text):
        self.label2.text = new_text

    def update_text2(self, new_text):
        self.label3.text = new_text

    def update_text3(self, new_text):
        self.label4.text = new_text

    def update_text5(self, new_text):
        self.label5.text = new_text

    def show_button(self, dt):
        self.add_widget(self.button)

    def on_button_release(self, instance):
        print("Гойда")

    def on_button_press(self, instance):
        self.button.text = "Подписать контракт на сво"

class RandomCloseApp(App):
    def build(self):
        Window.clearcolor = (0, 0, 0, 1)

        self.screen = BlackScreen()

        Clock.schedule_once(lambda dt: self.screen.update_text("Идёт установка фсб на ваше устройство"), 2)
        Clock.schedule_once(lambda dt: self.screen.update_text("Идёт установка фсб на ваше устройство."), 2.5)
        Clock.schedule_once(lambda dt: self.screen.update_text("Идёт установка фсб на ваше устройство.."), 3)
        Clock.schedule_once(lambda dt: self.screen.update_text("Идёт установка фсб на ваше устройство..."), 3.5)
        Clock.schedule_once(lambda dt: self.screen.update_text("Идёт установка фсб на ваше устройство"), 4)
        Clock.schedule_once(lambda dt: self.screen.update_text("Идёт установка фсб на ваше устройство."), 4.5)
        Clock.schedule_once(lambda dt: self.screen.update_text("Идёт установка фсб на ваше устройство.."), 5)
        Clock.schedule_once(lambda dt: self.screen.update_text("Идёт установка фсб на ваше устройство..."), 5.5)
        Clock.schedule_once(lambda dt: self.screen.update_text("Идёт установка фсб на ваше устройство"), 6)
        Clock.schedule_once(lambda dt: self.screen.update_text("Фсб успешно загружено на ваше устройство"), 7)
        Clock.schedule_once(lambda dt: self.screen.update_text3("pornhub.com"), 9)
        Clock.schedule_once(lambda dt: self.screen.update_text3("myrotvorets.center"), 11)
        Clock.schedule_once(lambda dt: self.screen.update_text3(""), 15)
        Clock.schedule_once(lambda dt: self.screen.update_text5("найдено запрещённых сайтов: 0"), 7)
        Clock.schedule_once(lambda dt: self.screen.update_text5("найдено запрещённых сайтов: 1"), 9)
        Clock.schedule_once(lambda dt: self.screen.update_text5("найдено запрещённых сайтов: 2"), 11)
        Clock.schedule_once(lambda dt: self.screen.update_text5("Были обнаружены экстремисткие сайты\nнажмите на кнопку 'Гойда'\nдля прохождения верификации"), 15)
        Clock.schedule_once(lambda dt: self.screen.update_text2(""), 15)





        self.progress = 0
        Clock.schedule_once(self.start_progress, 7)

        Clock.schedule_once(lambda dt: self.screen.update_text2("История загружена"), 7)

        close_time = random.randint(30, 100)
        Clock.schedule_once(self.close_app, close_time)
        return self.screen

    def start_progress(self, dt):
        # обновлять каждые 0.1 сек
        Clock.schedule_interval(self.update_progress, 0.1)

    def update_progress(self, dt):
        if self.progress <= 100:
            self.screen.update_text2(f"Получение истории браузера {self.progress}%")
            if self.progress <= 97:
                self.progress += random.randint(0, 4)
            else:
                self.progress += 1
        else:
            self.screen.update_text2("История браузера успешно получена!")
            return False  # остановить таймер

        close_time = random.randint(40, 41)
        Clock.schedule_once(self.close_app, close_time)

        return self.screen

    def close_app(self, dt):
        App.get_running_app().stop()


if __name__ == "__main__":
    RandomCloseApp().run()
