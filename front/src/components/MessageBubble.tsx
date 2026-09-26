import type { Message } from "../types/chat";

/* Propriétés nécessaires pour afficher une bulle de message. */
interface MessageBubbleProps {
  message: Message;
}

/* Affiche un message individuel de la conversation. */
export function MessageBubble({ message }: MessageBubbleProps) {
  /* Détermine si le message appartient à l'utilisateur. */
  const isUserMessage = message.role === "user";

  return (
    <div
      className={`message-bubble ${
        isUserMessage ? "message-bubble-user" : "message-bubble-assistant"
      }`}
    >
      {/* Affiche le texte du message. */}
      <p>{message.contenu}</p>
    </div>
  );
}