import react from "@vitejs/plugin-react";
import { defineConfig } from "vite";

//configuration de Vite 
export default defineConfig(() => {
  const apiUrl = process.env.VITE_API_URL;

  if (!apiUrl) {
    throw new Error("VITE_API_URL est requis.");
  }

  return {
    plugins: [react()],

    server: {
      watch: {
        // Permet à Vite de détecter les modifications dans Docker
        usePolling: true,
      },

      proxy: {
        "/api": {
          target: apiUrl,
          changeOrigin: true,

          // /api/chat devient /chat côté FastAPI
          rewrite: (path) => path.replace(/^\/api/, ""),
        },
      },
    },
  };
});