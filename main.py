from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.clock import Clock
from jnius import autoclass


class BlackScreen(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # чёрный фон
        Window.clearcolor = (0, 0, 0, 1)


class TestApp(App):
    def build(self):
        # через 3 секунды показать toast и закрыть приложение
        Clock.schedule_once(lambda dt: self.exit_with_toast(), 3)
        return BlackScreen()

    def exit_with_toast(self):
        PythonActivity = autoclass('org.kivy.android.PythonActivity')
        Toast = autoclass('android.widget.Toast')
        TextView = autoclass('android.widget.TextView')
        String = autoclass('java.lang.String')

        activity = PythonActivity.mActivity

        def make_toast():
            tv = TextView(activity)
            # длинное сообщение
            long_text = String(
                "К сожалению, приложение остановлено.\n"
                "Это тестовое сообщение, оно длинное и переносится "
                "на несколько строк, чтобы показать кастомный Toast."
            )
            tv.setText(long_text)
            tv.setTextSize(18)   # размер шрифта
            tv.setPadding(40, 40, 40, 40)

            toast = Toast(activity)
            toast.setDuration(Toast.LENGTH_LONG)
            toast.setView(tv)
            toast.show()

            # закрыть приложение

        # обязательно запускать в UI-потоке
        activity.runOnUiThread(make_toast)


TestApp().run()
