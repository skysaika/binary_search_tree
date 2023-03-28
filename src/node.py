class Node:
    """Класс для хранения данных"""

    def __init__(self, data: dict) -> None:
        """Сохраняю данные. Инициализирую пустые левый и правый атрибуты"""
        self.data = data
        self.left: Node | None = None
        self.right = None
