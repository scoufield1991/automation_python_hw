

def deleting_numbers(file_name):
    """
    4. You have a file of unknown length. Write a function that will remove all numbers from each line of the file.
    """
    with open(file_name, 'r') as file:
        data = file.read()
    new_text = ''
    for index in data:
        if not index.isdigit():
            new_text = new_text + index
    with open(file_name, 'w') as file:
        data_to_write_text = file.write(new_text)

    return new_text


if __name__ == '__main__':
    default_text = """Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of
    classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at
    Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum
    passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem
    Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by
    Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The
    first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..", comes from a line in section 1.10.32."""
    with open('qwerty.txt', 'w') as files:
        files.write(default_text)
    print(deleting_numbers('qwerty.txt'))
