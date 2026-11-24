import os

ENTRY = (
    "He failed the bar exam four times, studying on the night bus home from "
    "the dish pit; he opened the fifth letter standing in that same kitchen, "
    "read it twice, and smiled like it was his — because it was."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
