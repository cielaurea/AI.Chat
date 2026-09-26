import { useEffect, useState } from "react";

import type { Message } from "../types/chat";
import { Composer } from "./Composer";
import { MessageList } from "./MessageList";

/* Propriétés nécessaires pour afficher la fenêtre de conversation. */
interface ChatWindowProps {
  messages: Message[];
  isLoading: boolean;
  onSend: (message: string) => void;
}

/* Assemble les composants de la conversation et gère le thème. */
export function ChatWindow({
  messages,
  isLoading,
  onSend,
}: ChatWindowProps) {
  /* Conserve le thème actuellement choisi par l'utilisateur. */
  const [isDarkMode, setIsDarkMode] = useState(false);

  /* Applique le thème choisi à toute la page. */
  useEffect(() => {
    document.body.classList.toggle("dark-page", isDarkMode);

    /* Supprime la classe lorsque le composant est démonté. */
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

      {/* Zone principale contenant la conversation. */}
      <section className="chat-content" aria-live="polite">
        {/* Affiche les messages et les données associées. */}
        <MessageList messages={messages} />

        {/* Affiche un indicateur pendant l'attente de la réponse. */}
        {isLoading && (
          <div className="loading-indicator" role="status">
            L'assistant réfléchit...
          </div>
        )}
      </section>

      {/* Zone de saisie pour envoyer une nouvelle question. */}
      <Composer onSend={onSend} isLoading={isLoading} />
    </main>
  );
}