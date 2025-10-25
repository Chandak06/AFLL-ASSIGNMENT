from parser import parser

test_inputs = [
    "foo()",
    "bar(1, 2)",
    "nested_call(inner(3), outer(4))",
    "calculate_sum(a, b, c, d)"
]

for code in test_inputs:
    print(f"\nTesting: {code}")
    parser.parse(code)