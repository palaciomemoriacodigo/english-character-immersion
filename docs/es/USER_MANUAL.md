# 📘 English Character Immersion & RPG — Manual de usuario y mantenimiento

**Versión del manual:** 2.2 · **Fecha de actualización:** 24 de noviembre de 2026  
**Proyecto:** English Character Immersion & RPG · **Idioma del manual:** español · **Objetivo de aprendizaje:** B2 alto → C1

> **Propósito de este archivo:** servir como documentación consultable desde cualquier conversación del proyecto. Es una guía de uso y mantenimiento, no un sustituto de las instrucciones del proyecto ni de los módulos especializados. Si existe una discrepancia, para ejecutar una actividad prevalecen las instrucciones principales y el módulo específico correspondiente. Para consultar el funcionamiento, se puede usar este manual como índice.

## Índice

1. Objetivo y funcionamiento general
2. Dónde guardar este manual y cómo consultarlo
3. Inicio y menú principal
4. Personajes y conversaciones
5. Aprendizaje de inglés y correcciones
6. Cierre de sesión e informes de errores
7. Archivos Markdown y CSV: qué guardar y dónde
8. Análisis de errores con Python
9. RPG de Shadow Slave: crear una aventura
10. RPG: jugar, progresar y guardar
11. Memoria, canon y continuidad
12. Comandos: referencia rápida
13. Arquitectura y archivos del proyecto
14. Organización recomendada de conversaciones
15. Mantenimiento y ampliación
16. Limitaciones y solución de problemas
17. Hoja de ruta y criterios de diseño

---

## 1. Objetivo y funcionamiento general

El proyecto utiliza **conversaciones inmersivas, preferentemente por voz**, para practicar inglés y avanzar hacia B2 alto y después C1. Combina:

- Conversaciones con personajes ficticios de personalidades diferenciadas.
- Debates de filosofía y psicología, narración, vida cotidiana e inglés profesional.
- Aventura narrativa RPG ambientada en un escenario original basado en *Shadow Slave*.
- Correcciones adaptativas y revisiones de errores observados.
- Informes descargables para construir un historial de aprendizaje cuando las herramientas lo permitan.

**Principio central:** el personaje es la identidad; la conversación es el vehículo; aprender inglés es el objetivo.

## 2. Dónde guardar este manual y cómo consultarlo

**Recomendación:** subir este Markdown a **Fuentes / Archivos del proyecto** en `English Character Immersion & RPG`. De esta forma, puede servir como referencia a los distintos chats **del mismo proyecto**. No significa que todos los chats externos al proyecto accedan de manera garantizada al documento.

**Instalación:**

1. Abre el proyecto en ChatGPT.
2. Localiza el apartado de **fuentes** del proyecto y selecciona la opción para añadir un archivo.
3. Sube `00_Manual_Usuario_English_Character_Immersion_RPG.md`.
4. No lo pegues dentro de las **instrucciones principales**, porque esas tienen un límite de 8.000 caracteres.
5. Opcional: crea un chat llamado `📘 00 — Manual y mantenimiento` para pedir cambios y conservar decisiones de diseño.

**Consultas de ejemplo en cualquier chat del proyecto:**

- «Consulta el manual: ¿qué hace Feedback later?»
- «Según el manual, ¿cómo puedo iniciar una aventura con Nephis?»
- «¿Qué debo decir para recibir mi informe de errores?»
- «¿Dónde tengo que guardar los CSV?»
- «Revisa el manual y dime qué archivos debo cambiar para añadir otro personaje».

Si tienes una duda técnica importante, pide expresamente **«consulta el archivo del manual y el módulo correspondiente»**. Tener una fuente disponible facilita su uso, pero no garantiza que se recupere íntegramente en cada respuesta.

## 3. Inicio y menú principal

Al iniciar un chat sin una petición concreta, el asistente pregunta en inglés:

> What would you like to do today? Talk to a character, start a new adventure, continue an adventure, or practise English?

| Opción | Resultado |
|---|---|
| **Character Conversation** | Elegir personaje y mantener una conversación. |
| **New RPG Adventure** | Configurar una campaña nueva paso a paso. |
| **Continue Adventure** | Recuperar el último checkpoint disponible. |
| **English Training** | Elegir una destreza y personaje o profesor. |

No es necesario pasar por el menú si ya indicas la actividad: `I want to talk to Sunny`, `Quick start with Nephis`, `I want to practise prepositions`, etc. `Main menu` devuelve al inicio sin borrar una campaña.

## 4. Personajes y conversaciones

| Personaje | Obra | Rasgos y enfoque de conversación |
|---|---|---|
| **Lelouch** | *Code Geass* | Estrategia, poder, responsabilidad y conflictos afectivos. |
| **Sunny** | *Shadow Slave* | Libertad, supervivencia, desconfianza y sarcasmo protector. |
| **Nephis** | *Shadow Slave* | Convicción, sacrificio, determinación y emociones contenidas. |
| **Izaya** | *Durarara!!* | Motivaciones humanas, contradicciones, dilemas éticos y provocación. |
| **Roxas** | *Kingdom Hearts 358/2 Days* | Identidad, amistad, memoria y pertenencia. |
| **Professional English Teacher** | — | Explicación y práctica estructurada de inglés. |
| **Random Character** | — | Selección inesperada para variar la conversación. |

Al elegir un personaje se utiliza su dossier. Habla en primera persona, puede discrepar, errar, rectificar y proponer temas. **No debe comportarse como un profesor genérico con distinta voz.** Su relación con el usuario no se inventa: debe basarse en interacciones realmente disponibles y respetar límites de spoilers.

**Ideas de actividad:** conversación libre, psicología, filosofía, debate, historia interactiva, entrevistas, reuniones, tecnología, programación, logística o vida cotidiana.

**Comandos útiles:** `Change character`, `Be yourself`, `Tell me about your past`, `Let's debate`, `Surprise me`, `Out of character`, `Back in character`.

## 5. Aprendizaje de inglés y correcciones

El idioma principal es inglés, con español de apoyo cuando resulte útil. El nivel se ajusta durante la práctica. Se trabajan preposiciones, tiempos, gramática, pronunciación, condicionales, vocabulario, idioms, phrasal verbs y comunicación profesional.

| Modo | Qué ocurre |
|---|---|
| **Balanced** (predeterminado en conversación) | Corrige brevemente errores relevantes o repetidos sin romper la naturalidad. |
| **Relaxed** | Interviene solo ante errores importantes. |
| **Strict** | Corrige más exhaustivamente y permite repetir. |
| **Immersion** | Habla solo inglés, salvo cambio solicitado. |
| **Feedback later** (predeterminado en RPG) | No interrumpe para corregir salvo confusiones importantes; revisa cuando se solicite. |

**Diferencia importante:** un error gramatical confirmado no es lo mismo que una frase correcta que podría sonar más natural. El sistema debe separarlos.

Se pueden solicitar actividades concretas: `I want to practise prepositions`, `Let's practise a job interview`, `Teach me phrasal verbs`, `Speak more slowly`, `Explain in Spanish`, `Correct me`, `Challenge me` o `Make it easier`.

Para pronunciación, puede ofrecer IPA y una aproximación española. **No debe evaluar pronunciación, acento o entonación basándose solo en una transcripción escrita.** Tampoco debe asignar un CEFR concreto sin evidencia suficiente.

## 6. Cierre de sesión e informes de errores — versión 1.1

Esta es una funcionalidad especialmente importante del proyecto. Sigue `08_English_Error_Tracking.md` y **funciona con confirmación previa**.

### 6.1. Primer paso: despedida

El usuario indica de forma natural que quiere terminar: `That's all for today`, `Let's stop here`, `End session`, «Está bien por hoy», «Lo dejamos aquí», etc. El personaje se despide brevemente en inglés y pregunta **una sola vez**:

> **Would you like me to generate your English feedback report for today's conversation?**

**Todavía no genera el informe.** Espera una respuesta.

### 6.2. Segundo paso: respuesta

| Tu respuesta | Comportamiento esperado |
|---|---|
| `Yes, please`, `Sure`, `Sí`, `Adelante` | Genera la revisión en esa respuesta, sin volver a pedir permiso. |
| `No, thanks`, `Not today`, `No` | Se despide sin informe. |
| Respuesta ambigua | Pide una aclaración breve. |
| `Feedback now`, `Generate my report`, «Hazme el informe» | Genera directamente, sin esperar a una despedida ni pedir confirmación. |
| `Just say goodbye` | Termina sin preguntas. |

### 6.3. Qué debe contener el informe confirmado

- Frases originales **realmente observadas** en tus intervenciones accesibles.
- Correcciones y explicación de la regla.
- Clasificación: preposiciones, tiempos, artículos, estructuras verbales, orden, etc.
- Mejoras de naturalidad separadas de errores reales.
- Repeticiones verificables y patrones relevantes.
- Vocabulario aprovechable, 2–4 ejercicios y un objetivo para la siguiente sesión.
- Informe **Markdown** y registro **CSV**, solo cuando las herramientas disponibles permitan crear archivos auténticos.

**Ejemplo ficticio, no atribuible al usuario:**

| Original | Corrección | Categoría |
|---|---|---|
| `I depend of my friends.` | `I depend on my friends.` | `prepositions` |

Si no hay errores detectables, debe decirlo; no inventar observaciones para rellenar tablas. En sesiones largas puede no haber acceso a todos los turnos: el informe debe indicar la cobertura real.

**Por voz:** se puede formular la pregunta y resumir 1–3 hallazgos. Si la interfaz no permite exportar, continúa **en el mismo chat en modo texto** para solicitar los archivos. El cierre no se activa por cerrar la aplicación sin enviar un mensaje.

**En RPG:** al despedirte se prepara primero un checkpoint copiable, salvo que pidas no guardar. El informe lingüístico requiere su propia confirmación.

## 7. Archivos Markdown y CSV: qué guardar y dónde

La revisión de una sesión puede producir:

- `Session_Review_20261124_01.md`: informe legible, explicaciones y ejercicios.
- `Session_Errors_20261124_01.csv`: observaciones estructuradas para análisis histórico.

La plantilla `Session_Review_TEMPLATE.md` guía la presentación del informe. `Session_Errors_TEMPLATE.csv` define las columnas. **Son plantillas, no registros que se sobrescriban automáticamente.** Puedes añadirlas a las fuentes del proyecto como referencia. Las observaciones reales deben ir en archivos nuevos de cada sesión.

**Esquema del CSV:**

`session_id,date,character,activity,feedback_mode,source,record_type,category,rule_id,original,corrected,explanation_es,occurrences,priority,confidence,practice_prompt`

- `record_type`: `error` o `naturalness`.
- `rule_id`: identificador estable de una regla, por ejemplo `PREP_DEPEND_ON`.
- `occurrences`: repeticiones efectivamente constatadas.
- `source`: `text` o `voice_transcript`.
- `confidence`: `high` o `medium`; datos inciertos no deben contarse como errores confirmados.

**Guardar en el ordenador:** conserva los `.md` para estudiar y los `.csv` dentro de una carpeta `reportes/` para un análisis acumulado. Los archivos fuente del proyecto, como `07_English_Learning_Progress.md`, **no se actualizan por sí solos**.

## 8. Análisis de errores con Python

El archivo `analizar_errores.py` **se ejecuta en tu ordenador**, no hace falta subirlo como fuente. No interviene en las conversaciones ni guarda automáticamente sus resultados.

Ejemplo de organización:

```text
English_Learning/
├── analizar_errores.py
├── reportes/
│   ├── Session_Errors_20261124_01.csv
│   ├── Session_Errors_20261125_01.csv
│   └── Session_Errors_20261126_01.csv
└── analisis_resultados/     # se crea al ejecutar
```

Abre un terminal en `English_Learning` y ejecuta:

```bash
python analizar_errores.py --input reportes --output analisis_resultados
```

El script crea `Historico_errores.csv`, `Resumen_por_categoria.csv`, `Patrones_por_regla.csv` y `Resumen_historico.md`. Distingue errores y mejoras de naturalidad, y señala reglas repetidas en sesiones distintas.

**Interpretación:** un mayor número bruto de errores no implica necesariamente peor nivel si también aumenta la cantidad de conversación. Para medir evolución de forma rigurosa haría falta normalizar por oportunidades de uso o volumen comparable de habla.

## 9. RPG de Shadow Slave: crear una aventura

El RPG es una **historia original no canónica**, respetuosa con el universo y sin spoilers posteriores a la época elegida. El asistente es narrador, Game Master y compañero con autonomía propia. **Tú controlas tus palabras, elecciones e intentos de acción.**

Para empezar, di `Start a new adventure`, `Shadow Slave RPG`, `Quick start with Sunny` o `Quick start with Nephis`.

| Parámetro | Opciones |
|---|---|
| Compañero | Sunny, Nephis, ambos o aleatorio |
| Rango inicial | Sleeper o Awakened |
| Aspect | Aleatorio, personalizado o excepcional |
| Dificultad | Forgiving, Survival o Lethal |
| Estilo | Equilibrado, supervivencia, misterio, combate, exploración, psicológico |
| Inglés | Adaptable |
| Correcciones | Modo seleccionable |

Se pregunta **de una en una** solo por las opciones no decididas. Antes de comenzar, apruebas la ficha propuesta.

### Inicio rápido

`Quick start` o `Surprise me` durante la configuración rellena los campos pendientes con: compañero aleatorio (si no elegiste uno), **Sleeper**, Aspect aleatorio, **Survival**, estilo equilibrado, compañeros con autonomía alta, inglés **B1–B2** y **Feedback later**. **No hay muerte permanente del protagonista salvo consentimiento expreso.**

Si seleccionas **Awakened**, se ajustan la misión inicial y las dos habilidades de Aspect apropiadas al rango.

## 10. RPG: jugar, progresar y guardar

### 10.1. Jugar naturalmente

No hacen falta menús de acciones. Puedes decir `I look around`, `I investigate the ruins`, `I use my Aspect`, `I hide behind the rocks`, `Sunny, what do you think?` o `I disagree with your plan`. Las decisiones producen consecuencias coherentes; los compañeros pueden proponer alternativas, retirarse o discrepar.

### 10.2. Progresión y estado

Ruta inicial de referencia: **Aspirant → First Nightmare → Sleeper → Dream Realm → Gateway → Awakened**. El Sleeper tiene Aspect, habilidad Dormant, Attributes y Flaw. Al despertar obtiene una segunda habilidad. El **rango del alma** y el **rango del Aspect** son conceptos diferentes.

`Show my status` presenta el estado disponible. También puedes pedir `Show my inventory`, `What is my Flaw?`, `Show my current objectives`, `Inspect` o `Pause story`.

### 10.3. Guardar y continuar

Al pausar, volver al menú o despedirte, se prepara un **checkpoint** (también puedes pedir `Save campaign`) con ID de campaña, ficha y habilidades, equipo, recursos, heridas, lugar, objetivo, decisiones, relaciones, misterios pendientes y última escena. Copia el checkpoint en un archivo privado y pégalo en el siguiente chat si no se recupera. No necesitas añadir otra fuente. Conserva el último estado, los eventos completados, los enemigos derrotados y los costes.

Ejemplo: `Campaign_001_Sunny_Checkpoint_001.md`.

`Continue our adventure` verifica el último checkpoint y los acontecimientos posteriores confirmados, resume la última acción resuelta y continúa desde la decisión pendiente. Si falta el estado dinámico, pide el checkpoint o un resumen. No debe repetir combates resueltos, inventar partidas ni afirmar que una fuente se ha actualizado.

**Orden recomendado al dejar una campaña:** despídete, conserva el checkpoint generado y confirma o rechaza el informe de inglés. Si cierras sin enviar mensaje no se genera un checkpoint. `Update character memory` y `Update learning progress` son actualizaciones opcionales y separadas.

## 11. Memoria, canon y continuidad

- **Canon:** hechos del universo y etapa narrativa del personaje.
- **Ficción nueva:** sucesos creados dentro de una aventura o historia interactiva.
- **Información compartida:** datos y preferencias que el usuario expresa de forma real.

No mezclar esos niveles. No se transmiten secretos de un personaje a otro sin permiso. No inventar conversaciones compartidas ni spoilers. Cada personaje mantiene una perspectiva propia.

`06_Character_Relationships.md` contiene el formato de continuidad de personajes. `07_English_Learning_Progress.md` contiene el esquema de aprendizaje. `08_English_Error_Tracking.md` define los informes y criterios de error. Los archivos son **fuentes de referencia, no bases de datos con escritura automática**.

- `Update character memory`: propuesta copiable para el registro de relaciones.
- `Update learning progress`: propuesta de progreso respaldada por evidencia observada.
- `Review my mistakes`: repasa fallos presentes en registros accesibles.

## 12. Comandos: referencia rápida

| Quiero... | Puedo decir... |
|---|---|
| Menú | `Main menu` |
| Hablar con un personaje | `I want to talk to Roxas` |
| Cambiar personaje | `Change character` |
| Sorprenderme con un tema | `Surprise me` (en conversación) |
| Debate | `Let's debate` |
| Más dificultad | `Challenge me` |
| Menos dificultad | `Make it easier` |
| Hablar más despacio | `Speak more slowly` |
| Apoyo español | `Explain in Spanish` |
| Salir/volver del personaje | `Out of character` / `Back in character` |
| Corregir un turno | `Correct me` |
| Correcciones al final | `Feedback later` |
| Informe inmediatamente | `Feedback now` / `Generate my report` |
| Terminar y recibir pregunta de confirmación | `That's all for today` |
| Terminar sin pregunta | `Just say goodbye` |
| Práctica de inglés | `I want to practise conditionals` |
| Iniciar RPG rápido | `Quick start with Sunny` |
| Consultar ficha RPG | `Show my status` |
| Guardar campaña | `Save campaign` |
| Recuperar campaña | `Continue our adventure` |
| Registrar relación | `Update character memory` |
| Proponer actualización de progreso | `Update learning progress` |

Se aceptan formulaciones equivalentes en español o en inglés. Los comandos no son contraseñas ni requieren pronunciación literal.

## 13. Arquitectura y archivos del proyecto

Las **instrucciones principales** hacen de *router/controller* y están sujetas al límite de **8.000 caracteres**. Los Markdown son módulos de referencia y permiten mantener las reglas extensas fuera de ese límite.

| Archivo | Función |
|---|---|
| `00_Character_Immersion_Protocol.md` | Protocolo de interpretación y enseñanza |
| `01_Lelouch_Character_Profile.md` | Perfil de Lelouch |
| `02_Sunny_Character_Profile.md` | Perfil de Sunny |
| `03_Nephis_Character_Profile.md` | Perfil de Nephis |
| `04_Izaya_Character_Profile.md` | Perfil de Izaya |
| `05_Roxas_Character_Profile.md` | Perfil de Roxas |
| `06_Character_Relationships.md` | Continuidad narrativa independiente |
| `07_English_Learning_Progress.md` | Seguimiento de aprendizaje |
| `08_English_Error_Tracking.md` | Registro, clasificación y cierre confirmado |
| `09_Shadow_Slave_RPG_Campaign.md` | Motor RPG |
| `Session_Review_TEMPLATE.md` | Plantilla opcional del informe legible |
| `Session_Errors_TEMPLATE.csv` | Plantilla opcional del registro de datos |
| **`00_Manual_Usuario_English_Character_Immersion_RPG.md`** | **Este manual de consulta y mantenimiento** |

Fuera de ChatGPT puedes conservar `analizar_errores.py`, los informes reales y una copia de seguridad de las fuentes.

## 14. Organización recomendada de conversaciones

No es necesario crear todos los chats desde el principio. Una estructura útil sería:

```text
📘 00 — Manual y mantenimiento
🔧 01 — Desarrollo del proyecto
💬 Conversation — Sunny
💬 Conversation — Nephis
💬 Conversation — Lelouch
💬 Conversation — Izaya
💬 Conversation — Roxas
📚 English Training — Grammar
💼 English Training — Professional English
🎲 RPG 001 — Sunny
🎲 RPG 002 — Nephis
```

**Recomendación:** un chat independiente por campaña RPG para evitar mezclar estados. El manual está en **fuentes**, así que no necesitas duplicarlo en todas las conversaciones.

## 15. Mantenimiento y ampliación

### Añadir personajes

Crea un dossier individual con universo, etapa, recuerdos canónicos, motivaciones, valores, contradicciones, relaciones, estilo de habla, límites de spoilers y ejemplos originales. Añade el personaje al menú de las instrucciones principales y al formato de relaciones. Evita duplicar un identificador de archivo existente.

### Crear nuevos RPG

Crea un módulo con ambientación, reglas, ficha, progresión, consecuencias, NPC autónomos y checkpoints. Actualiza las instrucciones principales para que reconozcan el nuevo universo. Posibles universos futuros: *Code Geass*, *Kingdom Hearts* y *Durarara!!*.

### Mejorar Shadow Slave RPG

Posibles extensiones: bestiario, artefactos, facciones, sistema de comercio, regiones originales, habilidades y combates más detallados. Mantén los secretos y la etapa canónica consistentes.

### Mejorar el aprendizaje de inglés

Posibles módulos: gramática, preposiciones, pronunciación, phrasal verbs, inglés profesional, repetición espaciada y ruta B2→C1. Los informes históricos pueden orientar ejercicios, siempre basados en registros disponibles.

### Proceso de modificación recomendado

1. Identifica la función que quieres cambiar.
2. Edita el **módulo especializado** que la gobierna.
3. Cambia las instrucciones principales **solo si afecta al menú, prioridades o activación**; mantén menos de 8.000 caracteres.
4. Actualiza este manual para documentar el nuevo comportamiento.
5. Sustituye la fuente antigua por la nueva; evita versiones contradictorias con el mismo cometido.
6. Prueba el cambio en un chat nuevo del proyecto.

## 16. Limitaciones y solución de problemas

| Problema | Qué revisar |
|---|---|
| No aparece el menú | ¿Era una sesión nueva y no habías indicado ya una actividad? Prueba `Main menu`. |
| El personaje suena genérico | Pide que consulte su dossier y `Be yourself`. |
| Aparecen spoilers | Indica la etapa deseada; el personaje no debe usar conocimiento posterior. |
| No pregunta por el informe al despedirte | Verifica las instrucciones principales y la versión 1.1 de `08_English_Error_Tracking.md`. |
| Pregunta pero no crea archivos | Puede depender de las herramientas del modo voz; continúa en el mismo chat de texto y pide la exportación. |
| El informe incluye errores inventados | Exige frase textual verificable; elimina ejemplos ficticios y observaciones inciertas. |
| No encuentra sesiones anteriores | Proporciona sus CSV/Markdown; la memoria no sustituye los registros guardados. |
| No recupera el RPG | Facilita el último checkpoint válido. |
| Se exceden los 8.000 caracteres | Mueve explicaciones al módulo o a este manual; resume solo las instrucciones principales. |
| El script Python no encuentra datos | Comprueba la carpeta `reportes` y nombres `Session_Errors_*.csv`. |

**Advertencias generales:** las fuentes pueden facilitar continuidad, pero no son memoria perfecta. No se actualizan automáticamente. Las despedidas no generan tareas en segundo plano. Una transcripción de voz puede omitir matices y no equivale a una evaluación acústica.

## 17. Hoja de ruta y criterios de diseño

| Etapa | Estado de referencia | Alcance |
|---|---|---|
| **V1.0 — Character Immersion** | Diseñada | Cinco perfiles, diálogo inmersivo y correcciones |
| **V2.0 — Shadow Slave RPG** | Diseñada | Narración, ficha, progresión y checkpoints |
| **V2.1 — Voice Launcher** | Diseñada | Menú hablado, configuración e inicio rápido |
| **V2.2 — Session Error Tracking** | Configurada a nivel de instrucciones y módulos | Cierre confirmado, informe MD/CSV y análisis offline |
| **V3.0 — Advanced Memory** | Propuesta | Mejor seguimiento de relaciones y decisiones |
| **V4.0 — Advanced RPG** | Propuesta | Bestiario, facciones, artefactos y reglas ampliadas |
| **V5.0 — Multi-Universe RPG** | Propuesta | Nuevos universos y personajes |
| **V6.0 — Advanced English Learning** | Propuesta | Repetición espaciada, métricas y currículo B2–C1 |

El estado «configurada» **no implica** almacenamiento automático, ejecución en segundo plano ni garantía de exportación en todas las interfaces.

**Arquitectura en una frase:** instrucciones = controlador; módulos y dossiers = conocimiento y reglas; chats = contexto de sesión; checkpoints = estado de campaña; Markdown/CSV = evidencia de aprendizaje; Python = análisis acumulado.

---

**Nota de mantenimiento:** actualiza la fecha y versión de este manual cuando cambien de forma importante las instrucciones o los módulos. No lo utilices para sobrescribir la prioridad de los perfiles ni para afirmar acciones técnicas que no se hayan realizado.
