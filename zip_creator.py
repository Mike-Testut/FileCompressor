import zipfile
import pathlib


def make_archive(filepaths, folder, new_name):
    new_filepath = pathlib.Path(folder,f"{new_name}.zip")

    with zipfile.ZipFile(new_filepath, 'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)

