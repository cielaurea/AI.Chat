from domain.tools import TOOL_CATALOG, ToolDefinition
from domain.ports import ToolRegistryPort


class ToolRegistry(ToolRegistryPort):
    """
    Implémentation concrète du catalogue des outils.

    Cette classe appartient à l'infrastructure :
    elle fournit à l'application l'accès au catalogue
    défini dans le domaine.

    L'application utilisera uniquement ToolRegistryPort
    et ne connaîtra pas directement cette classe.
    """

    def get_tools(self) -> list[ToolDefinition]:
        """
        Retourne la liste des outils disponibles.

        Le catalogue réel est défini dans domain/tools.py.
        Cette classe joue donc le rôle d'adaptateur entre
        ce catalogue et le port attendu par l'application.
        """

        # On retourne le catalogue officiel des outils.
        # Le modèle pourra ensuite utiliser ces informations
        # lors de l'étape « Décider ».
        return TOOL_CATALOG