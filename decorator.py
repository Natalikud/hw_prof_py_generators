import datetime

def path_to_file(path):
  def write_logs(old_function):

      def new_function(*args,**kwargs):
          date = datetime.datetime.now()
          name = old_function.__name__
          with open(path,mode='a',encoding='utf-8') as file:
              file.write(f'{date} вызвана функция {name} с аргументами {args} и {kwargs}.\n ')

          result = old_function(*args,**kwargs)


          with open(path,mode='a',encoding='utf-8') as file:
              file.write(f'Возвращаемое значение:{result}\n')
              file.write(f'{date} записан результат работы функции в файл.\n')
              file.write(f'end\n')
          return result
      return new_function
  return write_logs