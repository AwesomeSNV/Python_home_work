from pathlib import Path


def group_rename_files(new_name: str, ext_renamed: str, /, count_dig: int = 3, ext_new: str = None,
                       saved_range: range = (3, 6), path: str = None) -> int:
    if ext_new is None:
        ext_new = ext_renamed

    work_path = Path.cwd() if path is None else Path(path)
    count_renamed = 0
    for p in work_path.iterdir():
        if p.is_file() and p.suffix == ext_renamed:
            number = str(count_renamed).zfill(count_dig)
            file_name = f"{p.stem[saved_range[0]:saved_range[1]]}{new_name}{number}{ext_new}"
            p.rename(Path(p.parent, file_name))
            count_renamed += 1

    return count_renamed


if __name__ == '__main__':
    print("Файлов переименовано: ", group_rename_files("new", ".jpg", ext_new=".png", count_dig=4))