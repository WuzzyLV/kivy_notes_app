from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
import csv
from utils import notes_utils
from uuid import uuid4
from widgets.note_widget import NoteWidget

class MainWindow(Screen):
    # 
    current_user = ObjectProperty(None)
    welcome_text = StringProperty("Welcome!")

    def on_enter(self):
        self.load_notes()
        
    def load_notes(self):
        notes_container = self.ids.notes_container
        notes_container.clear_widgets()

        example_notes = [
            {"uuid": str(uuid4()), "note": "My first note", "color": "#FF5733"},
            {"uuid": str(uuid4()), "note": "Another important note", "color": "#33FF57"}
        ]
        
        for note in example_notes:
            note_widget = NoteWidget(
                note_uuid=note["uuid"],
                note_text=note["note"],
                note_color=note["color"],
                delete_callback=self.delete_note,
                edit_callback=self.edit_note
            )
            notes_container.add_widget(note_widget)


    def update_welcome_text(self):
        self.welcome_text = f"Hello, {self.current_user["username"]}!"

    def delete_note(self, note_uuid):
        print(f"Deleting note with UUID: {note_uuid}")
        pass
    def edit_note(self, note_uuid):
        print(f"Editing note with UUID: {note_uuid}")
        pass

    def logout_button(self):
        self.current_user = {}
        self.welcome_text = "Welcome!"
        self.manager.current = 'login'
