from typing import Callable, List, Any

class LabelingFunctionLib:
    def __init__(self) -> None:
        """Initialize an empty labeling function library."""
        self.label_functions = {}

    def register(self, name: str, func: Callable[[Any], Any]) -> None:
        """
        Register a labeling function with a given name.

        Args:
            name (str): The name of the labeling function.
            func (Callable[[Any], Any]): The labeling function to be registered.

        Raises:
            TypeError: If the provided argument is not a function.
            ValueError: If a label function with the same name has already been registered.
        """
        if not callable(func):
            raise TypeError("The provided argument is not a function.")
        elif name in self.label_functions:
            raise ValueError(f"A label function named '{name}' has already been registered.")
        else:
            self.label_functions[name] = func

    def get(self, name: str) -> Callable[[Any], Any]:
        """
        Retrieve a label function by name.

        Args:
            name (str): The name of the label function to retrieve.

        Returns:
            Callable[[Any], Any]: The label function.

        Raises:
            LookupError: If the label function with the given name does not exist.
        """
        try:
            return self.label_functions[name]
        except KeyError as e:
            raise LookupError(f"No such label function: {e}") from e
    
    def get_all(self) -> List[Callable[[Any], Any]]:
        """
        Returns a list of all labeling functions.

        Returns:
            List[Callable[[Any], Any]]: A list of all labeling functions.
        """
        return list(self.label_functions.values())
    
    def unregister(self, name: str) -> None:
        """
        Unregisters a labeling function by removing it from the label_functions dictionary.

        Args:
            name (str): The name of the labeling function to unregister.

        Returns:
            None
        """
        del self.label_functions[name]
    
    def clear(self) -> None:
        """Remove all label functions from the library."""
        self.label_functions = {}