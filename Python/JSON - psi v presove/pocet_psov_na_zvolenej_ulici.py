import get_info_about_dog_count as doginfo

doginfo.create_file_paths()

streetUserInput = input("Zadajte celý názov ulice na ktorej chcete nájsť počet psov (ak nechcete túto informáciu, zadajte písmeno n, pre zoznam ulíc zadajte písmeno z): ")
print(doginfo.get_amount_of_dogs_on_strt(doginfo.data, streetUserInput))