from src.eda import load_data, create_eda
from src.preprocessing import transform_to_numeric
import argparse


def parse_args():
    parser = argparse.ArgumentParser(
        prog="fraud_detection",
        description="Detect fraud",
        epilog="",
    )
    parser.add_argument("-sv", "--sweetviz", default=False, type=bool)
    return parser.parse_args()


def main_train(arguments: dict):
    """
    The main function is the entry point of the program.
    It calls all other functions in order to accomplish its task.

    :return: None
    :doc-author: Ricardo Moya
    """
    df = load_data()

    # First preprocessing
    df = df.pipe(transform_to_numeric)

    # Create EDA
    if arguments["sv"] == True:
        create_eda(df=df)

    print(1)


if __name__ == "__main__":
    arguments = {}
    parser = parse_args()
    arguments["sv"] = parser.sweetviz
    main_train(arguments=arguments)
