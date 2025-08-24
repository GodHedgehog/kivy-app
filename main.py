from jnius import autoclass

PythonActivity = autoclass('org.kivy.android.PythonActivity')
Toast = autoclass('android.widget.Toast')

activity = PythonActivity.mActivity
Toast.makeText(activity, "Привет из Python!", Toast.LENGTH_SHORT).show()
