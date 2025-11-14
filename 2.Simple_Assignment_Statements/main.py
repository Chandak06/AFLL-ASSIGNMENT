from lexer import lexer
from parser import parser

if __name__ == "__main__":
    print("Rust-style Simple Assignment Evaluator; ex : let mut x = 10 ;let y = 5;")
    print("Type 'exit;' to quit.\n")

    while True:
        data = input(">>> ")
        if data.strip().lower() == "exit;":
            print("Exiting...")
            break
        if not data.strip():
            continue

        lexer.input(data)
        try:
            result = parser.parse(data)
            if result is not None:
                print("Accepted:", result)
            else:
                print("Parsed successfully (No direct Result)")

        except Exception as e:
            print("Error:", e)
