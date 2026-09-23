import { useState, type FormEvent } from "react";

/**
 * Propriétés nécessaires pour le composant Composer.
 *
 * Le composant reçoit uniquement l'action d'envoi
 * et l'état de chargement depuis le composant parent.
 */
interface ComposerProps {
  onSend: (message: string) => void;
  isLoading: boolean;
}

/**
 * Zone de saisie permettant à l'utilisateur d'écrire
 * et d'envoyer une question à l'assistant.
 *
 * Ce composant ne connaît pas l'API et ne gère pas
 * directement les requêtes HTTP.
 */
export function Composer({ onSend, isLoading }: ComposerProps) {
  // Contient le texte actuellement saisi par l'utilisateur.
  const [message, setMessage] = useState("");

  /**
   * Gère l'envoi du formulaire.
   *
   * L'utilisation d'un formulaire permet notamment
   * de déclencher l'envoi avec la touche Entrée.
   */
  function handleSubmit(event: FormEvent<HTMLFormElement>) {
    // Empêche le rechargement de la page provoqué
    // normalement par l'envoi d'un formulaire HTML.
    event.preventDefault();

    // Évite d'envoyer un message vide ou uniquement composé d'espaces.
    const trimmedMessage = message.trim();

    if (!trimmedMessage || isLoading) {
      return;
    }

    // Transmet le message au hook useChat via le composant parent.
    onSend(trimmedMessage);

    // Vide la zone de saisie après l'envoi.
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

      {/* Le bouton utilise le formulaire : cliquer dessus
          déclenche donc également handleSubmit. */}
      <button
        type="submit"
        disabled={isLoading || !message.trim()}
      >
        {isLoading ? "Envoi..." : "Envoyer"}
      </button>
    </form>
  );
}