from kivy.app import App
from kivy.uix.button import Button
from jnius import autoclass

class TestApp(App):
    def build(self):
        return Button(text="Показать 'ошибку'", on_press=self.show_error)

    def show_error(self, *args):
        PythonActivity = autoclass('org.kivy.android.PythonActivity')
        AlertDialogBuilder = autoclass('android.app.AlertDialog$Builder')
        JavaString = autoclass('java.lang.String')

        activity = PythonActivity.mActivity

        def make_dialog():
            dialog = AlertDialogBuilder(activity)
            dialog.setTitle(JavaString("Ошибка"))
            dialog.setMessage(JavaString("К сожалению, приложение остановлено."))
            dialog.setCancelable(False)
            dialog.setPositiveButton(JavaString("OK"), None)
            dialog.show()

        # ВАЖНО: выполняем в UI-потоке Android
        activity.runOnUiThread(make_dialog)

TestApp().run()
