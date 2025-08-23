from kivy.app import App
from kivy.uix.button import Button
from jnius import autoclass

class TestApp(App):
    def build(self):
        return Button(text="Показать современный диалог", on_press=self.show_error)

    def show_error(self, *args):
        PythonActivity = autoclass('org.kivy.android.PythonActivity')
        MaterialAlertDialogBuilder = autoclass('com.google.android.material.dialog.MaterialAlertDialogBuilder')
        JavaString = autoclass('java.lang.String')

        activity = PythonActivity.mActivity

        def make_dialog():
            dialog = MaterialAlertDialogBuilder(activity)
            dialog.setTitle(JavaString("Ошибка"))
            dialog.setMessage(JavaString("К сожалению, приложение остановлено."))
            dialog.setCancelable(False)
            dialog.setPositiveButton(JavaString("OK"), None)
            dialog.setNegativeButton(JavaString("Отправить отчёт"), None)
            dialog.show()

        activity.runOnUiThread(make_dialog)

TestApp().run()
