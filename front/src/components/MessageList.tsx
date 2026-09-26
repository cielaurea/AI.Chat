import type { Message } from "../types/chat";
import { DataTable } from "./DataTable";
import { MessageBubble } from "./MessageBubble";

/* Propriétés nécessaires pour afficher la liste des messages. */
interface MessageListProps {
  messages: Message[];
}

/* Affiche les messages dans leur ordre avec les données associées. */
export function MessageList({ messages }: MessageListProps) {
  return (
    <div className="message-list">
      {messages.map((message, index) => (
        <div className="message-group" key={`${message.role}-${index}`}>
          {/* Affiche la bulle du message courant. */}
          <MessageBubble message={message} />

          {/* Affiche le tableau si la réponse contient des données. */}
          {message.role === "assistant" && message.reponse && (
            <DataTable data={message.reponse.donnees} />
          )}
        </div>
      ))}
    </div>
  );
}