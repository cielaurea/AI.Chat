import react from "@vitejs/plugin-react";
import { defineConfig } from "vite";

// Configuration de Vite pour l'application React.
export default defineConfig({
  plugins: [react()],

  // Le frontend utilise /api pour communiquer avec le service IA.
  // Vite redirige ces requêtes vers FastAPI pendant le développement.
  server: {
    proxy: {
      "/api": {
        target: "http://127.0.0.1:8000",
        changeOrigin: true,

        // Transforme /api/chat en /chat avant d'envoyer
        // la requête au service FastAPI.
        rewrite: (path) => path.replace(/^\/api/, ""),
      },
    },
  },
});