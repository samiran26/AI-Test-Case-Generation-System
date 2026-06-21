from src.retrieval import retrieve_context

from src.generator import generate_test_cases

from src.excel_export import export_to_excel


def main():

    query = input(

        "Enter requirement/query: "

    )

    context = retrieve_context(

        query

    )

    print(

        "\nRetrieved Context:\n"

    )

    print(

        context

    )

    print(

        "\nGenerating Test Cases...\n"

    )

    output = generate_test_cases(

        context

    )

    print(

        output

    )

    export_to_excel(

        output

    )


if __name__ == "__main__":

    main()