import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import { viteStaticCopy } from "vite-plugin-static-copy";
import path from "path";

// https://vitejs.dev/config/
export default defineConfig({
  base: "/kanji-recognizer",
  plugins: [
    react(),
    viteStaticCopy({
      targets: [
        {
          src: "node_modules/onnxruntime-web/dist/*.wasm",
          dest: ".",
        },
      ],
    }),
  ],
  resolve: {
    alias: [
      {
        find: "@components",
        replacement: path.resolve(__dirname, "src/components"),
      },
      {
        find: "@context",
        replacement: path.resolve(__dirname, "src/context"),
      },
      { find: "@pages", replacement: path.resolve(__dirname, "src/pages") },
      { find: "@utils", replacement: path.resolve(__dirname, "src/utils") },
      {
        find: "@interfaces",
        replacement: path.resolve(__dirname, "src/interfaces"),
      },
    ],
  },
});
