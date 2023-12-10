import get_info_about_dog_count as doginfo
import os

with open(doginfo.ABSPATH_dogsPerStreet, "w", encoding="utf-8") as file:
    file.write(doginfo.write_partial_data(doginfo.data))
    print(f"Výsledný súbor s dátami najdete v súbore: {os.path.basename(doginfo.ABSPATH_dogsPerStreet)}")