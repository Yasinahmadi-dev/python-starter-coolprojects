from pathlib import Path
import shutil

DIRECTORIES = {

    ".pdf": "PDFs",
    ".txt": "documents",
    ".csv": "Spreadsheets",
    ".png": "images",
}    
folder = Path("test_folder")

for item in folder.iterdir():
    # ONLY inspect actual files, ignore folders
    if item.is_file():
        extension = item.suffix.lower()

        #look up the folder name from our rulebook
        #if the extension isn't in the dictionary, default to 'others'
        target_folder_name = DIRECTORIES.get(extension, "Others")

        destination_dir = folder / target_folder_name

        destination_dir.mkdir(exist_ok=True)

        shutil.move(item, destination_dir)

        print(f"Moved '{item.name}' to {destination_dir}/")