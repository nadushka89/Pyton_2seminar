import model

def input_class():
   while True:
      answer_class= input('Введите класс  ').upper()
      if answer_class in ['7А','7Б', '7В']:
         return answer_class
      else:
         print('Недопустимый класс. Выберите 7А, 7Б или 7В')

def input_subject():
   while True:
      answer_subject=input('Введите предмет  ').lower()
      if answer_subject in ['математика','русский язык', 'литература']:
         return answer_subject
      else:
         print('В этом классе не преподают такой предмет.')

def who_answer():
   return input('Кого вызовем к доске?  ')

def valid_student():
   return input('Такого ученика нет.Кого вызовем к доске?  ')

def what_mark():
   mark_answer= int(input('На какую оценку ответил?  '))
   while True:
      if mark_answer>=1 and mark_answer<=5:
         return mark_answer
      print ('Введите оценку от 1 до 5')
      mark_answer = int(input ('На какую оценку ответил?  '))




def list_of_child(journal:dict):
   for i, child in enumerate(journal,1):
      print(f'{i}.{child:20} {journal.get(child)}')






