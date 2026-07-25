import os

chickens = R"C:\Users\anton\curseforge\minecraft\Instances\Adventures of a Magician - Magician Quest - Magic RPG\mods"
mine = R"C:\Users\anton\curseforge\minecraft\Instances\Adventures of a Magician - Magician Quest - Magic RPG (2)\mods"

from pathlib import Path

def find_unique_files(folder1_path, folder2_path):
    # Convert string paths to Path objects
    dir1 = Path(folder1_path)
    dir2 = Path(folder2_path)
    
    # Validate that both folders exist
    if not dir1.is_dir() or not dir2.is_dir():
        raise ValueError("One or both of the provided paths do not exist or are not directories.")
    
    # Get relative file paths for both folders (ignoring subdirectories themselves, just getting files)
    # rglob("*") recursively finds all files and folders. We filter for files only.
    files_in_dir1 = {p.relative_to(dir1) for p in dir1.rglob("*") if p.is_file()}
    files_in_dir2 = {p.relative_to(dir2) for p in dir2.rglob("*") if p.is_file()}
    
    # Perform the XOR operation using set symmetric difference (^)
    unique_relative_paths = files_in_dir2 ^ files_in_dir1
    
    # Reconstruct the absolute paths so you know exactly where they are
    xor_files = []
    for rel_path in unique_relative_paths:
        if rel_path in files_in_dir1:
            xor_files.append(dir1 / rel_path)
        else:
            xor_files.append(dir2 / rel_path)
            
    return xor_files

# --- Example Usage ---
if __name__ == "__main__":
    # Use raw strings (r"...") for Windows paths to handle backslashes correctly
    folder_a = chickens
    folder_b = mine
    
    try:
        print("Scanning folders... (this might take a moment for large directories)")
        result = find_unique_files(folder_a, folder_b)
        
        print(f"\nFound {len(result)} files that exist in only one folder:\n")
        for file in sorted(result):
            print(file)
            
        # Optional: Save the results to a text file
        with open("xor_files_list.txt", "w", encoding="utf-8") as f:
            for file in sorted(result):
                f.write(f"{file}\n")
                
    except Exception as e:
        print(f"Error: {e}")