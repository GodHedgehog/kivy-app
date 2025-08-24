from kivy.app import App
from kivy.uix.button import Button
from jnius import autoclass

class TestApp(App):
    def build(self):
        return Button(text="Показать Toast", on_press=self.show_toast)

    def show_toast(self, *args):
        PythonActivity = autoclass('org.kivy.android.PythonActivity')
        Toast = autoclass('android.widget.Toast')
        String = autoclass('java.lang.String')

        activity = PythonActivity.mActivity

        def toast_message():
            message = String("Привет из Python!")
            Toast.makeText(activity, message, Toast.LENGTH_SHORT).show()

        # Важно: запускать в UI-потоке
        activity.runOnUiThread(toast_message)

TestApp().run()
