def add_picture_to_post(picture):
    """Функция добавления в хранилище картинки
    и возврата пути хранения картинки"""
    filename = picture.filename
    path = f'./uploads/images/{filename}'
    picture.save(path)
    return path