# Assistant-AI-

Application de chat avec **React + TypeScript** et un service **FastAPI** utilisant un modèle IA via **Ollama Cloud**.

L'assistant permet de consulter les clients et les articles à partir des données de DummyJSON, avec une réponse dédiée pour les demandes hors périmètre.

## Structure

Le projet est composé de deux services indépendants :

text
Assistant-AI-/
├── ai/          # Backend FastAPI
├── front/       # Frontend React + TypeScript
├── .env.example
└── Makefile

Le backend suit une organisation inspirée de la **Clean Architecture**, avec séparation entre le domaine, l'application, l'API et les infrastructures externes.

## Choix techniques

* React + TypeScript pour l'interface de chat.
* FastAPI pour le service IA.
* Ollama Cloud avec le modèle `gemma4`.
* DummyJSON comme source de données.
* Clean Architecture avec ports et adaptateurs pour séparer la logique métier des services externes.
* Docker pour isoler le frontend et le backend dans deux conteneurs distincts.
* Makefile pour simplifier les commandes de lancement et de test.

## Prérequis

* Docker Desktop
* Une clé API Ollama Cloud

Aucune installation de Python ou Node.js n'est nécessaire pour lancer le projet avec Docker.

## Configuration

Copier .env.example vers .env :

bash
cp .env.example .env

Puis renseigner les informations Ollama :

env
OLLAMA_BASE_URL=
OLLAMA_API_KEY=
OLLAMA_MODEL=gemma4
VITE_API_URL=http://host.docker.internal:8000

La clé API est volontairement absente du dépôt.

## Lancement

### Backend

bash
make ia-dev

Documentation Swagger : http://localhost:8000/docs

### Frontend

bash
make front-dev

Interface : http://localhost:5173

Les deux services peuvent être démarrés indépendamment et dans n'importe quel ordre.

## Commandes disponibles

text
make ia-dev       # démarre le backend
make front-dev    # démarre le frontend
make ia-down      # arrête le backend
make front-down   # arrête le frontend
make ia-logs      # affiche les logs du backend
make front-logs   # affiche les logs du frontend
make ia-test      # lance les tests backend

## API

### `POST /chat`

Reçoit une question utilisateur et retourne une réponse structurée :

json
{
"reponse": "Voici les 10 premiers clients.",
"outil": "lister_clients",
"donnees": [
{
"id": 1,
"nom": "...",
"email": "...",
"societe": "...",
"ville": "..."
}
]
}

outil peut être lister_clients, lister_articles ou null.

Pour une demande hors périmètre, outil vaut null et donnees reste vide.

### `GET /health`

Retourne :

json
{
"status": "ok"
}

## Tests

Les tests couvrent les demandes de clients, d'articles et les demandes hors périmètre.

bash
make ia-test

Résultat attendu :

text
3 passed

## Fonctionnalités non implémentées

Certaines fonctionnalités proposées comme bonus n'ont pas été implémentées afin de conserver un périmètre limité aux fonctionnalités demandées :

* streaming de la réponse IA ;
* mémoire de conversation sur plusieurs tours ;
* recherche filtrée de clients ou d'articles ;
* tests côté frontend ;
* test automatique de la règle de dépendance entre les couches ;
* intégration continue (CI).

Le **mode sombre**, également proposé comme bonus, a en revanche été implémenté.

## Utilisation de l'IA

Une assistance par IA a été utilisée pour le polissage de la documentation et l'accompagnement technique.
