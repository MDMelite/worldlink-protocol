# Running Automated Tests

This document provides instructions on how to run the automated tests included in the WorldLink Protocol repository.

## Running Python Tests

The Python automated tests use the `unittest` framework, which is part of the standard Python library. To run the Python tests for the "Hello, World!" example, follow these steps:

1.  Ensure you have Python installed on your system.
2.  Navigate to the root directory of the WorldLink Protocol repository in your terminal.
3.  Run the following command:

    ```bash
    python -m unittest automated-testing/examples/hello-world/test_hello_world.py
    ```

    This command will discover and run the tests in the specified file. The output will indicate whether the tests passed or failed.

## Running JavaScript Tests

The JavaScript automated tests for the "Hello, World!" example are written using Jest, a popular JavaScript testing framework. To run these tests, you will need Node.js and npm (or yarn) installed on your system.

1.  Navigate to the root directory of the WorldLink Protocol repository in your terminal.
2.  If you haven't already, initialize a Node.js project by running:

    ```bash
    npm init -y
    ```

    or

    ```bash
    yarn init -y
    ```
3.  Install Jest as a development dependency:

    ```bash
    npm install --save-dev jest
    ```

    or

    ```bash
    yarn add --dev jest
    ```
4.  Open your `package.json` file and add or modify the `scripts` section to include a test command:

    ```json
    "scripts": {
      "test": "jest"
    }
    ```
5.  Now you can run the tests using the following command in your terminal:

    ```bash
    npm test
    ```

    or

    ```bash
    yarn test
    ```

    Jest will find and execute the test files (typically those with a `.test.js` or `.spec.js` extension, or as configured in Jest's settings). The output will show the status of the tests.

**Note:** These instructions are for running the basic automated tests we have created. More comprehensive test suites might have different execution methods or require additional setup. Refer to the documentation of any other testing frameworks used for those specific instructions.