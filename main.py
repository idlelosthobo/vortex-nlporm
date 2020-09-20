from vortex.core import Core

vortex = Core()

input_string = str()

while True:
    input_string = input('Say something: ')
    if input_string == 'quit':
        break
    else:
        vortex.read_sentence(input_string)