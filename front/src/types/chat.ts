/* Représente un client reçu depuis le service IA. */
export interface Client {
  id: number;
  nom: string;
  email: string;
  societe: string;
  ville: string;
}

/* Représente un article reçu depuis le service IA. */
export interface Article {
  id: number;
  titre: string;
  prix: number;
  stock: number;
  categorie: string;
  marque: string;
}

/* Représente la réponse de POST /chat. */
export interface ReponseChat {
  reponse: string;
  outil: "lister_clients" | "lister_articles" | null;
  donnees: Client[] | Article[];
}

/* Représente un message affiché dans la conversation. */
export interface Message {
  role: "user" | "assistant";
  contenu: string;
  reponse?: ReponseChat;
}