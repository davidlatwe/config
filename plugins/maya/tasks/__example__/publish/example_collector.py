import pyblish.api


class CollectExample(pyblish.api.InstancePlugin):
    """Collect something for example valitation

    ```
    instance.data {
            example: my example
    }
    ```

    """

    label = "Collect Example"
    families = ["config.example"]
    order = pyblish.api.CollectorOrder + 0.1
    hosts = ["maya"]

    def process(self, instance):
        instance.data.update(
            {
                "example": self._collect_example(instance)
            }
        )

    @staticmethod
    def _collect_example(instance):
        from maya import cmds
        return cmds.ls("example")
