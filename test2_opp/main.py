import argparse
import os
from orchestrator import Orchestrator


def validate_path(path):
    if os.path.exists(path) and os.path.isdir(path):
        print('hola')
        return True
    else:
        print(f"Invalid path: {path}")
        return False
    pass


def validate_folders(folders):
    for folder in folders:
        folder_path = os.path.join(os.getcwd(), folder)
        if os.path.exists(folder_path) and os.path.isdir(folder_path):
            continue
        else:
            print(f"Invalid folder: {folder}")
            return False
    return True


def main():
    parser = argparse.ArgumentParser(description='Script description.')
    parser.add_argument('-p', '--path', help='Path to data files', required=True)
    parser.add_argument('-f', '--folders', help='List of folders', nargs='+', required=True)

    args = parser.parse_args()

    # Validate path
    if not validate_path(args.path):
        print("Invalid path. Exiting.")
        return

    # Validate folders
    if not validate_folders(args.folders):
        print("Invalid folder(s). Exiting.")
        return

    orchestrator = Orchestrator(args.path, args.folders)
    orchestrator.execute()

    # show all the groups and subgroups
    orchestrator.print_all_groups_subgroups()

    result = orchestrator.query_group_subgroup("verduras", "v_bajas_en_potasio.csv", "lipids")
    if result is not None:
        print(f"Total {result} for 'lipids' in 'v_bajas_en_potasio.csv' subgroup of 'verduras' group.")

    result = orchestrator.query_group_subgroup("verduras", "v_bajas_en_potasio.csv", "protein")
    if result is not None:
        print(f"Total {result} for 'protein' in 'v_bajas_en_potasio.csv' subgroup of 'verduras' group.")

    result = orchestrator.query_group_subgroup("verduras", "v_bajas_en_potasio.csv", "carbohydrates")
    if result is not None:
        print(f"Total {result} for 'carbohydrates' in 'v_bajas_en_potasio.csv' subgroup of 'verduras' group.")
'''
4. Crear un método que muestre la suma total de los elementos de los ingredientes, para protein, lipids, carbohydrates obj.CARBOHYDRATES.
'''

if __name__ == "__main__":
    main()
