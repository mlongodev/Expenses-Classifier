# Expense Categorization Procedure

The provided code is a procedure designed to help you categorize your expenses. Here is an overview of how the procedure works:

1. The procedure starts by reading the Excel files containing your bank account transactions or credit card transactions.
2. It combines the data from these different sources into a unified DataFrame, allowing you to analyze all your expenses in one place.
3. For each row (expense) in the DataFrame, the procedure utilizes OpenAI's API to seek assistance in categorizing the expense based on its description.
4. It sends a message to ChatGPT via the API, providing information about the available expense categories and the description of the expense that needs to be categorized.
5. ChatGPT processes the information and responds with a suggested category for the expense.
6. The procedure assigns the suggested category to the corresponding row in the DataFrame.
7. It prints the expense description along with its associated category to provide visibility into the categorization process.
8. To ensure a smooth interaction with the API, the procedure includes a short pause (0.5 seconds) between each expense categorization.
9. Once all expenses have been categorized, the procedure saves the updated DataFrame to an Excel file named 'output.xlsx' in the current directory.

By following the examples of this procedure, you can then easily adjust the Excel file reading functions (`get_creditcard_entry()`, `get_bank_acc_entry()`, `get_revolut_entry()`) to suit your specific file formats and locations. This way, you can seamlessly integrate your own expense data and utilize the expense categorization capabilities provided by ChatGPT and OpenAI's API.
