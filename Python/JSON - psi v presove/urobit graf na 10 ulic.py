import get_info_about_dog_count as doginfo
import matplotlib.pyplot as plt
import os

def compile_data(myData: dict) -> list[tuple]:
    sorted_data:list = [(street, val) for street, val in myData.items()] # prehodit do listu pre moznost zoradit podla indexu 2 (pocet)
    sorted_data.sort(key=lambda x: x[1], reverse=True) # zoradit podla poctu psov
    
    return sorted_data[:10] # vrat 10 prvych

def make_graph(myData: dict) -> None:
    sorted_data:list = compile_data(myData)

    labels: list = []
    sizes: list = []
    for val in sorted_data: # ulozit hodnoty samostatne
        labels.append(val[0])
        sizes.append(val[1])
    
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90) # graf
    plt.title("Top 10 najpsích ulíc")

    output_folder:str = os.path.dirname(__file__)
    file_name:str = "kolacovy graf.png"
    file_path:str = os.path.join(output_folder, file_name) # cesta na subor

    plt.savefig(file_path, format="png", dpi=300)
    plt.show()

make_graph(doginfo.get_dog_count_per_street(doginfo.data))