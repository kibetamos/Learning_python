def generate_html(name, description):
    html_content = f"""
<html>
<head>
</head>
<body>
    <center>
        <h1>{name}</h1>
    </center>
    <hr />
    {description}
    <hr />
</body>
</html>
"""

    with open("personal_web_page.html", "w") as file:
        file.write(html_content)

if __name__ == "__main__":
    # Get user input
    name = input("Enter your name: ")
    description = input("Describe yourself: ")

    # Generate HTML file
    generate_html(name, description)

    print("HTML file 'personal_web_page.html' has been generated.")
