# MallaIQ — Sistema visual "Minimal Apple / Mochy" (v7.0)

Neutros puros, vidrio translúcido, cápsulas y transiciones suaves con curva iOS. Inspirado en la estética de Mochy Music (solo el lenguaje visual; su código es GPL-3 y no se copió).

## Tokens (bloque v7.0 al final del CSS)
- **Fondo:** `#000` de noche, `#f5f5f7` de día. Arriba hay un brillo de dos colores, verde a la izquierda y naranja a la derecha (como HomeTopGlow de Mochy).
- **Superficies:** blancas translúcidas (6–10% de noche, 78% de día), con `backdrop-filter: blur(16–40px) saturate(1.5–1.8)` y un filete de 1px.
- **Texto:** `#f5f5f7` / `#a1a1a6` de noche, `#1d1d1f` / `#6e6e73` de día (neutros de Apple).
- **Acento:** verde de marca `--primary`. Ámbar para parcial, rojo para reprobada, verde suave para aprobada.
- **Radios:** 999px en botones, chips, pestañas y badges; 16px en materias; 20px en paneles; 24px en modales.

## Tipografía
Inter (con -apple-system y SF Pro en Apple), `letter-spacing: -0.011em`, cifras tabulares. Los títulos van en peso 700 con `-0.03em`.

## Componentes
- **Pestañas:** control segmentado de vidrio en cápsula. El indicador blanco o negro se desliza con `--ease-ios`, y la barra se queda pegada al hacer scroll.
- **Encabezados de semestre y agrupación:** texto suave sin fondo, más un punto de color por componente.
- **Materias:** al pasar el mouse suben 2px; al presionar bajan a escala 0.97; al aprobar, rebote con `--ease-bounce`.

## Movimiento
- `--ease-ios: cubic-bezier(0.32, 0.72, 0, 1)`, duraciones de 0.25–0.5s.
- **Vista:** fundido, escala 0.985 y desenfoque de 6px. **Modal:** sube como una hoja. **Tema:** View Transitions.
- Todo se desactiva con `prefers-reduced-motion`.
