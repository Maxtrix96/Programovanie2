import get_info_about_dog_count as doginfo
import os

with open(doginfo.ABSPATH_organizedFIle, "w", encoding="utf-8") as file:
    writing = doginfo.finalize_data(doginfo.get_dog_count_data(doginfo.data))
    file.write(writing)
    print(f"Dáta pre psov na ulicu organizované podľa časti mesta môžete nájsť v súbore {os.path.basename(doginfo.ABSPATH_organizedFIle)}")