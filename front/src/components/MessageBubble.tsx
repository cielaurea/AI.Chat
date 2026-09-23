import type { Message } from "../types/chat";

/**
 * Propriétés nécessaires pour afficher une bulle de message.
 *
 * Le composant reçoit un seul message et se charge uniquement
 * de son affichage.
 */
interface MessageBubbleProps {
  message: Message;
}

/**
 * Affiche un message individuel de la conversation.
 *
 * Ce composant ne gère ni l'envoi du message ni l'appel à l'API.
 * Il reçoit simplement les données préparées par useChat.
 */
export function MessageBubble({ message }: MessageBubbleProps) {
  // Détermine si le message appartient à l'utilisateur
  // afin de pouvoir lui appliquer une présentation différente.
  const isUserMessage = message.role === "user";

  return (
    <div
      className={`message-bubble ${
        isUserMessage ? "message-bubble-user" : "message-bubble-assistant"
      }`}
    >
      {/* Affiche uniquement le texte du message.
          Les données structurées seront affichées plus tard
          par le composant DataTable. */}
      <p>{message.contenu}</p>
    </div>
  );
}