import os


def create_readme(folder_path):

    # Create the Markdown content
    markdown_content = "# DSA-problem-solving\n"
    markdown_content += "#### An organized step to brushing-up my problem solving skills regularly.\n\n"

    # add leetcode stats ---------------------------------------------------------------------------------------------
    markdown_content += "![Leetcode Stats](https://leetcard.jacoblin.cool/sushanthkumar78)\n\n"

    # Add the details of each file to the Leetcode Markdown table
    markdown_content += "## List of Problems solved on LeetCode (updated automatically):\n\n"
    markdown_content += "| Problem No. | Problem Name | View Question | View My Code |\n"
    markdown_content += "| ----------- | ------------ | ------------- | ------------ |\n"

    # Get the list of files in the Leetcode folder
    files = os.listdir(folder_path[0])

    for file in files:

        problem_num, problem_name, _ = file.split(".")

        q_url = "https://leetcode.com/problems/"+problem_name+"/"
        s_url = os.path.join(folder_path[0], file)

        q_markdown_url = "[Question](" + q_url + ")"
        s_markdown_url = "[Solution](" + s_url + ")"

        # formatting
        problem_name = problem_name.replace("-", " ").title()
        markdown_content += f"| {problem_num} | {problem_name} | {q_markdown_url} | {s_markdown_url} |\n"

    # add codeforces stats ---------------------------------------------------------------------------------------------
    markdown_content += "\n\n![](https://raw.githubusercontent.com/sushantjha78/cf-stats/main/output/light_card.svg#gh-dark-mode-only)\n\n"

    # Add the details of each file to the Codeforces Markdown table
    markdown_content += "\n\n## List of Problems solved on Codeforces (updated automatically):\n\n"
    markdown_content += "| Problem No. | View Question | View My Code |\n"
    markdown_content += "| ----------- | ------------- | ------------ |\n"

    # Get the list of files in the Codeforces folder
    files = os.listdir(folder_path[1])

    for file in files:
        if file == "input.txt" or file == "template.py":
            continue
        problem_name, _ = file.split(".")
        problem_num = problem_name[:-1]
        problem_subtype = problem_name[-1]

        q_url = "https://codeforces.com/contest/" + \
            problem_num + "/problem/" + problem_subtype
        s_url = os.path.join(folder_path[1], file)

        q_markdown_url = "[Question](" + q_url + ")"
        s_markdown_url = "[Solution](" + s_url + ")"

        # formatting
        markdown_content += f"| {problem_num} | {q_markdown_url} | {s_markdown_url} |\n"

    # Write the Markdown content to the README.md file
    with open("README.md", "w") as file:
        file.write(markdown_content)


if __name__ == "__main__":
    folder_path = ["./Leetcode", "./Codeforces"]
    create_readme(folder_path)
