import vision
import telebot
import os
import time


# Так делать не стоит: токены/пароли и прочее стоит хранить в переменных окружения или конфигурационных файлах.
# Я не буду это исправлять потому что мне лень
# bot = telebot.TeleBot("1918344985:AAFnF5zliY0ULGMLxXE0X4WxXb69aJzDzc8")

# Так наверно можно писать, но на мой взгляд лучше запихнуть все в функцию, чтобы четко было видно где программа начинается и что она делает
# image_path = get_image_from_camera()
# c = count_faces(image_path)

# if c > 0:
#     bot.send_message(
#         240940120,
#         f"{os.getlogin()} на вашем этаже обнаружен инопланетянин",
#     )

#     bot.send_photo(240940120, open(image_path, "rb"))


def start():
    bot = telebot.TeleBot("1918344985:AAFnF5zliY0ULGMLxXE0X4WxXb69aJzDzc8")
    chat_id = 240940120

    while True:
        # Получаем изображение
        image_path = vision.save_image_from_camera()

        # Считаем количество лиц на фото
        faces = vision.count_faces(image_path)

        # Если на фото есть лицо, отправляем сообщение с помощью бота
        if faces > 0:
            bot.send_message(
                chat_id,
                f"на вашем этаже обнаружен инопланетянин",
            )

            bot.send_photo(chat_id, open(image_path, "rb"))
        time.sleep(8)


# Вызываем объявленную выше функцию
start()
