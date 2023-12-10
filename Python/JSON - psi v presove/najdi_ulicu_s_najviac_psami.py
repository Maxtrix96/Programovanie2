import get_info_about_dog_count as doginfo

mostDogs = doginfo.find_most_dogs(doginfo.data).replace("Ulica:  ", "ulici:")
result = f"Najviac psov je na {mostDogs}"

print(result)