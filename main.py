from src.eda import load_data, create_eda
from src.preprocessing import transform_to_numeric


def main_train(sv: bool):
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
    if sv == True:
        create_eda(df=df)

    print(1)


if __name__ == "__main__":
    main_train(sv=False)
