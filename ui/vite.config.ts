import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import tailwindcss from '@tailwindcss/vite'

const previewAllowedHostsEnv = process.env.VITE_PREVIEW_ALLOWED_HOSTS
const previewAllowedHosts =
  !previewAllowedHostsEnv || previewAllowedHostsEnv === '*'
    ? true
    : previewAllowedHostsEnv
        .split(',')
        .map((host) => host.trim())
        .filter(Boolean)

// https://vitejs.dev/config/
export default defineConfig({
  base: process.env.VITE_BASE_PATH || '/',
  plugins: [react(), tailwindcss()],
  preview: {
    allowedHosts: previewAllowedHosts,
  },
})
