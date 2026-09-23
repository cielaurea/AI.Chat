import type { Message } from "../types/chat";
import { DataTable } from "./DataTable";
import { MessageBubble } from "./MessageBubble";

/**
 * Propriétés nécessaires pour afficher la liste des messages.
 */
interface MessageListProps {
  messages: Message[];
}

/**
 * Affiche tous les messages de la conversation dans leur ordre.
 *
 * Lorsqu'une réponse de l'assistant contient des données,
 * le tableau correspondant est affiché immédiatement sous cette réponse.
 *
 * Ainsi, chaque question et sa réponse restent regroupées
 * avec les données qui lui correspondent.
 */
export function MessageList({ messages }: MessageListProps) {
  return (
    <div className="message-list">
      {messages.map((message, index) => (
        <div className="message-group" key={`${message.role}-${index}`}>
          {/* Affiche la bulle du message courant. */}
          <MessageBubble message={message} />

          {/* Affiche le tableau uniquement pour une réponse
              de l'assistant contenant des données. */}
          {message.role === "assistant" && message.reponse && (
            <DataTable data={message.reponse.donnees} />
          )}
        </div>
      ))}
    </div>
  );
}