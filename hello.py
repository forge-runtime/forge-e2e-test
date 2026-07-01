"""Hello module."""


def hello() -> str:
    """Return greeting message."""
    return "Hello World"


def main() -> None:
    """Print greeting."""
    print(hello())


if __name__ == "__main__":
    main()
