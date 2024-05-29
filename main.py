import itertools

def replace_characters(base_string, replacements):
    variations = [base_string]
    for original, replacement in replacements.items():
        new_variations = []
        for variation in variations:
            new_variations.extend(variation.replace(original, replacement, 1) for _ in range(variation.count(original)))
        variations.extend(new_variations)
    return set(variations)

def generate_variations(password, max_variations=100000, duplicate=False):
    replacements = {
        'a': '@', 'A': '@',
        'e': '3', 'E': '3',
        'i': '1', 'I': '1',
        'o': '0', 'O': '0',
        's': '$', 'S': '$'
    }
    
    # Step 1: Replace characters
    char_replaced_variations = replace_characters(password, replacements)

    # Step 2: Toggle case
    case_toggled_variations = set()
    for variation in char_replaced_variations:
        variations = map(''.join, itertools.product(*((char.lower(), char.upper()) for char in variation)))
        case_toggled_variations.update(variations)
        if len(case_toggled_variations) > max_variations:
            break

    # Step 3: Replace spaces with special characters
    special_char_replacements = {' ': ['_', '-']}
    special_char_variations = set()
    for variation in case_toggled_variations:
        variations = [variation]
        for original, replacements in special_char_replacements.items():
            new_variations = []
            for replacement in replacements:
                new_variations.extend(variation.replace(original, replacement, 1) for _ in range(variation.count(original)))
            variations.extend(new_variations)
        special_char_variations.update(variations)
        if len(special_char_variations) > max_variations:
            break
    
    # Step 4: Add special characters at the end
    special_characters = ['!', '@', '#', '$', '%', '&', '*']
    final_variations = set()
    for variation in special_char_variations:
        for special_char in special_characters:
            final_variations.add(variation + special_char)
            if len(final_variations) > max_variations:
                break
        if len(final_variations) > max_variations:
            break

    # Step 5: Add duplicate option
    if duplicate:
        duplicated_variations = set()
        for variation in final_variations:
            duplicated_variations.add(variation + variation)
        final_variations.update(duplicated_variations)
        if len(final_variations) > max_variations:
            final_variations = set(list(final_variations)[:max_variations])

    return list(final_variations)[:max_variations]

def main():
    potential_passwords = ["example password", "test123", "mypassword"]
    all_variations = []
    duplicate_option = True  # Set to False if you don't want the duplicate feature
    for password in potential_passwords:
        variations = generate_variations(password, duplicate=duplicate_option)
        all_variations.extend(variations)
    
    print(f"Generated {len(all_variations)} variations.")
    # Optional: Save to a file
    with open("password_variations.txt", "w") as f:
        for variation in all_variations:
            f.write(variation + "\n")

if __name__ == "__main__":
    main()
