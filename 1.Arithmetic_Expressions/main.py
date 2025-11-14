from lexer import lexer
from parser import parser

if __name__ == "__main__":
    print("Rust-style Arithmetic Evaluator ; ex : let x= 10; x = x + 1 (INVALID) let mut y =10; y = y + 1 (VALID);")
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
                print("Result:", result)
            else:
                print("Parsed successfully (No direct Result)")
        except Exception as e:
            print("Error:", e)
