import { useState } from "react";

import { sendMessage } from "../api/chatClient";
import type { Message } from "../types/chat";

/**
 * Gère l'état et le comportement de la conversation.
 *
 * Ce hook centralise :
 * - la liste des messages ;
 * - l'envoi d'un message au service IA ;
 * - l'état de chargement ;
 * - l'affichage d'une erreur dans la conversation.
 *
 * Les composants graphiques n'ont donc pas besoin
 * de connaître les détails de l'appel HTTP.
 */
export function useChat() {
  // Contient tous les messages affichés dans la conversation.
  const [messages, setMessages] = useState<Message[]>([]);

  // Indique si une requête vers le service IA est en cours.
  const [isLoading, setIsLoading] = useState(false);

  /**
   * Envoie une question au service IA.
   *
   * Le message utilisateur est d'abord ajouté à la conversation.
   * Le service IA est ensuite appelé via sendMessage().
   */
  async function sendUserMessage(message: string): Promise<void> {
    // Évite d'envoyer un message vide ou composé uniquement d'espaces.
    const trimmedMessage = message.trim();

    if (!trimmedMessage) {
      return;
    }

    // Ajoute immédiatement la question de l'utilisateur
    // afin qu'elle apparaisse dans la conversation.
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

      // Ajoute la réponse de l'assistant ainsi que les données structurées.
      setMessages((currentMessages) => [
        ...currentMessages,
        {
          role: "assistant",
          contenu: response.reponse,
          reponse: response,
        },
      ]);
    } catch {
      // En cas de problème réseau ou serveur,
      // on affiche une erreur lisible directement dans la conversation.
      setMessages((currentMessages) => [
        ...currentMessages,
        {
          role: "assistant",
          contenu:
            "Désolé, le service IA est temporairement indisponible.",
        },
      ]);
    } finally {
      // Désactive toujours le chargement, que la requête
      // ait réussi ou échoué.
      setIsLoading(false);
    }
  }

  // Le composant qui utilise ce hook reçoit uniquement
  // les informations et l'action dont il a besoin.
  return {
    messages,
    isLoading,
    sendUserMessage,
  };
}