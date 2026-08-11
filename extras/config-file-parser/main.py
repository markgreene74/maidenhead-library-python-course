# imports
from helpers import parse_config, read_config_file

# global variables
FILENAME = "data/my-config"


def main():
    raw_config = read_config_file(FILENAME)
    config = parse_config(raw_config)
    print(config)


if __name__ == "__main__":  # pragma: nocover
    main()
