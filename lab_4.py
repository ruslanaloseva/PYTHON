from typing import List


class SocialNetwork:
    """
    Базовый класс социальной сети.
    """

    def __init__(self, name: str, users_count: int) -> None:
        """
        Конструктор базового класса.

        Args:
            name (str): название сети
            users_count (int): количество пользователей
        """
        self.name: str = name
        self.users_count: int = users_count

        # защищённый список постов
        # используется для хранения контента платформы
        self._posts: List[str] = []

        # приватный ID платформы
        self.__network_id: int = id(self)

    def add_post(self, text: str) -> None:
        """
        Добавить пост.

        Args:
            text (str): текст поста
        """
        self._posts.append(text)

    def send_message(self, user: str, message: str) -> str:
        """
        Отправить сообщение пользователю.

        Returns:
            str: результат отправки
        """
        return f"Message sent to {user}: {message}"

    def __str__(self) -> str:
        return f"Social network {self.name}, users: {self.users_count}"

    def __repr__(self) -> str:
        return f"SocialNetwork(name={self.name!r}, users_count={self.users_count!r})"


class VK(SocialNetwork):
    """
    Дочерний класс социальной сети VK.
    """

    def __init__(self, users_count: int, groups: int) -> None:
        super().__init__("VK", users_count)
        self.groups: int = groups

    def send_message(self, user: str, message: str) -> str:
        """
        Переопределённый метод отправки сообщений.

        Причина перегрузки:
        VK поддерживает отправку сообщений с
        дополнительными вложениями (стикеры, медиа).

        Returns:
            str: результат отправки
        """
        return f"VK message to {user}: {message} 📩"

    def __str__(self) -> str:
        return f"VK network, users: {self.users_count}, groups: {self.groups}"

    def __repr__(self) -> str:
        return (
            f"VK(users_count={self.users_count!r}, groups={self.groups!r})"
        )


class Max(SocialNetwork):
    """
    Дочерний класс социальной сети Max.
    """

    def __init__(self, users_count: int, channels: int) -> None:
        super().__init__("Max", users_count)
        self.channels: int = channels

    def send_message(self, user: str, message: str) -> str:
        """
        Переопределённый метод отправки сообщений.

        Причина перегрузки:
        платформа Max ориентирована на каналы
        и групповые коммуникации.

        Returns:
            str: результат отправки
        """
        return f"Message in Max channel to {user}: {message}"

    def __str__(self) -> str:
        return f"Max network, users: {self.users_count}, channels: {self.channels}"

    def __repr__(self) -> str:
        return (
            f"Max(users_count={self.users_count!r}, channels={self.channels!r})"
        )


if __name__ == "__main__":
    vk = VK(90000000, 500000)
    max_net = Max(20000000, 120000)

    vk.add_post("Hello VK!")
    max_net.add_post("First post in Max")

    print(vk)
    print(vk.send_message("Alex", "Hi!"))

    print()

    print(max_net)
    print(max_net.send_message("Maria", "Welcome!"))