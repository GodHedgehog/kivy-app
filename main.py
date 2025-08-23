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

        # Активность
        activity = PythonActivity.mActivity

        # Создаём AlertDialog
        dialog = AlertDialogBuilder(activity)
        dialog.setTitle("Ошибка")
        dialog.setMessage("К сожалению, приложение остановлено.")
        dialog.setCancelable(False)

        # Добавляем кнопку OK (иначе краш)
        def on_click(dialog_interface, which):
            dialog_interface.dismiss()
        dialog.setPositiveButton("OK", on_click)

        # Показываем
        dialog.show()

TestApp().run()
