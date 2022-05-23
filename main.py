from deepface import DeepFace
import json

def face_verify(img_1, img_2):
    try:
        result_dict = DeepFace.verify(img1_path=img_1, img2_path=img_2)
        
        with open('result.json', 'w') as file:
            json.dump(result_dict, file, indent=4, ensure_ascii=False)

        #return result_dict
        if result_dict.get("verified"):
            return 'Проверка пройдена! Все отлично!'
        return 'Алярм, Алярм! Нарушитель!'

    except Exception as ex:
        return ex


def main():
   print(face_verify(img_1='faces/mask1.jpg', img_2='faces/bezos1.jpg'))


if __name__ == '__main__':
    main()
