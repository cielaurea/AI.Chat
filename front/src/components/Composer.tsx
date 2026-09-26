import { useState, type FormEvent } from "react";

/* Propriétés nécessaires pour le composant Composer. */
interface ComposerProps {
  onSend: (message: string) => void;
  isLoading: boolean;
}

/* Permet à l'utilisateur de saisir et d'envoyer une question. */
export function Composer({ onSend, isLoading }: ComposerProps) {
  /* Contient le texte actuellement saisi par l'utilisateur. */
  const [message, setMessage] = useState("");

  /* Gère l'envoi du formulaire. */
  function handleSubmit(event: FormEvent<HTMLFormElement>) {
    /* Empêche le rechargement de la page lors de l'envoi. */
    event.preventDefault();

    /* Supprime les espaces inutiles avant l'envoi. */
    const trimmedMessage = message.trim();

    if (!trimmedMessage || isLoading) {
      return;
    }

    /* Transmet le message au composant parent. */
    onSend(trimmedMessage);

    /* Vide la zone de saisie après l'envoi. */
    setMessage("");
  }

  return (
    <form className="composer" onSubmit={handleSubmit}>
      {/* Zone dans laquelle l'utilisateur saisit sa question. */}
      <input
        type="text"
        value={message}
        onChange={(event) => setMessage(event.target.value)}
        placeholder="Posez votre question..."
        disabled={isLoading}
        aria-label="Question"
      />

      {/* Déclenche handleSubmit lors du clic. */}
      <button
        type="submit"
        disabled={isLoading || !message.trim()}
      >
        {isLoading ? "Envoi..." : "Envoyer"}
      </button>
    </form>
  );
}