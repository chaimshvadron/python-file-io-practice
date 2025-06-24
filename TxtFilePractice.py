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


def analizeTextFile(fileName):
    try:
        with open(fileName, 'r', encoding='utf-8') as file:
            even_word_lines = 0
            total_words = 0
            total_letters = 0
            word_count_dict = {}

            for line in file:
                line = line.strip()
                if not line:
                    continue
                words = line.split()
                words_no_numbers = [w for w in words if not w.isdigit()]
                total_words += len(words_no_numbers)
                total_letters += sum(c.isalpha() for c in line)
                if len(words) % 2 == 0:
                    even_word_lines += 1
            for w in words_no_numbers:
                w_clean = w.lower()
                if w_clean in word_count_dict:
                    word_count_dict[w_clean] += 1
                else:
                    word_count_dict[w_clean] = 1



            most_common_word = max(word_count_dict, key=word_count_dict.get) if word_count_dict else None

            print(f"Number of lines with even number of words: {even_word_lines}")
            print(f"Total number of words (excluding numbers): {total_words}")
            print(f"Total number of letters (excluding spaces and empty lines): {total_letters}")
            print(f"Most frequent word: {most_common_word}")

    except FileNotFoundError:
        print(f"Error: The file '{fileName}' does not exist.")

def add_word_count_to_lines(fileName, sumFileName):
    try:
        with open(fileName, 'r', encoding='utf-8') as orFile, open(sumFileName, 'w', encoding='utf-8') as sumFile:
            for line in orFile:
                word_count = len(line.strip().split())
                new_line = f"{line.strip()} (word count: {word_count})\n"
                sumFile.write(new_line)
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
    analizeTextFile(fileName)
    add_word_count_to_lines(fileName, "sum_" + fileName)