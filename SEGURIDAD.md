# Seguridad

Sitio estático (un `index.html`). Los datos dinámicos (catálogo, reseñas, comentarios) pasan por [proxy-sia](https://github.com/Saerling/proxy-sia), que es donde viven la base de datos, las claves y los límites.

| # | Punto | Estado |
|---|---|---|
| 1 | Ocultar API keys | ✅ El frontend no tiene claves; solo el ID público de Google Analytics. Sin anuncios. |
| 2 | Secretos fuera de Git | ✅ Historial revisado: sin secretos. |
| 3 | Key pública para DB | ✅ El navegador no toca la DB; habla con proxy-sia. |
| 4 | Row-Level Security | ✅ En Neon (vía proxy-sia). |
| 5 | Encriptar datos sensibles | ✅ Lo sensible se guarda con hash en el backend; aquí solo `localStorage` con progreso del usuario. |
| 6 | Forzar autenticación | N/A — no hay cuentas; la moderación está en el backend con clave. |
| 7 | Restringir acceso a registros | ✅ En backend. |
| 8 | Bloquear manipulación de campos | ✅ El backend ignora campos no permitidos. |
| 9 | Session cookies | N/A — no hay sesiones. |
| 10 | Hashear contraseñas | N/A — no hay contraseñas. |
| 11 | Rate limiting | ✅ En backend. |
| 12 | Protección contra bots | ✅ Honeypot + límites en backend. |
| 13 | Queries parametrizadas | ✅ En backend. |
| 14 | Validar inputs | ✅ Límites de longitud en el formulario y validación real en backend. |
| 15 | Sanitizar contenido | ✅ Todo texto externo se escapa antes de pintarlo (`siaEsc`, `rvEsc`, `esc`). |
| 16 | Restringir archivos | N/A — no se suben archivos. |
| 17 | Devolver solo lo necesario | ✅ En backend. |
| 18 | Security headers | ✅ CSP y Referrer-Policy por `<meta>` (GitHub Pages no permite cabeceras propias; HSTS lo pone GitHub). |
| 19 | Forzar HTTPS | ✅ Hosting solo HTTPS + `upgrade-insecure-requests`. |
| 20 | Escanear dependencias | N/A — sin dependencias npm (todo inline). |
