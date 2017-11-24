from avalon import maya


class CreateExample(maya.Creator):
    """example"""

    name = "exampleDefault"
    label = "Example"
    family = "config.example"

    def process(self):
        pass
