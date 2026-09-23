import "./App.css";

import { ChatWindow } from "./components/ChatWindow";
import { useChat } from "./hooks/useChat";

/**
 * Composant principal de l'application.
 *
 * App reste volontairement très simple :
 * il utilise le hook useChat pour gérer la conversation
 * et transmet les données à la fenêtre de chat.
 *
 * Il n'y a pas de routeur ni de gestionnaire d'état global,
 * conformément au périmètre demandé dans le sujet.
 */
function App() {
  // Récupère l'état de la conversation et l'action permettant
  // d'envoyer un nouveau message au service IA.
  const { messages, isLoading, sendUserMessage } = useChat();

  return (
    <ChatWindow
      messages={messages}
      isLoading={isLoading}
      onSend={sendUserMessage}
    />
  );
}

export default App;