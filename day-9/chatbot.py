from typing import Union, Sequence
InputData=Union[str,bytes]

def chatbots(inputs:Sequence[InputData]):
    for item in inputs:
        if isinstance(item,str):
            print("User Text:",item)
        else:
            print("Image Uploaded: (",len(item), "bytes)")

conversation=(
    "Hi",
    "show me nearby restaurant",
    b'\x89PNG',
    "Explain the image"
)

chatbots(conversation)
