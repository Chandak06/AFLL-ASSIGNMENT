# main.py
from parser import parser

if __name__ == "__main__":
    print("Welcome to the Match Expression Parser.")
    print("Type 'quit' or 'exit;' to quit.\n")

    while True:
        data = input(">>> ")
        
        if data.strip().lower() in ["quit", "exit;"]:
            print("Exiting...")
            break
            
        if not data.strip():
            continue

        try:
            result = parser.parse(data)
            
            if result is not None:
                print("AST:", result)
                
        except Exception as e:
            print(f"Internal Error:{e}")
