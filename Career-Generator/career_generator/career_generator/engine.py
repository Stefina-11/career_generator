# engine.py

class Pipeline:
    """
    Base pipeline class. Subclass this and implement the `run()` method
    to create custom logic.
    """
    def run(self, inputs):
        raise NotImplementedError("Subclasses must implement the run method.")

class ConversationEngine:
    """
    Engine that manages pipelines and routes inputs to the correct one.
    """
    def __init__(self, pipelines: dict):
        self.pipelines = pipelines

    def run(self, pipeline_name: str, inputs: dict):
        """
        Executes the given pipeline with the provided inputs.
        """
        if pipeline_name not in self.pipelines:
            raise ValueError(f"No pipeline found with name: {pipeline_name}")
        return self.pipelines[pipeline_name].run(inputs)
