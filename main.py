import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.clock import Clock


class BlackScreen(Widget):
    pass


class RandomCloseApp(App):
    def build(self):
        # чёрный фон окна
        Window.clearcolor = (0, 0, 0, 1)

        # выбираем случайное время от 5 до 10 секунд
        close_time = random.randint(5, 10)
        Clock.schedule_once(self.close_app, close_time)

        return BlackScreen()

    def close_app(self, dt):
        App.get_running_app().stop()


if __name__ == "__main__":
    RandomCloseApp().run()
