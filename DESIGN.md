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

## v8 · Movimiento con los valores de Mochy
Se leyeron los parámetros de animación de Mochy Music (github.com/realidkroo/Mochy-Music) y se reescribieron en CSS; no se copió código (es Kotlin y GPL-3).
- **Curvas:** `--ease-emph: cubic-bezier(0.2, 0, 0, 1)` (principal) y `--ease-menu: cubic-bezier(0.57, 0.53, 0, 1)` a 440 ms (menús y hojas).
- **Resortes** (como `linear()`): `--spring-smooth` (amortiguación 0.8, rigidez 500), `--spring-bounce` (0.55 / 380) y `--spring-snap` (0.54 / 720).
- **Presión:** botones a escala 0.94 y materias a 0.96, bajan en 110 ms y vuelven con resorte.
- **Modales:** entran y salen; en celular son hojas que suben desde abajo.
- **Malla:** los semestres entran escalonados (32 ms) solo al abrir la pestaña; ya no se re-animan en cada clic.
- **Estados:** "disponible" va en contorno verde y "aprobada" rellena.
- **Avisos flotantes:** fondo casi opaco; el de comentarios es una cápsula fija abajo a la derecha.

## v9 · Azul, requisitos por color y varias carreras
- **Acento:** azul (`#6ea8ff` de noche, `#2f6fed` de día); brillo superior azul y violeta. Verde solo para "aprobada".
- **Requisitos:** ya no hay líneas permanentes. Al pasar el cursor, o con ⋮ → Ver requisitos, la materia se enfoca: sus requisitos en morado (`--req`), lo que abre en azul, lo demás atenuado, y solo esas líneas.
- **Emergentes:** `--glass` casi opaco (90%) con desenfoque en menús, avisos y modales.
- **Ventanas:** cupos hasta 1040 px con los grupos en rejilla; reseñas y libre elección 720 px; en celular, hoja inferior.
- **Carreras:** `PROG` define la carrera activa; las que no son Química guardan su estado con prefijo `<id>:`.

## v10 · Planificar
- Botón **Planificar** en la barra de la malla: cada materia se arrastra a otro semestre (ratón de inmediato; en táctil, tras mantener presionado 320 ms para no bloquear el desplazamiento) o se mueve con ‹ ›.
- Hasta 14 semestres; siempre hay uno vacío al final para soltar. Créditos por semestre en el encabezado (ámbar si pasa de 21).
- Avisos no bloqueantes con **Deshacer**: prerrequisito después o en el mismo semestre, y requisitos de créditos (108, 53, 60). Las materias con problema quedan con borde rojo.
- Se guarda por carrera en `malla_iq_plan_v1` / `malla_iq_plan_on`; al salir se ve la malla oficial.

## v11 · Thinking orbs
Indicadores de carga de [thinking-orbs](https://github.com/Jakubantalik/thinking-orbs) (MIT, Jakub Antalik). Se incrusta solo su motor de canvas 2D (~14 KB, sin React) y un elemento propio `<thinking-orb state size="64|20">`.
- `searching` 64: consultas al SIA (cupos, horario, libre elección). `weaving` 64: cargar reseñas.
- `solving` 20: revisión de una reseña. `composing` 20: enviar comentario. `connecting` 20: servidor dormido. `working` 20: lista de libre elección. `shaping` 20: aviso de carrera en construcción.
- Un solo `requestAnimationFrame` para todos; se pausan fuera de pantalla o con la pestaña oculta; cuadro fijo con "reducir movimiento"; siguen el modo día/noche.
- **Variación:** cada lugar tiene varios estados posibles (`state="searching connecting working"`) y cada espera elige uno distinto al anterior; si el mismo aviso se repinta en menos de 2,5 s (contadores) conserva el que tenía.
