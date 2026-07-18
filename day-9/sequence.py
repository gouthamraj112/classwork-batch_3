from typing import Sequence
def process_management(message:Sequence[str])->None:
    print('message Recieved')

    for m in message:
        print(m)

texts=[
    "Hello",
    "How are you",
    "Woring with fastapi"
]

text_tuple=(
    "Checking the input",
    "Tuple input",
    "Working or not"
)
process_management(text_tuple)
