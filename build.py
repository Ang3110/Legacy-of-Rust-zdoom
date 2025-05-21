import os
import sys
import zipfile

# Define the source directories
MENU_ITEMS = {
    'LOR-ZD': 'src/LOR-ZD',
    'LOR-ZDCE': 'src/LOR-ZDCE',
}
BUILD_DIR = 'Build'

def makepkg(source_path, dest_path):
    destination = dest_path + ".pk3"
    with zipfile.ZipFile(destination, 'w', zipfile.ZIP_DEFLATED) as distzip:
        for root, _, files in os.walk(source_path):
            for name in files:
                full_path = os.path.join(root, name)
                rel_path = os.path.relpath(full_path, source_path)
                distzip.write(full_path, rel_path)

def build_project(source_dir):
    project_name = os.path.basename(source_dir)
    dest_base = os.path.join(BUILD_DIR, project_name)
    os.makedirs(BUILD_DIR, exist_ok=True)
    makepkg(source_dir, dest_base)
    print(f"\nBuilt {project_name}.pk3 in {BUILD_DIR}/")

def main():
    options = list(MENU_ITEMS.keys())

    try:
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("=== 📦 PK3 Compiler Menu ===\n")
            for idx, option in enumerate(options, start=1):
                print(f"{idx}. {option}")
            print("\nEnter the number of the project to build, or type 'exit' to quit.")

            user_input = input("Your choice: ").strip().lower()

            if user_input == 'exit':
                print("\nExiting PK3 Compiler.")
                break

            if user_input.isdigit():
                choice = int(user_input)
                if 1 <= choice <= len(options):
                    selected_option = options[choice - 1]
                    build_project(MENU_ITEMS[selected_option])
                    input("\nPress Enter to return to the menu.")
                else:
                    print("\nInvalid selection. Please choose a valid number.")
            else:
                print("\nInvalid input. Please enter a number corresponding to the project.")
    except KeyboardInterrupt:
        print("\nExiting PK3 Compiler.")

if __name__ == '__main__':
    main()
