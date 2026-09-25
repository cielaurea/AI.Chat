import react from "@vitejs/plugin-react";
import { defineConfig } from "vite";

// Configuration de Vite pour l'application React.
export default defineConfig(() => {
  const apiUrl = process.env.VITE_API_URL;

  if (!apiUrl) {
    throw new Error("VITE_API_URL est requis.");
  }

  return {
    plugins: [react()],

    server: {
      watch: {
        // Nécessaire pour détecter les modifications dans Docker.
        usePolling: true,
      },

      proxy: {
        "/api": {
          target: apiUrl,
          changeOrigin: true,

          // /api/chat devient /chat côté FastAPI.
          rewrite: (path) => path.replace(/^\/api/, ""),
        },
      },
    },
  };
});