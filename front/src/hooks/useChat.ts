import { useState } from "react";

import { sendMessage } from "../api/chatClient";
import type { Message } from "../types/chat";

// Gère l'état de la conversation et les appels au service IA.
export function useChat() {
  // Contient tous les messages affichés dans la conversation.
  const [messages, setMessages] = useState<Message[]>([]);

  // Indique si une requête vers le service IA est en cours.
  const [isLoading, setIsLoading] = useState(false);

  /**
   * Envoie une question au service IA.
   */
  async function sendUserMessage(message: string): Promise<void> {
    // Évite d'envoyer un message vide ou composé uniquement d'espaces.
    const trimmedMessage = message.trim();

    if (!trimmedMessage) {
      return;
    }

    // Ajoute la question de l'utilisateur à la conversation.
    setMessages((currentMessages) => [
      ...currentMessages,
      {
        role: "user",
        contenu: trimmedMessage,
      },
    ]);

    // Active l'indicateur de chargement pendant l'appel HTTP.
    setIsLoading(true);

    try {
      // Envoie la question au service IA.
      const response = await sendMessage(trimmedMessage);

      // Ajoute la réponse de l'assistant et les données structurées.
      setMessages((currentMessages) => [
        ...currentMessages,
        {
          role: "assistant",
          contenu: response.reponse,
          reponse: response,
        },
      ]);
    } catch {
      // Affiche un message lisible en cas d'erreur.
      setMessages((currentMessages) => [
        ...currentMessages,
        {
          role: "assistant",
          contenu:
            "Désolé, le service IA est temporairement indisponible.",
        },
      ]);
    } finally {
      // Arrête le chargement, que la requête réussisse ou échoue.
      setIsLoading(false);
    }
  }

  // Retourne les données et l'action nécessaires à l'interface.
  return {
    messages,
    isLoading,
    sendUserMessage,
  };
}