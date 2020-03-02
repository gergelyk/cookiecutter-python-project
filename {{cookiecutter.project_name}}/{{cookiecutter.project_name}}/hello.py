
class HelloWorld:
    """Sample class"""

    def say_hello(self, name: str):
        """
        Sample method

        Arguments:
            name: sample argument
        """
        print(f"Hello {name}!")

if __name__ == "__main__":
    app = HelloWorld()
    app.say_hello(name='John')
