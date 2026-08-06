# Resumen Cap 1 (v4.0.1) — Fundamentals of Testing

## 1. ¿Qué es testing? (1.1)

**Testing = verificar work products** mediante procesos planificados.

**Objetivos típicos (1.1.1):**
- Evaluar work products (requisitos, diseño, código)
- Detectar defects
- Reducir riesgo
- Verificar cumplimiento de requisitos
- Mejorar calidad
- Cumplir regulaciones
- Construir confianza
- Validar necesidades del usuario

**Testing vs Debugging (1.1.2):**

| Testing | Debugging |
|---|---|
| Encuentra **symptoms** | Corrige **root cause** |
| Tester | Developer |
| Mide calidad del producto | Por qué falló el código |

---

## 2. ¿Por qué el testing es necesario? (1.2)

**Razones (1.2.1):**
- Software en uso crítico (medical, finance)
- Causas de defectos
- Costo de no testing

**Testware types que se pueden testear:**
- Requisitos
- Diseño
- Código
- Casos de prueba
- Datos
- Manual de usuario

**Quality Assurance (QA) vs Testing (1.2.2):**
- QA = enfoque planificado, proactivo sobre **procesos** → calidad
- Testing = actividad de QC (Quality Control) que verifica **producto**

**Terminología crítica (1.2.3):**

```
Error (mistake)
  ↓ causa
Defect (fault, bug) — imperfección
  ↓ ejecuta el path → Failure — comportamiento observable
```

---

## 3. ⭐ Los 7 Principios (1.3.1) — MUY preguntado

1. **Testing shows presence, not absence of defects**
2. **Exhaustive testing is impossible**
3. **Early testing saves time and money**
4. **Defects cluster together**
5. **Beware the pesticide paradox**
6. **Testing is context-dependent**
7. **Absence-of-errors is a fallacy**

---

## 4. Actividades de Testing (1.4.1)

```
1. Test Planning
   ↓
2. Test Monitoring & Control (continuo)
   ↓
3. Test Analysis → test conditions
   ↓
4. Test Design → test cases, test data
   ↓
5. Test Implementation → test procedures, suites
   ↓
6. Test Execution → test logs
   ↓
7. Test Completion → test summary report
```

**Testware (1.4.3)** son los artefactos producidos en estas actividades.

**Roles (1.4.5):** test manager, test lead, tester, test designer, test automation engineer.

**Trazabilidad (1.4.4):** vínculo requisitos ↔ tests ↔ defects ↔ riesgos. Permite evaluar cobertura y entender impacto de cambios.

---

## 5. Habilidades y prácticas (1.5)

**Habilidades genéricas (1.5.1):**
- Analíticas, técnicas, dominio, comunicación, atención al detalle

**Whole team approach (1.5.2):** calidad es responsabilidad de TODO el equipo.

**Independence of testing (1.5.3):** mayor independencia → mejor detección.

Niveles de independencia (de menor a mayor):
1. Mismo developer
2. Peer
3. Test lead independiente
4. Equipo de testing interno
5. Equipo externo

**Drawbacks de independence:** barreras de comunicación, más tiempo.

---

## 🎯 Preguntas típicas

1. ¿Qué es un error?
2. ¿Cuántos principios de testing hay?
3. ¿Qué es testing exhaustivo?
4. ¿Cuándo se hace el testing más temprano?
5. ¿Qué es defect masking?
6. ¿Cuál es la diferencia entre QA y testing?

---

## 📝 Mnemotécnicos

- **7 Principios:** "S-E-E-C-P-C-A"
- **Error → Defect → Failure:** "causa → imperfección → síntoma"
- **Independence levels:** "Self → Peer → Lead → Internal team → External team"
