import { useEffect, useState } from "react";

import type { Message } from "../types/chat";
import { Composer } from "./Composer";
import { MessageList } from "./MessageList";

/**
 * Propriétés nécessaires pour afficher la fenêtre de conversation.
 */
interface ChatWindowProps {
  messages: Message[];
  isLoading: boolean;
  onSend: (message: string) => void;
}

/**
 * Assemble les différents composants de la conversation.
 *
 * ChatWindow ne gère pas l'appel à l'API.
 * Il reçoit les données et les actions depuis le hook useChat.
 *
 * Il gère également le choix entre le thème clair
 * et le thème sombre de toute l'application.
 */
export function ChatWindow({
  messages,
  isLoading,
  onSend,
}: ChatWindowProps) {
  // Conserve le thème actuellement choisi par l'utilisateur.
  const [isDarkMode, setIsDarkMode] = useState(false);

  /**
   * Applique le thème choisi au document entier.
   *
   * La classe est ajoutée au <body> afin que le fond
   * de toute la page puisse changer, et pas uniquement
   * celui de la fenêtre de conversation.
   */
  useEffect(() => {
    document.body.classList.toggle("dark-page", isDarkMode);

    // Nettoie la classe lorsque le composant est démonté.
    return () => {
      document.body.classList.remove("dark-page");
    };
  }, [isDarkMode]);

  return (
    <main className={`chat-window ${isDarkMode ? "dark-mode" : "light-mode"}`}>
      {/* En-tête contenant le titre, le sous-titre et le bouton de thème. */}
      <header className="chat-header">
        <div>
          <h1>Assistant Dataven</h1>
          <p>Clients et articles</p>
        </div>

        {/* Permet de passer entre le thème clair et le thème sombre. */}
        <button
          type="button"
          className="theme-toggle"
          onClick={() => setIsDarkMode((currentMode) => !currentMode)}
          aria-label={
            isDarkMode
              ? "Activer le mode clair"
              : "Activer le mode sombre"
          }
        >
          {isDarkMode ? "☀️ Clair" : "🌙 Sombre"}
        </button>
      </header>

      {/* Zone principale contenant toute la conversation. */}
      <section className="chat-content" aria-live="polite">
        {/* MessageList affiche maintenant chaque tableau
            directement sous la réponse qui lui correspond. */}
        <MessageList messages={messages} />

        {/* Indicateur visible pendant l'attente de la réponse du service IA. */}
        {isLoading && (
          <div className="loading-indicator" role="status">
            L'assistant réfléchit...
          </div>
        )}
      </section>

      {/* Zone de saisie permettant d'envoyer une nouvelle question. */}
      <Composer onSend={onSend} isLoading={isLoading} />
    </main>
  );
}