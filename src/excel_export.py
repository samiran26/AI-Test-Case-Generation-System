import pandas as pd


def export_to_csv(test_cases):

    df = pd.DataFrame(test_cases)

    output_path = "output/test_cases.csv"

    df.to_csv(

        output_path,

        index=False

    )

    print(

        f"CSV created: {output_path}"

    )