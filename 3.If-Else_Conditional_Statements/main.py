from lexer import lexer
from parser import parser

if __name__ == "__main__":
    print("Rust-style If-Else Evaluator ; ex : let mut x = 5 ; let y = 10 ; if x > y {x=100;} else {x =10;}")
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
            print("Parsed successfully")
        except Exception as e:
            print("Error:", e)
