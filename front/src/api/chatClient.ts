import type { ReponseChat } from "../types/chat";

/* Adresse utilisée pour appeler le service IA via le proxy Vite. */
const CHAT_ENDPOINT = "/api/chat";

/* Envoie une question au service IA et retourne sa réponse. */
export async function sendMessage(message: string): Promise<ReponseChat> {
  /* Envoie la question au endpoint POST /chat du service IA. */
  const response = await fetch(CHAT_ENDPOINT, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      message,
    }),
  });

  /* Signale une erreur si la réponse HTTP n'est pas réussie. */
  if (!response.ok) {
    throw new Error("Le service IA ne répond pas correctement.");
  }

  /* Transforme la réponse JSON en objet correspondant à notre type. */
  const data: ReponseChat = await response.json();

  /* Retourne la réponse structurée au hook useChat. */
  return data;
}