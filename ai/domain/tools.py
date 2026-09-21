from enum import Enum


class ToolName(str, Enum):
    LISTER_CLIENTS = "lister_clients"
    LISTER_ARTICLES = "lister_articles"
    