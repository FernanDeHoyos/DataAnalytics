# 📊 Dashboard de Ingresos de Eventos con Streamlit

Este proyecto implementa una aplicación web interactiva construida con **Streamlit**, que permite visualizar los **ingresos de eventos** registrados por usuarios (como profesores) a lo largo del tiempo, categorizados por **departamento**, **rol docente**, y diversas variables temporales (día, semana, mes, hora). Está diseñado para analizar patrones de actividad de acceso a un sistema educativo o de gestión.

---

## 🚀 ¿Qué muestra el dashboard?

La aplicación está dividida en tres secciones principales accesibles desde el menú lateral:

### 1. **Datos Generales**
- ✅ Total de ingresos registrados
- 📊 Gráfico de barras por **departamento**
- 🥧 Gráfico de torta por **departamento**
- 📈 Gráficos de líneas por ingresos:
  - Por día
  - Por semana
  - Por mes
- ⏰ Gráfico de barras por **hora**
- 🔥 Heatmap de actividad por hora y departamento

### 2. **Datos por Departamento**
- Selector de departamento
- 📊 Ingresos por docente en ese departamento
- 🥧 Gráfico de torta por docente
- 📈 Líneas de ingresos por día, semana y mes
- 🔥 Heatmap específico de ese departamento

### 3. **Datos por Profesor**
- Selector de docente
- 📈 Líneas de ingresos por día, semana y mes
- 🔥 Heatmap de actividad por hora de ese docente

---

## 🗂️ Estructura esperada del archivo `datos.csv`

Tu archivo `datos.csv` debe tener las siguientes columnas:

| Columna        | Descripción                                                  |
|----------------|--------------------------------------------------------------|
| `logid`        | ID del evento                                                |
| `eventname`    | Nombre del evento                                            |
| `timecreated`  | Marca de tiempo en formato UNIX (segundos desde 1970)       |
| `origin`       | Origen del evento                                            |
| `userid`       | ID del usuario                                               |
| `department`   | Departamento al que pertenece el usuario                     |
| `roleteacher`  | Rol del docente o nombre del profesor                        |

---

## ⚙️ ¿Cómo correr la aplicación?

### 1. **Clona este repositorio** (o descarga los archivos):
```bash
git clone https://github.com/tu_usuario/nombre_repositorio.git
cd nombre_repositorio