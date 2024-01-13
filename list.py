
import itertools
import os

def generate_domain_names(length):
    alphabet = 'abcdefghijklmnopqrstuvwxyz0123456789'
    permutations = [''.join(p) for p in itertools.product(alphabet, repeat=length)]
    return [name + ".rs" for name in permutations]

def save_to_file(domain_names, length):
    directory = "domains"
    if not os.path.exists(directory):
        os.makedirs(directory)

    filename = f"{directory}/{length}.txt"
    with open(filename, 'w') as file:
        for domain in domain_names:
            file.write(domain + '\n')

def main():
    lengths = [2, 3, 4, 5]

    for length in lengths:
        domain_names = generate_domain_names(length)
        save_to_file(domain_names, length)
        print(f"Generated and saved {len(domain_names)} .rs domain names for {length}-character names to {length}.txt.")

if __name__ == "__main__":
    main()
