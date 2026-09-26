import "./App.css";

import { ChatWindow } from "./components/ChatWindow";
import { useChat } from "./hooks/useChat";

// Composant principal : relie la logique du chat à son interface.
function App() {
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