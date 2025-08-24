from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.clock import Clock
from jnius import autoclass

class BlackScreen(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.clearcolor = (0, 0, 0, 1)  # чёрный фон

class TestApp(App):
    def build(self):
        # через 3 секунды показать длинный toast и закрыть приложение
        Clock.schedule_once(lambda dt: self.show_long_toast(
            "К сожалению, приложение остановлено.\n"
            "Это тестовое сообщение оформлено как настоящий Toast.\n"
            "Оно будет висеть примерно 10 секунд.", duration=6), 3)
        return BlackScreen()

    def show_long_toast(self, text, duration=10):
        PythonActivity = autoclass('org.kivy.android.PythonActivity')
        Toast = autoclass('android.widget.Toast')
        TextView = autoclass('android.widget.TextView')
        Color = autoclass('android.graphics.Color')
        String = autoclass('java.lang.String')
        android = autoclass('android')

        activity = PythonActivity.mActivity

        def make_toast(*_):
            tv = TextView(activity)
            tv.setText(String(text))
            tv.setTextColor(Color.WHITE)
            tv.setTextSize(16)
            tv.setPadding(40, 25, 40, 25)
            tv.setBackgroundResource(android.R.drawable.toast_frame)

            toast = Toast(activity)
            toast.setDuration(Toast.LENGTH_LONG)
            toast.setView(tv)
            toast.show()

        # LENGTH_LONG ≈ 3.5 сек, повторяем несколько раз, чтобы удлинить
        repeats = duration // 3
        for i in range(repeats):
            Clock.schedule_once(make_toast, i * 3)

        # закрыть приложение через duration секунд
        Clock.schedule_once(lambda dt: activity.finish(), duration)

TestApp().run()
