from kivy.app import App
from kivy.uix.button import Button
from jnius import autoclass, cast

class TestApp(App):
    def build(self):
        return Button(text="Показать 'ошибку'", on_press=self.show_error)

    def show_error(self, *args):
        # Android классы
        PythonActivity = autoclass('org.kivy.android.PythonActivity')
        AlertDialogBuilder = autoclass('android.app.AlertDialog$Builder')
        DialogInterface = autoclass('android.content.DialogInterface')
        JavaString = autoclass('java.lang.String')

        activity = PythonActivity.mActivity
        dialog = AlertDialogBuilder(activity)

        # ВАЖНО: оборачиваем строки в java.lang.String
        dialog.setTitle(JavaString("Ошибка"))
        dialog.setMessage(JavaString("К сожалению, приложение остановлено."))
        dialog.setCancelable(False)

        def on_click(dialog_interface, which):
            dialog_interface.dismiss()

        dialog.setPositiveButton(JavaString("OK"), on_click)
        dialog.show()

TestApp().run()
