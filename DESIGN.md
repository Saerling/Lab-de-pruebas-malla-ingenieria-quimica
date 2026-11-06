# MallaIQ — Sistema visual "Afiche serigrafiado" (v5.0)

El estado académico se imprime con tintas planas, como un afiche serigrafiado del campus. Cada tinta tiene un trabajo y no se usa de adorno.

## Tintas (tokens en `:root` / `[data-theme="light"]`, bloque v5.0 al final del CSS)
| Token | Noche | Día | Trabajo |
|---|---|---|---|
| `--paper` / `--bg` | #17140f | #e9e7e0 | Fondo de papel con trama `--halftone` de 6px |
| `--surface` / `--surface-2` | #1f1b15 / #29241c | #f5f4ef / #dfddd4 | Tarjetas y campos |
| `--text` / `--text-dim` | #f1ead9 / #a89d88 | #1d1b17 / #5f5a4f | Texto; `--text` también rellena franjas de encabezado |
| `--ink-blue` | #4d7cff | #1f4fe0 | Aprobado, acción primaria, progreso |
| `--ink-yellow` | #ffd23f | #f2bb00 | Disponible, parcial, pestaña activa |
| `--ink-pink` | #ff5c8a | #e8336b | Reprobado, alertas, registro corrido |

`--primary`, `--success`, `--danger`, `--warning` y `--accent` son alias de las tintas, así que todo el CSS viejo hereda el sistema.

## Tipografía
- **Archivo** (variable, `wdth` 62–125). Rótulos, pestañas, encabezados y botones van a `font-stretch: 70%`, peso 800 y mayúsculas. El título va a 62% y peso 900.
- El texto corrido va en Archivo a ancho normal.
- **JetBrains Mono** (`--data`) solo para datos: créditos, códigos, PAPA, horas.

## Firma
- **Registro corrido:** sombra rosa desfasada 3px/2px en el título; 2px en tarjetas aprobadas y en el botón principal.
- **Retícula visible:** filetes de 1px entre columnas de semestre; los encabezados son franjas sólidas de `--text`.
- Radios pequeños: 6px en tarjetas, 0 en franjas y pestañas.

## Movimiento
- **Jalón de rasero:** `clip-path` de izquierda a derecha al cambiar de vista (`inkPull`, 0.5s, ease-out exponencial) y al cambiar de tema (View Transitions).
- La aprobación de una materia se imprime con un golpe de tinta (`approveIn`).
- El indicador de pestaña amarillo se desliza.
- Las tarjetas aparecen con el scroll (`animation-timeline: view()`).
- Todo se desactiva con `prefers-reduced-motion`.

## Reglas
- No usar degradados decorativos; una franja de tres tintas solo en el bloque de agradecimientos.
- Nada de sombras difusas de color ni halos: las sombras tienen desfase.
- Los estados nuevos usan una de las tres tintas según su trabajo, nunca un color nuevo.
