import FreeSimpleGUI as gui

label1 = gui.Text("Select file(s) to compress")
input_box1 = gui.Input()
choose_button1 = gui.FileBrowse("Choose file(s)")

label2 = gui.Text("Select destination folder")
input_box2 = gui.Input()
choose_button2 = gui.FolderBrowse("Choose folder")

window = gui.Window(title="Compress Files", layout=[[label1,input_box1,choose_button1],[label2,input_box2,choose_button2]])
window.read()
window.close()
