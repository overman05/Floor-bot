from typing import Any, Tuple
import cv2
import requests
import time
import concurrent.futures
import pik_api


# Так писать функции не стоит. Ссылка с которой нужно качать фото должна передаваться как параметр функции
def save_image_from_camera(
    name="./test.jpg",
) -> str:
    """Функция скачивает фотографию и сохраняет в файл с именем, указанным в параметере name"""
    method = pik_api.API("+79778864755", "hywku0-zohcem-bejJub")
    massiv = method.intercoms(154520)
    photo = massiv[27803]["photo_url"] if massiv else ""
    r = requests.get(photo)

    with open(name, "wb") as f:
        f.write(r.content)

    return name


# В боте не нужно использовать эту функцию, она нужна для вывода окна с фотографией
def viewImage(image, name_of_window):
    cv2.namedWindow(name_of_window, cv2.WINDOW_NORMAL)
    cv2.imshow(name_of_window, image)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()


def count_faces(
    image_path: str,
) -> int:  # ": str" рядом с image_path тоже необязательное указание типа параметра. Тебе не нужно это ставить в своих функциях.
    """Функция принимает путь к файлу(его имя) и возвращает количество обнаруженных лиц"""
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(
        gray, scaleFactor=1.1, minNeighbors=5, minSize=(10, 10)
    )
    print(f"Найдено лиц: {len(faces)}")

    # Эта часть не нужна, так как мы не выводим и не сохраняем обработанное изображение

    # Рисуем квадраты вокруг лиц
    # for (x, y, w, h) in faces:
    #     cv2.rectangle(image, (x, y), (x + w, y + h), (255, 255, 0), 2)
    # viewImage(image, faces_detected)

    return len(faces)


# Этот файл хранит только объявление функций и не должен содеражть исполняемый код.
# Если оставить этот цикл здесь, то после того, как ты имортируешь его, код будет вечно работать в этом цикле вместо корректной работы
# Запусти test.py (python example/test.py) чтобы увидеть как это происходит.

# while True:
#     get_image_from_camera = get_image_from_camera(name="./test.jpg")
#     count_faces = count_faces(image_path: str)
#     time.sleep(10)
