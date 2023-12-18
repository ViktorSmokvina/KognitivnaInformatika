from deepface import DeepFace
import cv2
import os

def prepoznavanje_lica(slika):
    img = cv2.imread(slika)

    obrada_slike = DeepFace.analyze(img_path=slika, actions=["age", "gender"])

    for lice in obrada_slike:
        x, y, w, h = lice["region"]["x"], lice["region"]["y"], lice["region"]["w"], lice["region"]["h"]
        age = lice["age"]
        gender = max(lice["gender"], key=lice["gender"].get)
        if gender == "Man":
            gender = "Musko"
        elif gender == "Woman":
            gender = "Zensko"

        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(img, f"Dob: {age} godina, Spol: {gender}", (x, y - 10), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 255, 0), 2)

    trenutna_lokacija = os.path.dirname(os.path.realpath(__file__))
    lokacija_obradene_slike = os.path.join(trenutna_lokacija, "obradena_" + os.path.basename(slika))
    cv2.imwrite(lokacija_obradene_slike, img)
    
    return lokacija_obradene_slike

slika = r"C:\Users\Viktor Smokvina\Desktop\prepoznavanje_lica\trump.jpg"
obradena_slika = prepoznavanje_lica(slika)
print(f"Obrađena slika je spremljena na lokaciji: {obradena_slika}")

os.startfile(obradena_slika)