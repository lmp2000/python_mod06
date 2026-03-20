from alchemy.grimoire import validate_ingredients, record_spell

def main() -> None:
    print("=== Circular Curse Breaking ===\n")

    print("Testing ingredient validation:")
    print(f'validate_ingredients("fire air"): {validate_ingredients("fire air")}')
    result = validate_ingredients("dragon scales")
    print(f'validate_ingredients("dragon scales"): {result}')

    print("\nTesting spell recording with validation:")
    result = record_spell("Fireball", "fire air")
    print(f'record_spell("Fireball", "fire air"): {result}')
    result = record_spell("Dark Magic", "shadow")
    print(f'record_spell("Dark Magic", "shadow"): {result}')

    print("\nTesting late import technique:")
    print(f'record_spell("Lightning", "air"): {record_spell("Lightning", "air")}')

    print("\nCircular dependency curse avoided using late imports!")
    print("All spells processed safely!")


if __name__ == '__main__':
    main()
