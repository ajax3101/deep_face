from deepface import DeepFace


def face_verify(img_1, img_2):
    try:
        result_dict = DeepFace.verify(img1_path=img_1, img2_path=img_2)
        return result_dict

    except Exception as ex:
        return ex


def main():
   print(face_verify(img_1='faces/mask1.jpg', img_2='faces/mask2.jpg'))


if __name__ == '__main__':
    main()
