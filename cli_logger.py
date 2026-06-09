import argparse

from generate_log import generate_log


def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Generate timestamped log files'
    )
    parser.add_argument(
        '--logs',
        nargs='+',
        help='Log entries to write to file',
        default=["User logged in", "User updated profile", "Report exported"]
    )
    return parser.parse_args()


def main():
    args = parse_arguments()
    filename = generate_log(args.logs)
    print(f"\n✓ Log file created: {filename}")
    print(f"✓ Number of entries: {len(args.logs)}")


if __name__ == "__main__":
    main()
