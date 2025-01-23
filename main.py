import requests
from llm import LLM

def fetch_repositories(user):
    """Fetch all repositories from the GitHub API considering pagination."""
    url = f"https://api.github.com/users/{user}/repos"
    repositories = []
    page = 1
    per_page = 100  # Max per page
    
    while True:
        response = requests.get(url, params={"page": page, "per_page": per_page})
        if response.status_code == 200:
            data = response.json()
            if not data:  # If the response is empty, we have fetched all repositories
                break
            repositories.extend(data)  # Add the repositories to the list
            page += 1  # Move to the next page
        else:
            print(f"Failed to fetch data. HTTP Status Code: {response.status_code}")
            return []  # Return empty list in case of error
    
    return repositories  # Return all repositories

def format_repositories_for_ai(repos):
    """Format repositories into a prompt for the AI model."""
    formatted_data = "Generate a mermaid graph with the following repositories:\n"
    for repo in repos:
        name = repo.get("name")
        description = repo.get("description", "")
        if description:  # Check if description is not None or empty
            if len(description) > 100:  # Truncate overly long descriptions
                description = description[:97] + "..."
        else:
            description = "No description provided"
        formatted_data += f"- Repository: {name}\n  Description: {description}\n"
    formatted_data += "Please ensure the graph is concise and remove overly long descriptions if necessary. "
    return formatted_data


def main():
    """Main function to run the terminal app."""
    user = input("Enter the GitHub username: ").strip()
    print("\nFetching repositories...")
    repos = fetch_repositories(user)

    if not repos:
        print("No repositories found or an error occurred.")
        return

    print("\nPreparing data for AI...")
    formatted_data = format_repositories_for_ai(repos)

    # Use LLM to generate the mermaid code
    llm = LLM()
    print("\nGenerating mermaid graph code...")
    mermaid_code = llm.model(
        "Your job is to write mermaid code for a GitHub README.md file to create a graph that should describe the account with one glance make subgraphs with inter and intra connections."
        "I will provide you with data about repositories and their descriptions segment repo based on them and connect with eachother if required."
        "i want to display repos connected smartly inter and intra connected between groups and subgroups. no need to display anyhting else only use repo name and its connections to describe graphs"
        "make it beautifull so it looks good and make it complex. use dark theme"
        "make the repo on the vertical line, repos that might belong to same group br creting links. try to keep error free its for github readme.md. "
        "make it error free, use technology to segment and make it complex and curvey."
        "avoid this error Expecting 'SEMI', 'NEWLINE', 'EOF', 'AMP', 'START_LINK', 'LINK', got 'NODE_STRING'.\n\n" + formatted_data
    )

    if mermaid_code:
        print("\nMermaid Graph Code:")
        print(mermaid_code)
    else:
        print("Failed to generate the mermaid graph.")

if __name__ == "__main__":
    main()


