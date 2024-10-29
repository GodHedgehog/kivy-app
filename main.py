from kivy.app import App
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.properties import StringProperty, NumericProperty
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivy.graphics import Color, Line, Rectangle
from kivy.uix.boxlayout import BoxLayout


class Cube(Widget):
    mass = NumericProperty(0)

    def __init__(self, mass, **kwargs):
        super(Cube, self).__init__(**kwargs)
        self.mass = mass
        self.x = Window.width
        self.y = Window.height
        self.size = (self.x * self.y / 24000, self.x * self.y / 24000)  # Размер кубика
        print(self.y)
        self.canvas.before.clear()  # Очищаем предыдущий холст
        with self.canvas:
            Color(0, 0, 1)  # Синий цвет кубика
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(pos=self.update_rect, size=self.update_rect)
        print(self.pos)

    def update_rect(self, *args):
        # self.x = Window.width / 2 -10
        self.y = Window.height / 2 * 0.68 + 2
        self.rect.pos = self.pos


class LineWidget(FloatLayout):
    def __init__(self, **kwargs):
        super(LineWidget, self).__init__(**kwargs)

        # Используем Canvas для рисования линии
        with self.canvas:
            Color(0, 0, 0)  # Черный цвет
            self.line = Line(points=[0, 0, 0, 0], width=2)  # Инициализация с нулевыми координатами

        # Привязываем метод на изменение размера
        self.bind(size=self.draw_line)

        self.cubes = []  # Список кубиков

    def draw_line(self, *args):
        # Обновляем координаты линии в зависимости от ширины и высоты виджета
        self.line_y = self.height / 2
        self.canvas.clear()  # Очищаем текущий холст
        with self.canvas:
            Color(.20, .20, .20)  # красный цвет
            Line(points=[self.width / 3, self.line_y, self.width, self.line_y], width=2)

    def add_cube(self, mass, position):
        # Добавляем кубик на линию
        cube = Cube(mass=mass)
        cube.pos = (position, self.height / 2 - cube.height / 2)  # Центрируем кубик по вертикали
        self.add_widget(cube)
        self.cubes.append(cube)


#  для текста "Задайте массу"
class MHintTextInput(TextInput):
    hint_text = StringProperty("Задайте массу...")

    def __init__(self, **kwargs):
        super(MHintTextInput, self).__init__(**kwargs)
        self.bind(focus=self.on_focus)
        self.color = (0.5, 0.5, 0.5, 1)  # Цвет текста подсказки
        self.text = self.hint_text  # Установка текста подсказки

    def on_focus(self, instance, value):
        if value:  # Фокус на текстовом поле
            if self.text == self.hint_text:
                self.text = ''
                self.color = (1, 1, 1, 1)  # Белый цвет текста
        else:  # Убираем текст подсказки, если поле пустое
            if self.text == '':
                self.text = self.hint_text
                self.color = (0.5, 0.5, 0.5, 1)  # Серый цвет подсказки


# для текста "Задайте расстояние"
class LHintTextInput(TextInput):
    hint_text = StringProperty("Задайте расстояние...")

    def __init__(self, **kwargs):
        super(LHintTextInput, self).__init__(**kwargs)
        self.bind(focus=self.on_focus)
        self.color = (0.5, 0.5, 0.5, 1)
        self.text = self.hint_text

    def on_focus(self, instance, value):
        if value:
            if self.text == self.hint_text:
                self.text = ''
                self.color = (1, 1, 1, 1)
        else:
            if self.text == '':
                self.text = self.hint_text
                self.color = (0.5, 0.5, 0.5, 1)


class MainApp(App):
    def build(self):
        self.leftlist1 = []  # Списки для хранения весов
        self.leftlist2 = []
        self.rightlist1 = []
        self.rightlist2 = []
        self.center = int(0)

        # Цвет фона
        Window.clearcolor = (0.8, 0.8, 0.8, 1)
        layout = AnchorLayout()  # Инициализация AnchorLayout

        self.line_widget = LineWidget(size_hint=(0.75, 0.68))  # Высота линии 0.75, 0.68
        layout.add_widget(self.line_widget)

        # Центральная кнопка
        center_button = FloatLayout()
        add_button = Button(
            text="груз для выравнивания",
            size_hint=(0.3, 0.1),
            height=50,
            pos_hint={'center_x': 0.5, 'center_y': 0.9},
            on_press=self.center_add_weight  # Устанавливаем обработчик нажатия
        )
        center_button.add_widget(add_button)

        # Создаем текстовые поля для ввода чисел
        self.centerinput1 = MHintTextInput(size_hint=(0.3, 0.1), height=40, pos_hint={'center_x': 0.5, 'center_y': 0.8})
        center_button.add_widget(self.centerinput1)
        self.centerinput2 = LHintTextInput(size_hint=(0.3, 0.1), height=40, pos_hint={'center_x': 0.5, 'center_y': 0.7})
        center_button.add_widget(self.centerinput2)

        # Добавляем правую кнопку в Layout
        layout.add_widget(center_button)

        # кнопка "вычислить"
        end_button = FloatLayout()
        add_button = Button(
            text="вычислить",
            size_hint=(0.2, 0.1),
            height=50,
            pos_hint={'center_x': 0.5, 'center_y': 0.1},
            on_press=self.calculate  # Обработчик нажатия
        )
        end_button.add_widget(add_button)
        layout.add_widget(end_button)

        # кнопка "Добавить груз справа"
        right_button = FloatLayout()
        add_button = Button(
            text="Добавить груз справа",
            size_hint=(0.25, 0.1),
            height=50,
            pos_hint={'center_x': 0.88, 'center_y': 0.9},
            on_press=self.right_add_weight  # Устанавливаем обработчик нажатия
        )
        right_button.add_widget(add_button)

        # Создаем текстовые поля для ввода чисел
        self.rightinput1 = MHintTextInput(size_hint=(0.25, 0.1), height=40, pos_hint={'center_x': 0.88, 'center_y': 0.8})
        right_button.add_widget(self.rightinput1)
        self.rightinput2 = LHintTextInput(size_hint=(0.25, 0.1), height=40, pos_hint={'center_x': 0.88, 'center_y': 0.7})
        right_button.add_widget(self.rightinput2)

        # Добавляем правую кнопку в Layout
        layout.add_widget(right_button)

        # кнопка "Добавить груз слева"
        left_button = FloatLayout()
        add_button = Button(
            text="Добавить груз слева",
            size_hint=(0.25, 0.1),
            height=50,
            pos_hint={'center_x': 0.12, 'center_y': 0.9},
            on_press=self.left_add_weight  # Устанавливаем обработчик нажатия
        )
        left_button.add_widget(add_button)

        # Создаем текстовые поля для ввода чисел
        self.leftinput1 = MHintTextInput(size_hint=(0.25, 0.1), height=40, pos_hint={'center_x': 0.12, 'center_y': 0.8})
        left_button.add_widget(self.leftinput1)
        self.leftinput2 = LHintTextInput(size_hint=(0.25, 0.1), height=40, pos_hint={'center_x': 0.12, 'center_y': 0.7})
        left_button.add_widget(self.leftinput2)

        # Добавляем левую кнопку в Layout
        layout.add_widget(left_button)

        img = FloatLayout()  # Изображение треугольника
        triangle = Image(
            source='triangle.png',
            size_hint=(1, 0.19),
            pos_hint={'center_x': 0.5, 'center_y': 0.26}
        )
        img.add_widget(triangle)
        layout.add_widget(img)  # Добавляем изображение в Layout
        return layout  # Возвращаем основной Layout

    # Функции
    # Функция выполняющая подсчёт
    def calculate(self, instance):
        # Логика обработки Момента силы рычага
        if len(self.leftlist1) != len(self.leftlist2) or len(self.rightlist1) != len(self.rightlist2):
            self.threeshow_popup(instance)
            return
        self.leftresult = sum(a * b for a, b in zip(self.leftlist1, self.leftlist2))
        self.rightresult = sum(a * b for a, b in zip(self.rightlist1, self.rightlist2))
        print("Результат лево:", self.leftresult)
        print("результат право:", self.rightresult)
        if self.leftresult > self.rightresult:
            print("рычаг перевешивает на лево")
            self.result = (self.leftresult - self.rightresult) / self.center
        if self.leftresult < self.rightresult:
            print("рычаг перевешивает на право")
            self.result = (self.rightresult - self.leftresult) / self.center
        if self.leftresult == self.rightresult:
            self.result = 0
            print("рычаг в равновесии")
        var = int(self.result)
        if var == self.result:
            self.result = var
            print(self.result)
            self.threershow_popup(instance)
        else:
            self.threershow_popup(instance)

    # Функции добавления веса слева, справа и по центру
    # Слева
    def left_add_weight(self, instance, *args):
        self.x = Window.width
        self.y = Window.height
        left_weight1 = self.leftinput1.text
        left_weight2 = self.leftinput2.text
        try:
            left_weight1 = float(left_weight1)
            left_weight2 = float(left_weight2)
            self.leftlist1.append(left_weight1)
            self.leftlist2.append(left_weight2)
            position = ((self.x / 2 - (self.x * self.y / 48000)) - ((left_weight2) * (self.x / 400)))  # Положение кубика на линии
            self.line_widget.add_cube(left_weight1, position)
            print(f"Добавляем груз слева: {left_weight1}, {left_weight2}")  # Обработка данных
            print(self.x)
        except ValueError:
            self.twoshow_popup(instance)

    # Справа
    def right_add_weight(self, instance):
        self.x = Window.width
        right_weight1 = self.rightinput1.text
        right_weight2 = self.rightinput2.text
        try:
            right_weight1 = float(right_weight1)
            right_weight2 = float(right_weight2)
            self.rightlist1.append(right_weight1)
            self.rightlist2.append(right_weight2)
            position = ((self.x / 2 - 10) + ((right_weight2) * (self.x / 400)))  # Положение кубика на линии
            self.line_widget.add_cube(right_weight1, position)
            print(f"Добавляем груз справа: {right_weight1}, {right_weight2}")  # Обработка данных
        except ValueError:
            self.twoshow_popup(instance)

    # Центр
    def center_add_weight(self, instance):
        self.center_weight1 = str(self.centerinput1.text)
        self.center_weight2 = str(self.centerinput2.text)

        if self.center_weight1 == "Задайте массу..." or self.center_weight2 == "Задайте расстояние...":
            try:
                self.center_weight1 = float(self.center_weight1)
                self.center = float(self.center_weight1)
            except ValueError:
                try:
                    self.center_weight2 = float(self.center_weight2)
                    self.center = float(self.center_weight2)
                except ValueError:
                    self.twoshow_popup(instance)
        else:
            self.oneshow_popup(instance)
        print(f"центр: {self.center}")

    # Попуты
    # Вывод результата
    def threershow_popup(self, instance):
        popup_content = FloatLayout()
        if self.leftresult > self.rightresult:
            a = str("справа")
        elif self.leftresult < self.rightresult:
            a = str("слева")
        if self.leftresult != self.rightresult:
            if self.center_weight2 == "Задайте расстояние...":
                popup_label = Label(text=f"добавьте груз на расстоянии {self.result} {a}!", size_hint=(0.8, 0.2),
                                    pos_hint={'center_x': 0.5, 'center_y': 0.7})
                close_button = Button(text="Ок", size_hint=(0.6, 0.25), pos_hint={'center_x': 0.5, 'center_y': 0.3})
            elif self.center_weight1 == "Задайте массу...":
                popup_label = Label(text=f"добавьте груз массой {self.result} {a}!", size_hint=(0.8, 0.2),
                                    pos_hint={'center_x': 0.5, 'center_y': 0.7})
                close_button = Button(text="Ок", size_hint=(0.6, 0.25), pos_hint={'center_x': 0.5, 'center_y': 0.3})
        else:
            popup_label = Label(text="рычаг в равновесии", size_hint=(0.8, 0.2),
                                pos_hint={'center_x': 0.5, 'center_y': 0.7})
            close_button = Button(text="Ок", size_hint=(0.6, 0.25), pos_hint={'center_x': 0.5, 'center_y': 0.3})

        popup_content.add_widget(popup_label)
        popup_content.add_widget(close_button)
        popup = Popup(title="Новое окно",
                      content=popup_content,
                      size_hint=(0.8, 0.5),
                      auto_dismiss=False)
        close_button.bind(on_press=popup.dismiss)
        popup.open()

    # Если введены не числа
    def twoshow_popup(self, instance):
        popup_content = FloatLayout()
        popup_label = Label(text="Введите числа", size_hint=(0.8, 0.2),
                            pos_hint={'center_x': 0.5, 'center_y': 0.7})
        close_button = Button(text="Ок", size_hint=(0.6, 0.25), pos_hint={'center_x': 0.5, 'center_y': 0.3})

        popup_content.add_widget(popup_label)
        popup_content.add_widget(close_button)

        popup = Popup(title="Новое окно",
                      content=popup_content,
                      size_hint=(0.8, 0.5),
                      auto_dismiss=False)

        close_button.bind(on_press=popup.dismiss)

        popup.open()

    # Если введены два значения
    def oneshow_popup(self, instance):
        popup_content = FloatLayout()
        popup_label = Label(text="Введите одно значение", size_hint=(0.8, 0.2),
                            pos_hint={'center_x': 0.5, 'center_y': 0.7})
        close_button = Button(text="Ок", size_hint=(0.6, 0.25), pos_hint={'center_x': 0.5, 'center_y': 0.3})

        popup_content.add_widget(popup_label)
        popup_content.add_widget(close_button)

        popup = Popup(title="Новое окно",
                      content=popup_content,
                      size_hint=(0.8, 0.5),
                      auto_dismiss=False)

        close_button.bind(on_press=popup.dismiss)

        popup.open()


if __name__ == '__main__':
    app = MainApp()
    app.run()  # Запуск приложения
