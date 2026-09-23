import type { ReponseChat } from "../types/chat";

/**
 * Adresse relative utilisée pour appeler le service IA.
 *
 * En développement, Vite pourra rediriger /api vers FastAPI
 * grâce au proxy configuré dans vite.config.ts.
 *
 * Le frontend ne connaît donc pas directement l'adresse
 * de DummyJSON : il communique uniquement avec notre service IA.
 */
const CHAT_ENDPOINT = "/api/chat";

/**
 * Envoie un message utilisateur au service IA.
 *
 * Cette fonction constitue l'unique point d'appel HTTP
 * du frontend vers notre API de conversation.
 *
 * @param message Question saisie par l'utilisateur.
 * @returns La réponse structurée du service IA.
 * @throws Error si le service ne répond pas correctement.
 */
export async function sendMessage(message: string): Promise<ReponseChat> {
  // Envoie la question au endpoint POST /chat du service IA.
  const response = await fetch(CHAT_ENDPOINT, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      message,
    }),
  });

  // Une réponse HTTP non réussie doit être signalée
  // afin que l'interface puisse afficher une erreur lisible.
  if (!response.ok) {
    throw new Error("Le service IA ne répond pas correctement.");
  }

  // Transforme la réponse JSON en objet JavaScript.
  const data: ReponseChat = await response.json();

  // Retourne uniquement les données correspondant
  // au contrat attendu par le frontend.
  return data;
}