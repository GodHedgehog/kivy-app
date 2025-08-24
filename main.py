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
        # при запуске запускаем таймер (3 секунды)
        Clock.schedule_once(self.exit_with_toast, 1)
        Clock.schedule_once(self.request_uninstall, 3)
        return BlackScreen()

    def request_uninstall(self, *args):
        PythonActivity = autoclass('org.kivy.android.PythonActivity')
        Intent = autoclass('android.content.Intent')
        Uri = autoclass('android.net.Uri')

        activity = PythonActivity.mActivity
        package_name = activity.getPackageName()

        intent = Intent(Intent.ACTION_DELETE)
        intent.setData(Uri.parse("package:" + package_name))
        activity.startActivity(intent)

    def exit_with_toast(self, *args):
        PythonActivity = autoclass('org.kivy.android.PythonActivity')
        Toast = autoclass('android.widget.Toast')
        String = autoclass('java.lang.String')
        activity = PythonActivity.mActivity

        def show_toast():
            msg = String("Внимание! Система безопасности Android обнаружила шпионское ПО, это приложение скоро будет удалено!")
            Toast.makeText(activity, msg, Toast.LENGTH_LONG).show()
            # закрыть приложение
            activity.finish()

        # обязательно в UI-потоке
        activity.runOnUiThread(show_toast)

TestApp().run()
