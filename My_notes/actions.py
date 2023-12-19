import file_operation
import My_Note
import kreate

number = 3


def add():
    note = kreate.create_note(number)
    array = file_operation.read_file()
    for notes in array:
        if My_Note.Note.get_id(note) == My_Note.Note.get_id(notes):
            My_Note.Note.set_id(note)
    array.append(note)
    file_operation.write_file(array, 'a')
    print('Заметка добавлена...')




def show(text):
    logic = True
    array = file_operation.read_file()
    if text == 'date':
        date = input('Введите дату в формате dd.mm.yyyy: ')
    for notes in array:
        if text == 'all':
            logic = False
            print(My_Note.Note.map_note(notes))
        if text == 'id':
            logic = False
            print('ID: ' + My_Note.Note.get_id(notes))
        if text == 'date':
            logic = False
            if date in My_Note.Note.get_date(notes):
                print(My_Note.Note.map_note(notes))
    if logic == True:
        print('Заметки не найдены.')


def id_edit_del_show(text):
    id = input('Введите id необходимой заметки:  ')
    array = file_operation.read_file()
    logic = True
    for notes in array:
        if id == My_Note.Note.get_id(notes):
            logic = False
            if text == 'edit':
                note = kreate.create_note(number)
                My_Note.Note.set_title(notes, note.get_title())
                My_Note.Note.set_body(notes, note.get_body())
                My_Note.Note.set_date(notes)
                print('Заметка изменена...')
            if text == 'del':
                array.remove(notes)
                print('Заметка удалена...')
            if text == 'show ':
                print(My_Note.Note.map_note(notes))
    if logic == True:
        print('Такой заметки нет, возможно, вы ввели неверный id')
    file_operation.write_file(array, 'a')