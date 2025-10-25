# main.py
from parser import parser

if __name__ == "__main__":
    print("Welcome to the Simple Function Call Parser.")
    print("Enter a function call (e.g., 'foo(a, 10)') or type 'quit' to exit.\n")

    while True:
        data = input(">>> ")
        
        if data.strip().lower() == "quit":
            print("Exiting...")
            break
            
        if not data.strip():
            continue

        try:
            result = parser.parse(data)
            
            if result is not None:
                print("AST:", result)
                
        except Exception as e:
            print(f"Internal Error: {e}")
