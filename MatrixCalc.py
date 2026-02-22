def get_matrix(name):
    print(f"\nMatrix {name}:")
    r, c = int(input("  rows: ")), int(input("  cols: "))
    m = []
    for i in range(r):
        while True:
            row = list(map(float, input(f"  row {i+1}: ").split()))
            if len(row) == c:
                m.append(row)
                break
            print(f"  ! Expected {c} values, got {len(row)}. Try again.")
    return m

def show(m, title="Result"):
    print(f"\n{title}:")
    for row in m:
        print("  ", row)

def same_shape(a, b, op):
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        print(f"\n! {op} requires same shape. A is {len(a)}x{len(a[0])}, B is {len(b)}x{len(b[0])}.")
        return False
    return True

def matsum(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]

def matsub(a, b):
    return [[a[i][j] - b[i][j] for j in range(len(a[0]))] for i in range(len(a))]

def matmul(a, b):
    if len(a[0]) != len(b):
        print(f"\n! Multiplication requires cols(A) == rows(B). Got {len(a[0])} and {len(b)}.")
        return None
    rows, cols, inner = len(a), len(b[0]), len(b)
    return [[sum(a[i][k] * b[k][j] for k in range(inner)) for j in range(cols)] for i in range(rows)]

def scalarsum(k, a):
    return [[a[i][j] + k for j in range(len(a[0]))] for i in range(len(a))]

def scalarsub(k, a):
    return [[a[i][j] - k for j in range(len(a[0]))] for i in range(len(a))]

def matnorm(a):
    rows, cols = len(a), len(a[0])
    result = [row[:] for row in a]
    for j in range(cols):
        col = [a[i][j] for i in range(rows)]
        mn, mx = min(col), max(col)
        span = mx - mn or 1
        for i in range(rows):
            result[i][j] = round((a[i][j] - mn) / span, 4)
    return result

print("\n=== Matrix Calculator ===")
while True:
    print("""
1. Add matrices       (A + B)
2. Subtract matrices  (A - B)
3. Multiply matrices  (A x B)
4. Scalar addition    (A + k)
5. Scalar subtraction (A - k)
6. Normalize matrix
0. Exit""")
    choice = input("\nChoice: ").strip()

    if choice == "0":
        print("Bye!")
        break
    elif choice in ("1", "2", "3"):
        A = get_matrix("A")
        B = get_matrix("B")
        if choice == "1":
            if same_shape(A, B, "Addition"):   show(matsum(A, B), "A + B")
        elif choice == "2":
            if same_shape(A, B, "Subtraction"): show(matsub(A, B), "A - B")
        elif choice == "3":
            result = matmul(A, B)
            if result: show(result, "A x B")
    elif choice in ("4", "5"):
        A = get_matrix("A")
        k = float(input("  scalar k: "))
        if   choice == "4": show(scalarsum(k, A), f"A + {k}")
        elif choice == "5": show(scalarsub(k, A), f"A - {k}")
    elif choice == "6":
        A = get_matrix("A")
        show(matnorm(A), "Normalized (min-max)")
    else:
        print("! Invalid choice.")