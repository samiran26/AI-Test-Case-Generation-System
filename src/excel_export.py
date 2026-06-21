import pandas as pd


def export_to_excel(content):

    df = pd.DataFrame({

        "Generated_Test_Cases": [content]

    })

    output_path = "output/test_cases.xlsx"

    df.to_excel(

        output_path,

        index=False

    )

    print(

        f"Excel file created: {output_path}"

    )