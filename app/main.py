"""Demo application main module."""

import sys
import argparse

def add(a: int, b: int) -> int:
    """Return the sum of *a* and *b*."""
    return a + b

def cli() -> None:
    parser = argparse.ArgumentParser(description="Demo CLI")
    parser.add_argument("a", type=int, help="First integer")
    parser.add_argument("b", type=int, help="Second integer")
    args = parser.parse_args()
    result = add(args.a, args.b)
    print(result)

if __name__ == "__main__":
    cli()
