import sys

ENTRY = "My bank texted me 'we're worried about you' — then charged me $5 for the concern. Even my wallet needs therapy now."

MAX_CHARS = 200


def render(text):
    """Return the exact bytes to emit: the entry plus one trailing newline."""
    validated = validate(text)
    output = validated + "\n"
    if output.count("\n") != 1:
        raise ValueError("output must contain exactly one newline, at the end")
    return output


def validate(text):
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over the {MAX_CHARS} limit")
    if not text.strip():
        raise ValueError("entry must not be empty")
    return text


def main():
    try:
        sys.stdout.write(render(ENTRY))
        sys.stdout.flush()
    except BrokenPipeError:
        # Fallback: nothing else may be printed; exit quietly on a closed pipe.
        try:
            sys.stdout.close()
        except Exception:
            pass
        raise SystemExit(0)


if __name__ == "__main__":
    main()
