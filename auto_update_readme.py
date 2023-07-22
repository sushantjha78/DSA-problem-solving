import os

def create_readme(folder_path):
    # Get the list of files in the folder
    files = os.listdir(folder_path)

    # Create the Markdown content
    markdown_content = "# DSA-problem-solving\n"
    markdown_content += "An organized step to brushing-up my problem solving skills regularly.\n\n"
    markdown_content += "![Leetcode Stats](https://leetcard.jacoblin.cool/sushanthkumar78)\n\n"

    markdown_content += "## List of Problems solved on LeetCode (updated automatically):\n\n"
    markdown_content += "| Problem No. | Problem Name | View Question | View My Code |\n"
    markdown_content += "| ----------- | ------------ | ------------- | ------------ |\n"

    # Add the details of each file to the Markdown table
    for file in files:
        problem_num, problem_name, _ = file.split(".")

        q_url = "https://leetcode.com/problems/"+problem_name+"/"
        s_url = os.path.join(folder_path, file)

        q_markdown_url = "[Question](" + q_url + ")"
        s_markdown_url = "[Solution](" + s_url + ")"

        # formatting
        problem_name = problem_name.replace("-", " ").title()
        markdown_content += f"| {problem_num} | {problem_name} | {q_markdown_url} | {s_markdown_url} |\n"

    # Write the Markdown content to the README.md file
    with open("README.md", "w") as file:
        file.write(markdown_content)

if __name__ == "__main__":
    folder_path = "./Leetcode"
    create_readme(folder_path)
