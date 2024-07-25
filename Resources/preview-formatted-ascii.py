import sys

def interpret_escape_sequences(text):
    # Replace escape sequences
    text = text.replace("\\033", "\033")
    text = text.replace("\\e", "\033")
    return text

def display_formatted_ascii(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            formatted_content = interpret_escape_sequences(content)
            print(formatted_content)
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except IOError:
        print(f"Error reading file '{file_path}'.")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py <filename>")
    else:
        filename = sys.argv[1]
        display_formatted_ascii(filename)
