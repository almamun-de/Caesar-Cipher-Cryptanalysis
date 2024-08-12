from collections import Counter

def frequency_analysis(ciphertext):
    counter = Counter(ciphertext)
    total = sum(counter.values())
    for char, count in counter.items():
        if char.isalpha():
            print(f"{char}: {count / total:.2%}")

# Example usage
frequency_analysis(ciphertext)
