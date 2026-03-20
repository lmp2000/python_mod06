import alchemy
import alchemy.elements


def direct() -> None:
    print('\n=== Sacred Scroll Mastery ===')

    print('\nTesting direct module access:')
    fire = alchemy.elements.create_fire()
    print(
        f'alchemy.elements.create_fire(): {fire}'
    )
    water = alchemy.elements.create_water()
    print(
        f'alchemy.elements.create_water(): {water}'
    )
    earth = alchemy.elements.create_earth()
    print(
        f'alchemy.elements.create_earth(): {earth}'
    )
    air = alchemy.elements.create_air()
    print(
        f'alchemy.elements.create_air(): {air}'
    )


def package() -> None:
    print(
        '\nTesting package-level access (controlled by __init__.py):'
        )

    fire = alchemy.create_fire()
    print(
        f'alchemy.create_fire(): {fire}'
    )
    water = alchemy.create_water()
    print(
        f'alchemy.create_water(): {water}'
    )

    try:
        earth = alchemy.create_earth()
        print(
        f'alchemy.create_earth(): {earth}'
        )
    except AttributeError:
        print(
            'alchemy.create_earth(): AttributeError - not exposed'
        )


    try:
        air = alchemy.create_air()
        print(
        f'alchemy.create_air(): {air}'
        )
    except AttributeError:
        print(
            'alchemy.create_air(): AttributeError - not exposed'
        )


if __name__ == "__main__":
    direct()
    package()
    print(
        '\nPackage metadata:'
    )
    print(
        f'Version: {alchemy.__version__}'
    )
    print(
        f'Author: {alchemy.__author__}'
    )
