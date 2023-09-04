def is_balanced(text):
    stack = []
    brackets = {'(': ')', '[': ']', '{': '}'}

    for i, char in enumerate(text):
        if char in brackets.keys():
            stack.append((char, i))  # Store both the bracket and its position.
        elif char in brackets.values():
            if not stack or brackets[stack.pop()[0]] != char:
                return i + 1

    return stack[0][1] + 1 if stack else "Success"


def main():
    text = input()
    mismatch = is_balanced(text)
    print(mismatch)


if __name__ == "__main__":
    main()
