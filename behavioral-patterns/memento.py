from dataclasses import dataclass, field


@dataclass
class Editor:
    text: str = ""
    cursor_pos: list[int] = field(default_factory=lambda: [0, 0])
    width: int = 80

    def copy(self) -> "Editor":
        return Editor(self.text, list(self.cursor_pos), self.width)

    def update(self, text: str):
        self.text += text

        out_of_bounds = self.cursor_pos[0] + len(text) > self.width

        if out_of_bounds:
            self.cursor_pos[0] = self.cursor_pos[0] + len(text) % self.width
            self.cursor_pos[1] += 1
        else:
            self.cursor_pos[0] += len(text)
        

class Snapshot:
    def __init__(self, editor: Editor):
        self.editor = editor
        self.saved_editor = editor.copy()

    def restore(self):
        self.editor.text = self.saved_editor.text
        self.editor.cursor_pos = self.saved_editor.cursor_pos
        self.editor.width = self.saved_editor.width


def main():
    editor = Editor()
    backup = Snapshot(editor)

    editor.update("Hello World!")
    print(editor)

    backup.restore()
    print(editor)



if __name__ == "__main__":
    main()
 
    """
    Editor(text='Hello World!', cursor_pos=[12, 0], width=80)
    Editor(text='', cursor_pos=[0, 0], width=80)
    """
