from parser import parser

test_inputs = [
    "match x { one => foo(), _ => bar(42), }",
    "match y { a => b(), b => c(1, 2), }",
    "match z { _ => handle(), }"
]

for code in test_inputs:
    print(f"\nTesting: {code}")
    parser.parse(code)