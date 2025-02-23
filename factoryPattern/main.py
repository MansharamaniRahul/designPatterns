from factoryPattern.EnglishFactory import EnglishFactory
from factoryPattern.FrenchFactory import FrenchFactory
from factoryPattern.SpanishFactory import SpanishFactory


def main():
    # Create Factory instances for different languages
    french_factory = FrenchFactory()
    english_factory = EnglishFactory()
    spanish_factory = SpanishFactory()

    message = ["car", "bike", "cycle"]

    french_localizer = french_factory.get_localizer()
    english_localizer = english_factory.get_localizer()
    spanish_localizer = spanish_factory.get_localizer()

    for msg in message:
        # Translate and print the messages
        print(f"Message: {msg}")
        print(f"French: {french_localizer.transform(msg)}")
        print(f"English: {english_localizer.transform(msg)}")
        print(f"Spanish: {spanish_localizer.transform(msg)}")
        print("-" * 30)


if __name__ == "__main__":
    main()  # Run the main function