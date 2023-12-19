from datetime import datetime
import uuid


class Note:
    def __init__(self, id=str(uuid.uuid1())[0:3], title=" text ", body=" text ",
                 date=str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))):
        self.id = id
        self.title = title
        self.body = body
        self.date = date

    def get_id(self):
        return self.id

    def get_title(self):
        return self.title

    def get_body(self):
        return self.body

    def get_date(self):
        return self.date

    def set_id(note):
        note.id = str(uuid.uuid1())[0:3]

    def set_title(note, title):
        note.title = title

    def set_body(note, body):
        note.body = body

    def set_date(note):
        note.date = str(datetime.now().strftime("%d.%m.%Y %H:%M:%S"))

    def to_string(note):
        return note.id + ';' + note.title + ';' + note.body + ';' + note.date

    def map_note(note):
        return '\nID: ' + note.id + '\n' + 'заголовок: ' + note.title + '\n' + 'Заметка: ' + note.body + '\n' + 'Дата публикации: ' + note.date
