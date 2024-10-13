# Contributing to the Automated-Irrigation-System-Using-an-MCU Project

I appreciate your interest in contributing to the Automated-Irrigation-System-Using-an-MCU project! This guide outlines the contribution process and provides instructions for :
- Creating or picking open issues
- Setting up the local development environment
- Making changes on a new branch
- Pushing changes to the upstream repository
- Submitting tasks for pull requests
- Adding issue references and details to your pull requests.

## Creating or Picking Open Issues

1. Before starting any work, check the [GitHub Issues](https://github.com/mbvgua/Automated-Irrigation-System-Using-an-MCU/issues) section to find existing open issues related to the project. These issues cover various aspects of the redesign project, such as bug fixes, feature enhancements, and design improvements.

2. If you find an issue that you would like to work on, comment on the issue to express your interest in addressing it. A project maintainer or the owner will assign the issue to you, or provide additional information or guidance if needed.

3. If you can't find an existing issue that matches your desired contribution, feel free to create a new issue. Clearly describe the problem, feature request, or design enhancement you want to tackle. Provide as much information as possible to help others understand the context and requirements of the issue.

## Setting Up the Local Development Environment

To set up your local development environment, follow these steps:


1. Fork the repository

    On the main project repo, click on the fork icon and fork it. This allows you to access a version of the repository in your own account.

1. Clone the repository

   Open your terminal and run the following command:

   ```bash
   $ git clone https://github.com/<your_username>/Automated-Irrigation-System-Using-an-MCU.git
   ```

2. Navigate into the directory

   Change your current directory and move into the main website directory:

   ```bash
   $ cd Automated-Irrigation-System-Using-an-MCU/3.Building-the-Website    
   ```

3. Create a virtual environment and install the neccesary packages

   Run the following command to create a virtual environment:

   ```bash
   $ python -m venv .venv
   ```

   Once created, you need to download all the neccessary packages:

   ```bash
   $ pip install -r requirements.txt
   ```

> This only works on a Linux OS. if using a Windows or Mac, figure out how to activate it [here](https://chatgpt.com)


4. Start the development server

   Now you can navigate to the top level of your repository and start the server:

   ```bash
   $ cd iFarm    
   $ python app.py
   ```


5. Access the website in your browser at `http://localhost:8000`. You can now make changes to the code and see them reflected in real-time on the local development server.

## Making Changes on a New Branch

To work on a new feature or bug fix, follow these steps to create and switch to a new branch:

1. Create a new branch based on the `main` branch:

   ```
   git checkout -b feature/your-feature-name
   ```

   Replace `your-feature-name` with a descriptive name for your feature or bug fix.

2. Make the necessary changes to the codebase using your preferred code editor or IDE.

3. Commit your changes with a meaningful commit message:
   ```
   git commit -m "short and brief commit message" -m"long, detailed and descriptive commit message"
   ```

## Pushing Changes to the Upstream Repository

To push your changes to the upstream repository and make them available for review, follow these steps:

1. Push your changes to your forked repository:

   ```
   git push origin feature/your-feature-name
   ```

2. Open your forked repository on GitHub and navigate to the branch that contains your changes.

3. Click on the "New Pull Request" button to create a new pull request.

4. Provide a descriptive title and detailed description for your pull request. Include any relevant information, such as the problem you solved or the feature you implemented.

5. If your pull request addresses any open issues, reference the issue number in the description using the following format: `Fixes #<issue-number>`. This will automatically link the pull request to the respective issue.

6. Submit the pull request for review.

## Adding Issue References to Your Pull Request

If your pull request addresses any open issues, make sure to reference them in the pull request description using the format mentioned earlier (`Fixes #<issue-number>`). This helps track and link the pull request to the corresponding issue.

Additionally, provide details in your pull request description about the specific problem or feature that you have managed to solve. Explain

the changes you made and how they contribute to the overall project.

## Summary

By following these guidelines, you can effectively contribute to the Automated-Irrigation-System-Using-an-MCU project. Your contributions are highly valued and appreciated. Thank you for your service!