# 📋 Cheatsheet Cap 1 — Fundamentos del Testing (1 página)

> *Imprimible. Pegar en la pared o tener a mano para repasar.*

---

## 🎯 ISTQB en 1 frase

> Testing es el proceso de **verificar y validar** que un producto software cumple lo que tiene que cumplir, **encontrar defectos** antes de que lleguen al usuario, y **dar confianza** sobre la calidad.

---

## 🧬 Cadena causal: Error → Defect → Failure ⭐

```
ERROR (mistake)         La persona cometió un error
   ↓ causa
DEFECT (fault, bug)     La imperfección está en el producto
   ↓ se ejecuta
FAILURE                 Comportamiento observable incorrecto
```

**Dental:**
- Error: el odontólogo no vio la caries
- Defect: la caries progresó sin tratar
- Failure: el paciente vuelve con dolor

> 📌 **Defect puede existir sin causar failure.** (Una necrosis puede estar sin síntomas.)

---

## ⭐ LOS 7 PRINCIPIOS DEL TESTING ⭐⭐⭐ (memorizar)

| # | Principio | Dental |
|---|---|---|
| 1 | **Testing shows the presence of defects, not their absence** | Ningún odontólogo puede garantizar 100% |
| 2 | **Exhaustive testing is impossible** | Imposible testear todos los pacientes en todos los estados |
| 3 | **Early testing saves time and money** | Diagnóstico temprano = tratamiento más barato |
| 4 | **Defects cluster together** | 80% caries en molares; 80% bugs en 20% del código |
| 5 | **Beware the pesticide paradox** | Si siempre mirás las 6 mismas caras, dejás de ver lo nuevo |
| 6 | **Testing is context-dependent** | No se trata igual caries en paciente con xerostomía |
| 7 | **Absence-of-errors is a fallacy** | Endodoncia perfecta + paciente con dolor = falla funcional |

---

## 🔄 Testing vs Debugging

| Testing | Debugging |
|---|---|
| Encontrar el defecto | Encontrar la causa raíz y corregirlo |
| Lo hace el tester | Lo hace el developer |
| "Esto falla" | "Esto falla PORQUE…" |

---

## 🏭 QA vs Testing

| QA (Quality Assurance) | Testing (Quality Control) |
|---|---|
| **Procesos** (cómo se trabaja) | **Producto** (qué se entrega) |
| Proactivo | Reactivo |
| Definir el protocolo de endodoncia | Ejecutar el protocolo en un paciente |

---

## ✅ Verification vs Validation ⭐

| Verification | Validation |
|---|---|
| ¿Lo hicimos bien? | ¿Es lo correcto? |
| ¿Construimos el producto correctamente? | ¿Construimos el producto correcto? |
| Confirmar el cumplimiento de requisitos | Confirmar que satisface necesidades del usuario |
| Documentos + ejecución contra specs | Usuario real |
| "El conducto está obturado a longitud" | "El paciente puede masticar sin dolor" |

> 📌 **V&V.** Memorizar la diferencia. Sale siempre.

---

## 🔄 Actividades del testing (orden)

```
1. Test Planning
2. Test Monitoring & Control (continuo)
3. Test Analysis → test conditions
4. Test Design → test cases
5. Test Implementation → test procedures, suites
6. Test Execution
7. Test Completion
```

**Dental:** Plan de tratamiento → control → análisis → diseño del plan → preparación del instrumental → ejecución → epicrisis.

---

## 🧠 Psicología + Independencia

- **Independencia:** cuanto más separado esté el tester del autor, mejor encuentra defects
- **Sesgo de confirmación:** "yo lo hice, debe estar bien" — bloquea el testing
- **Más independencia:** mejor testing

| Nivel de independencia | Quién testea |
|---|---|
| Bajo | El mismo developer |
| Medio | Otro developer del equipo |
| Alto | Tester dedicado del equipo |
| Muy alto | Tester externo a la organización |

---

## 🎯 Objetivos típicos del testing (LO 1.1.1)

1. Evaluar work products
2. Detectar defects
3. Reducir riesgo
4. Verificar cumplimiento de requisitos
5. Validar necesidades del usuario
6. Construir confianza
7. Mejorar calidad
8. Cumplir regulaciones

---

## ⚠️ Lo que NO es testing

- ❌ No es debugging
- ❌ No es solo ejecutar el software
- ❌ No garantiza 0 defectos
- ❌ No es responsabilidad solo del tester

---

*Cap 1 listo. Dominás esto, tenés 50% del Cap 1 en el examen.*
