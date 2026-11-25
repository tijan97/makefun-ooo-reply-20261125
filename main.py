"""Write the funniest one-line out-of-office reply to /output/entry.txt.

The entry must be a single line of UTF-8 text, 1-160 characters, not only
whitespace. It is judged pairwise by an AI comedy judge against other
one-line out-of-office replies, so the laugh has to land on the first read
and still sound like a message a real person would switch on before going
away.
"""

import os

# The entry line: a fresh turn on the auto-reply itself — no beach, no
# inbox pile-up, no "limited access to email" cliche. The "so" makes the
# punchline land on the same breath as the setup.
ENTRY = "I'm away until Monday — my auto-reply has started replying to itself, so neither of us is available."


def main() -> None:
    line = ENTRY.strip()
    if not line:
        raise SystemExit("entry line is empty")
    if line != ENTRY:
        raise SystemExit("entry line has leading or trailing whitespace")
    if "\n" in line or "\r" in line:
        raise SystemExit("entry line must be a single line")
    if len(line) > 160:
        raise SystemExit(f"entry line is {len(line)} chars, over the 160 limit")
    if len(line.encode("utf-8")) > 160:
        raise SystemExit("entry line is over 160 bytes")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
