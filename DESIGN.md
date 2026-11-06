# MallaIQ — Sistema visual "Japonés denso" (v6.0)

Inspirado en los sitios japoneses de alta densidad: módulos con filete fino, letra gótica compacta y un rojo utilitario que marca dónde estás. La meta es que quepa mucha información sin que se sienta apretada.

## Color (tokens en el bloque v6.0, al final del CSS)
| Token | Noche | Día | Trabajo |
|---|---|---|---|
| `--bg` / `--surface` / `--surface-2` | #0e1014 / #15181d / #1c2027 | #f3f4f6 / #fff / #f5f6f8 | Fondo, módulos, campos |
| `--border` | #2b3039 | #d8dbe0 | Filete de 1px en todos los módulos |
| `--text` / `--text-dim` | #eef0f3 / #9aa1ad | #16181c / #5d6370 | Texto |
| `--red` | #ff4b55 | #e3001b | Navegación activa, acción principal, pestañitas de encabezado, reprobada |
| `--blue` | #5aa2ff | #0a5fc2 | Disponible, hover, foco |
| `--green` | #3ccf7f | #13804a | Aprobada |
| `--amber` | #f5b53d | #c27a00 | Parcial |

## Tipografía
- **Zen Kaku Gothic New** (400, 500, 700, 900) para toda la interfaz. La base es 14px, y 15px en móvil para que se lea bien.
- **JetBrains Mono** solo para datos: créditos, códigos, PAPA y horas.

## Componentes
- **Módulo:** fondo `--surface`, filete de 1px, radio de 3px y sombra mínima.
- **Encabezado de módulo:** texto en peso 900, alineado a la izquierda, con una pestañita roja de 6×12px y un filete inferior rojo de 2px.
- **Header:** una sola barra. A la izquierda el logo "IQ" en caja roja y el título; a la derecha las utilidades. Debajo van las pestañas, con un subrayado rojo deslizante.
- **Malla:** columnas de 168px como mínimo, 4–6px de separación y tarjetas de 6×8px de relleno.

## Movimiento
- Cambio de vista rápido: 0.18s, fundido más 4px de desplazamiento.
- Tema por View Transitions con fundido de 0.22s.
- Indicador de pestaña deslizante, aparición con el scroll y destello al aprobar una materia.
- Todo se desactiva con `prefers-reduced-motion`.

## Reglas
- No usar degradados, halos ni sombras grandes.
- El rojo es para navegación y alertas, nunca para decorar.
- Todo estado nuevo usa uno de los cuatro colores según su trabajo.
