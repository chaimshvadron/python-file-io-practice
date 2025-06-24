def WriteTxtFile(fileName, content):
    with open(fileName, 'w', encoding='utf-8') as file:
        file.write(content)


def ReadTxtFileAndPrintLineNumbers(fileName):
    try:
        with open(fileName, 'r', encoding='utf-8') as file:
            for line_number, line in enumerate(file, start=1):
                if any(char.isdigit() for char in line):
                    print(f"{line_number}: {line.strip()}")
    except FileNotFoundError:
        print(f"Error: The file '{fileName}' does not exist.")






if __name__ == "__main__":
    fileName = "my_text.txt"
    content = """Hello world
It’s the first exercise in I/O
That mean it is number 1
Not 2
Not three
It is exciting
And i am all 4 it"""
    WriteTxtFile(fileName, content)
    ReadTxtFileAndPrintLineNumbers(fileName)