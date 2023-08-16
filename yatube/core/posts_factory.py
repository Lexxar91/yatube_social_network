from posts.models import Post, User, Group


class PostFactory:
    """
    Фабрика для создания, обновления и удаления объектов Post.
    """

    @staticmethod
    def create(author: User, text: str, group: Group = None) -> Post:
        """
        Создает и возвращает объект типа Post.

        :param author: Автор поста (объект User).
        :param text: Текст поста.
        :param group: Группа для поста (необязательный, объект Group).
        :return: Созданный объект Post.
        """
        post = Post.objects.create(
            author=author,
            text=text,
            group=group
        )
        return post

    @staticmethod
    def update(
            post: Post,
            author: User,
            text: str,
            group: Group = None
    ) -> Post:
        """
        Обновляет и сохраняет пост.

        :param post: Объект поста для обновления.
        :param author: Новый автор поста (объект User).
        :param text: Новый текст поста.
        :param group: Новая группа поста (необязательный, объект Group).
        :return: Обновленный объект Post.
        """
        post.author = author
        post.text = text
        post.group = group
        post.save()
        return post

    @staticmethod
    def delete(post: Post) -> bool:
        """
        Удаляет указанный пост.

        :param post: Объект поста для удаления.
        :return: True, если пост успешно удален.
        """
        post.delete()
        return True
