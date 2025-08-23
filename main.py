from kivy.app import App
from kivy.uix.button import Button
from jnius import autoclass

class TestApp(App):
    def build(self):
        return Button(text="Показать ошибку", on_press=self.show_error)

    def show_error(self, *args):
        PythonActivity = autoclass('org.kivy.android.PythonActivity')
        AlertDialog = autoclass('android.app.AlertDialog$Builder')
        
        activity = PythonActivity.mActivity
        dialog = AlertDialog(activity)
        dialog.setTitle("Ошибка")
        dialog.setMessage("К сожалению, приложение остановлено.")
        dialog.setPositiveButton("OK", None)
        dialog.show()

TestApp().run()
