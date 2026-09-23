import type { Article, Client } from "../types/chat";

/**
 * Propriétés nécessaires pour afficher les données reçues du service IA.
 *
 * Le composant reçoit uniquement les données nettoyées par le backend.
 * Il ne connaît donc pas la structure interne de DummyJSON.
 */
interface DataTableProps {
  data: Client[] | Article[];
}

/**
 * Vérifie si les données correspondent à une liste de clients.
 *
 * Le champ "nom" existe uniquement dans l'interface Client.
 */
function isClientList(data: Client[] | Article[]): data is Client[] {
  return data.length === 0 || "nom" in data[0];
}

/**
 * Affiche les données structurées reçues du service IA.
 *
 * Les clients et les articles sont présentés sous forme de tableau
 * afin d'éviter d'afficher directement le JSON reçu par l'API.
 */
export function DataTable({ data }: DataTableProps) {
  // Une réponse sans données ne nécessite aucun tableau.
  if (data.length === 0) {
    return null;
  }

  // Si les données sont celles des clients, on affiche
  // les colonnes correspondant à l'entité Client.
  if (isClientList(data)) {
    return (
      <div className="data-table-container">
        <table className="data-table">
          <thead>
            <tr>
              <th>ID</th>
              <th>Nom</th>
              <th>Email</th>
              <th>Société</th>
              <th>Ville</th>
            </tr>
          </thead>

          <tbody>
            {data.map((client) => (
              <tr key={client.id}>
                <td>{client.id}</td>
                <td>{client.nom}</td>
                <td>{client.email}</td>
                <td>{client.societe}</td>
                <td>{client.ville}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    );
  }

  // Si les données ne sont pas des clients, elles correspondent
  // aux articles définis dans notre contrat frontend.
  const articles = data as Article[];

  return (
    <div className="data-table-container">
      <table className="data-table">
        <thead>
          <tr>
            <th>ID</th>
            <th>Article</th>
            <th>Prix</th>
            <th>Stock</th>
            <th>Catégorie</th>
            <th>Marque</th>
          </tr>
        </thead>

        <tbody>
          {articles.map((article) => (
            <tr key={article.id}>
              <td>{article.id}</td>
              <td>{article.titre}</td>
              <td>{article.prix} €</td>
              <td>{article.stock}</td>
              <td>{article.categorie}</td>
              <td>{article.marque}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}