from unittest import result
from deepface import DeepFace
import json


def face_verify(img_1, img_2):
    try:
        result_dict = DeepFace.verify(img1_path=img_1, img2_path=img_2)

        with open('result.json', 'w') as file:
            json.dump(result_dict, file, indent=4, ensure_ascii=False)

        # return result_dict
        if result_dict.get("verified"):
            return 'Проверка пройдена! Все отлично!'
        return 'Алярм, Алярм! Нарушитель!'

    except Exception as ex:
        return ex


def face_recogn():
    try:
        result = DeepFace.find(img_path='faces\mask1.jpg', db_path='ilona')
        result = result.values.tolist()
        return result

    except Exception as ex:
        return ex


def face_analyse():
    try:
        result_dict = DeepFace.analyze(
            img_path='faces/mask1.jpg', actions=['age'])

        with open('face_analyse.json', 'w') as file:
            json.dump(result_dict, file, indent=4, ensure_ascii=False)
            return result_dict

    except Exception as ex:
        return ex


def main():
    #print(face_verify(img_1='faces/mask1.jpg', img_2='faces/bezos_mask.jpg'))
    # print(face_recogn())
    print(face_analyse())


if __name__ == '__main__':
    main()
