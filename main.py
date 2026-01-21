import FreeSimpleGUI as gui
import zip_creator

label1 = gui.Text("Select file(s) to compress")
input_box1 = gui.Input()
choose_button1 = gui.FilesBrowse("Choose file(s)", key="files")

label2 = gui.Text("Select destination folder")
input_box2 = gui.Input()
choose_button2 = gui.FolderBrowse("Choose folder", key="folder")

label3 = gui.Text("Name compressed file")
input_box3 = gui.Input(key="new_name")

compress_button = gui.Button("Compress")

window = gui.Window(title="Compress Files", layout=[[label1,input_box1,choose_button1],
                                                    [label2,input_box2,choose_button2],
                                                    [label3,input_box3],
                                                    [compress_button]])
while True:
    event, values = window.read()
    print(event, values)

    filepaths = values["files"].split(';')
    folder = values["folder"]
    new_name = values["new_name"]

    match event:
        case "Compress":
            zip_creator.make_archive(filepaths, folder, new_name)
        case gui.WIN_CLOSED:
            break
window.close()
