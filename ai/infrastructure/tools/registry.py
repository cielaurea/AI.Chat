from domain.tools import TOOL_CATALOG, ToolDefinition
from domain.ports import ToolRegistryPort


class ToolRegistry(ToolRegistryPort):
    """
    Donne accès au catalogue des outils.
    """

    def get_tools(self) -> list[ToolDefinition]:
        """
        Retourne la liste des outils disponibles.
        """
        return TOOL_CATALOG