import type { Article, Client } from "../types/chat";

/* Propriétés nécessaires pour afficher les données reçues du service IA. */
interface DataTableProps {
  data: Client[] | Article[];
}

/* Vérifie si les données correspondent à une liste de clients. */
function isClientList(data: Client[] | Article[]): data is Client[] {
  return data.length === 0 || "nom" in data[0];
}

/* Affiche les clients ou les articles sous forme de tableau. */
export function DataTable({ data }: DataTableProps) {
  /* Une réponse sans données ne nécessite aucun tableau. */
  if (data.length === 0) {
    return null;
  }

  /* Si les données sont des clients, affiche les colonnes correspondantes. */
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

  /* Si ce ne sont pas des clients, les données correspondent aux articles. */
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