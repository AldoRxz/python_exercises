import argparse
import os
from orchestrator import Orchestrator


def validate_path(path):
    if not os.path.exists(path):
        print(f"Error: Path '{path}' does not exist.")
        return False
    return True


def validate_folders(folders, base_path):
    for folder in folders:
        folder_path = os.path.join(base_path, folder)
        if not os.path.exists(folder_path):
            print(f"Error: Folder '{folder_path}' does not exist.")
            return False
    return True


def main():
    parser = argparse.ArgumentParser(description="Process CSV files.")
    parser.add_argument("-p", "--path", type=str, help="Path to folders with CSV files", required=True)
    parser.add_argument("-f", "--folders", type=str, nargs="+", help="List of folders to process", required=True)
    args = parser.parse_args()

    if not validate_path(args.path) or not validate_folders(args.folders, args.path):
        return

    orchestrator = Orchestrator(args.path, args.folders)
    orchestrator.execute()

    result = orchestrator.query_group_subgroup("verduras", "v_bajo_en_potasio", "lipids")
    if result is not None:
        print(f"Total {result} for 'lipids' in 'v_bajo_en_potasio' subgroup of 'verduras' group.")


if __name__ == "__main__":
    main()
