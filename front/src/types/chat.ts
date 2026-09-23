/**
 * Représente un client reçu depuis le service IA.
 *
 * Le backend a déjà transformé les données DummyJSON
 * dans cette structure avant de les envoyer au frontend.
 */
export interface Client {
  id: number;
  nom: string;
  email: string;
  societe: string;
  ville: string;
}

/**
 * Représente un article reçu depuis le service IA.
 *
 * Le frontend ne connaît pas la structure interne de DummyJSON :
 * il utilise uniquement les données propres fournies par notre API.
 */
export interface Article {
  id: number;
  titre: string;
  prix: number;
  stock: number;
  categorie: string;
  marque: string;
}

/**
 * Représente la réponse de POST /chat.
 *
 * Le champ "outil" indique l'outil utilisé par le service IA,
 * ou null lorsqu'une demande est hors périmètre.
 *
 * "donnees" contient les données nettoyées retournées par le backend.
 */
export interface ReponseChat {
  reponse: string;
  outil: "lister_clients" | "lister_articles" | null;
  donnees: Client[] | Article[];
}

/**
 * Représente un message affiché dans la conversation.
 *
 * Un message peut venir de l'utilisateur ou de l'assistant.
 * Le champ "reponse" permet d'associer éventuellement
 * les données structurées reçues avec la réponse de l'assistant.
 */
export interface Message {
  role: "user" | "assistant";
  contenu: string;
  reponse?: ReponseChat;
}