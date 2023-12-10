import os

'''
- main_folder/
  - script_folder/
    - your_script.py
  - data_folder/
    - your_file.txt
'''

scriptPath = os.path.abspath(__file__)

#relativePath = os.path.join("..", "Dejepiss", "sussous.txt")
''' ^
- programovanie/
  - python/
    - your_script.py
  - Dejepiss/
    - your_file.txt
'''

#relativePath = os.path.join("..", "..", "..", "Dejepiss", "sussous.txt")
''' ^
- skola/
    - Dejepis/
        - sussous.txt
    - programovanie/
        - python/
            - reading files without knowing absolute path.py
'''

scriptPath = os.path.dirname(__file__) #

relativePath = "Dejepiss/sussous.txt"

''' ^
- programovanie/
    - python/
        - your_script.py
        - Dejepiss/
            - your_file.txt
'''

scriptPath = os.path.abspath(os.path.join(scriptPath, relativePath))

# Open and manipulate the file as needed
with open(scriptPath, 'r') as file:
    content = file.read()
    print(f"Content of the file:\n{content}")