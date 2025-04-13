from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTextEdit, QPushButton
from PyQt5.QtCore import Qt

class MainPage(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Описание функционала в Markdown-подобном формате
        description = QTextEdit()
        description.setReadOnly(True)
        description.setMarkdown("""
# Добро пожаловать в Помощник-бот!

Этот бот поможет вам развлечься и найти музыку по вашему вкусу.

## Возможности:
- **Анекдоты**: Получите случайный анекдот из нашей коллекции.
- **Музыка**: Ответьте на несколько вопросов, и мы подберём песни, соответствующие вашим предпочтениям.
        """)
        description.setAlignment(Qt.AlignCenter)
        layout.addWidget(description)

        # Кнопка для перехода к анекдотам
        jokes_button = QPushButton("Анекдоты")
        jokes_button.clicked.connect(lambda: self.parent.show_page(1))
        layout.addWidget(jokes_button)

        # Кнопка для перехода к музыке
        music_button = QPushButton("Музыка")
        music_button.clicked.connect(lambda: self.parent.show_page(2))
        layout.addWidget(music_button)

        self.setLayout(layout)