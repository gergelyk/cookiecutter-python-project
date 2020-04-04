
class HelloWorld:
    """Sample class"""

    def say_hello(self, name: str):
        """
        Sample method

        Arguments:
            name: sample argument
        """
        # docstring format: https://github.com/pawamoy/mkdocstrings#docstrings-format
        print(f"Hello {name}!")


if __name__ == "__main__":
    app = HelloWorld()
    app.say_hello(name='John')
