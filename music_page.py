from PyQt5.QtWidgets import QWidget, QVBoxLayout, QFormLayout, QComboBox, QTextEdit, QPushButton, QLabel
from PyQt5.QtCore import Qt

class MusicPage(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Форма для ввода предпочтений
        form_layout = QFormLayout()

        # Вопрос 1: Любимый жанр
        self.genre_combo = QComboBox()
        self.genre_combo.addItems(["Поп", "Рок", "Хип-хоп", "Классика", "Электроника"])
        form_layout.addRow("Любимый жанр:", self.genre_combo)

        # Вопрос 2: Настроение
        self.mood_combo = QComboBox()
        self.mood_combo.addItems(["Энергичное", "Спокойное", "Меланхоличное", "Весёлое"])
        form_layout.addRow("Какое настроение вы ищете?", self.mood_combo)

        # Вопрос 3: Предпочитаемая эпоха
        self.era_combo = QComboBox()
        self.era_combo.addItems(["Современная", "80-е", "90-е", "2000-е"])
        form_layout.addRow("Музыка какой эпохи вам ближе?", self.era_combo)

        layout.addLayout(form_layout)

        # Кнопка анализа
        analyze_button = QPushButton("Проанализировать")
        analyze_button.clicked.connect(self.analyze_preferences)
        layout.addWidget(analyze_button)

        # Поле для результата
        self.result_display = QTextEdit()
        self.result_display.setReadOnly(True)
        self.result_display.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.result_display)

        # Кнопка возврата
        back_button = QPushButton("На главную")
        back_button.clicked.connect(lambda: self.parent.show_page(0))
        layout.addWidget(back_button)

        self.setLayout(layout)

    def analyze_preferences(self):
        genre = self.genre_combo.currentText()
        mood = self.mood_combo.currentText()
        era = self.era_combo.currentText()

        # Простая логика подбора песен (для примера)
        recommendations = {
            "Поп": ["Dua Lipa - Levitating", "The Weeknd - Blinding Lights"],
            "Рок": ["Imagine Dragons - Believer", "Foo Fighters - Everlong"],
            "Хип-хоп": ["Drake - God's Plan", "Kendrick Lamar - HUMBLE."],
            "Классика": ["Beethoven - Symphony No.9", "Vivaldi - The Four Seasons"],
            "Электроника": ["Calvin Harris - Feel So Close", "Daft Punk - Get Lucky"]
        }

        # Учитываем настроение и эпоху
        songs = recommendations.get(genre, ["Неизвестный жанр"])
        result = f"# Рекомендации для вас\n\n**Жанр**: {genre}\n**Настроение**: {mood}\n**Эпоха**: {era}\n\n## Песни:\n"
        for song in songs:
            result += f"- {song}\n"

        self.result_display.setMarkdown(result)