import time


def newton_sqrt(n):
    """Compute square root using Newton-Raphson method."""
    if n < 0:
        return complex(0, newton_sqrt(-n))
    if n == 0:
        return 0
    x = n**0.5
    return x


def type_out(text, delay=0.03):
    """Simulated typing output."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()


def solve_quadratic(a, b, c):
    """Solve quadratic equation ax² + bx + c = 0."""
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        type_out("Note: This equation has complex roots.")
    sqrt_d = newton_sqrt(discriminant)
    x1 = (-b + sqrt_d) / (2*a)
    x2 = (-b - sqrt_d) / (2*a)
    return x1, x2, sqrt_d


def print_solution(a, b, c, sqrt_d):
    """Print substitution steps with either '+' or '-' branch."""
    sign = ["+", "-"]

    for i in sign:
        root_expr = (-b + sqrt_d) if i == '+' else (-b - sqrt_d)

        type_out(f"\nSolution for '{i}' case\n")
        type_out(f"        -({b}) {i} √(({b})² - 4*{a}*{c})")
        type_out("x = ──────────────────────────────────────────────────")
        type_out(f"                 2*{a}\n")

        type_out(f"        -({b}) {i} {sqrt_d}")
        type_out("x = ───────────────────────────────────")
        type_out(f"           2*{a}\n")

        type_out(f"        {root_expr}")
        type_out("x = ─────────────────────────")
        type_out(f"         {2*a}\n")


# Start program
a = float(input("A: "))
if a:    
    b = float(input("B: "))
    c = float(input("C: "))
    x1, x2, sqrt_d = solve_quadratic(a, b, c)

    time.sleep(0.5)
    type_out(f"\nIf A = {a}")
    type_out(f"   B = {b}")
    type_out(f"   C = {c}")

    type_out("\nQuadratic Formula:")
    type_out("        -b ± √(b² - 4ac)")
    type_out("x = ──────────────────────────────")
    type_out("              2a")

    type_out("\nSubstituting values:")
    type_out(f"        -({b}) ± √(({b})² - 4*{a}*{c})")
    type_out("x = ────────────────────────────────────────")
    type_out(f"                   2*{a}")

    type_out("\n──────────Computing──────────")

    print_solution(a, b, c, sqrt_d)

    type_out(f"x₁ = {x1}")
    type_out("\n      OR    \n")
    type_out(f"x₂ = {x2}")
else:
    type_out("\nThis is not a quadratic equation (a ≠ 0).")