# MallaIQ — Producto

## Qué es
Herramienta web independiente y sin ánimo de lucro para estudiantes de Ingeniería Química de la Universidad Nacional de Colombia, sede Bogotá (Facultad de Ingeniería). Un solo `index.html` desplegado en Vercel (mallaiq.vercel.app); backend propio en Render (`proxy-sia`) para catálogo del SIA (grupos, cupos, horarios) y reseñas anónimas de profesores.

## Para quién y cuándo
Estudiantes de pregrado, casi siempre desde el celular o la laptop, de noche o entre clases, sobre todo en temporada de inscripción de materias: deciden qué ver el próximo semestre, revisan prerrequisitos, cupos y choques de horario, y calculan su PAPA.

## Funciones (no se quitan)
- Malla interactiva por semestres con estados: bloqueada, parcial, disponible, reprobada, aprobada; líneas de prerrequisitos (Conexiones); créditos aprobados vs. 180.
- Calculadora histórica: PAPA acumulado, PAPI por semestre, nivelación.
- Programa por agrupaciones y Libre elección: grupos, cupos y horarios del SIA.
- Horario semanal con planes A/B/C, detección de choques, copiar e imprimir.
- Info y calendario académico, trámites, contactos.
- Reseñas anónimas de profesores, comentarios, novedades por versión, botón de café, modo día/noche.
- Estado del estudiante guardado en localStorage (claves existentes no se cambian).

## Modo
Operate: el estudiante completa una tarea. Escaneo rápido, estados claros y densidad útil valen más que la expresión.

## Restricciones
- No romper funciones, IDs, ni claves de localStorage.
- Debe funcionar bien en móvil (Android) y escritorio, con modo día y noche.
- Escalará a otras carreras de la Facultad de Ingeniería.
- Ligero: sin frameworks, sin build.

## Compromisos de marca
Nombre "Malla Curricular IQ" / MallaIQ. Proyecto estudiantil, cercano, en español colombiano informal.
