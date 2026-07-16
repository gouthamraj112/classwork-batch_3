from typing import Union

def process_input(data: Union[str, bytes])-> None:
    if isinstance(data,str):
        print("processing text:",data)
    elif isinstance(data,bytes):
        print("processing Image/audio bytes:",data)

print(process_input("Artificial Intelligence"))

print(process_input(b'\x89PNG\r\n'))

#Union-one variable cxan accept different data types.
#89 - non printable byte used to identify PNG imaage
#PNG - PNG image
#\r- carriage return
