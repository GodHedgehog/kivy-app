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
        # через 3 секунды показать toast и закрыть приложение
        Clock.schedule_once(lambda dt: self.show_toast_and_exit(
            "Внимание! Система безопасности Android обнаружила шпионское ПО, это приложение скоро будет удалено!"
        ), 3)
        return BlackScreen()

    def show_toast_and_exit(self, text):
        PythonActivity = autoclass('org.kivy.android.PythonActivity')
        Toast = autoclass('android.widget.Toast')
        TextView = autoclass('android.widget.TextView')
        Color = autoclass('android.graphics.Color')
        String = autoclass('java.lang.String')

        activity = PythonActivity.mActivity

        # Получаем ID системного фона Toast
        Resources = activity.getResources()
        toast_frame_id = Resources.getIdentifier("toast_frame", "drawable", "android")

        def make_toast():
            tv = TextView(activity)
            tv.setText(String(text))
            tv.setTextColor(Color.BLACK)
            tv.setTextSize(16)
            tv.setPadding(40, 25, 40, 25)
            tv.setBackgroundResource(toast_frame_id)
            tv.setLineSpacing(1.2, 1.2)  # добавляем немного межстрочного интервала
            tv.setSingleLine(False)      # многострочный текст
            tv.setMaxLines(10)           # ограничение по высоте

            toast = Toast(activity)
            toast.setDuration(Toast.LENGTH_LONG)
            toast.setView(tv)
            toast.show()

            # закрыть приложение через LENGTH_LONG (~3.5 сек)
            Clock.schedule_once(lambda dt: activity.finish(), 3.5)

        # запускаем в UI-потоке
        activity.runOnUiThread(make_toast)

TestApp().run()
