import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configurar estilo de gráficos
sns.set(style="whitegrid")

# Cargar el archivo CSV
df = pd.read_csv('datos.csv')

# Convertir el campo 'timecreated' a formato datetime
df['timecreated'] = pd.to_datetime(df['timecreated'], unit='s')

# Asegurarse de que el dataframe tenga las columnas correctas
df.columns = ['logid', 'eventname', 'timecreated', 'origin', 'userid', 'department', 'roleteacher']

# Agregar columnas de tiempo útiles
df['day'] = df['timecreated'].dt.date
df['week'] = df['timecreated'].dt.isocalendar().week
df['month'] = df['timecreated'].dt.to_period('M')
df['hour'] = df['timecreated'].dt.hour


# Funciones de visualización
def total_ingresos(df):
    return df.shape[0]


def ingresos_por_departamento(df):
    return df.groupby('department').size().reset_index(name='total')


def ingresos_por_profesor(df):
    return df.groupby('roleteacher').size().reset_index(name='total')


def grafico_torta(data, labels_col, values_col):
    fig, ax = plt.subplots(figsize=(16, 16))  # Cambia el tamaño aquí
    ax.pie(data[values_col], labels=data[labels_col], autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  
    return fig



def ingresos_por_tiempo(df, periodo):
    return df.groupby(periodo).size().reset_index(name='total')


def heatmap_por_horas(df):
    df_grouped = df.groupby(['hour', 'department']).size().reset_index(name='total')
    heatmap_data = df_grouped.pivot_table(
        values='total',
        index='hour',
        columns='department',
        aggfunc='sum',
        fill_value=0
    )
    fig, ax = plt.subplots(figsize=(13, 8))
    sns.heatmap(heatmap_data, annot=True, fmt='d', cmap='YlGnBu', ax=ax)
    ax.set_title("Heatmap de Ingresos por Hora")
    return fig


# Aplicación Streamlit
def app():
    st.title("Dashboard de Ingresos de Eventos")

    menu = ["Datos Generales", "Datos por Departamento", "Datos por Profesor"]
    choice = st.sidebar.selectbox("Selecciona una categoría", menu)

    if choice == "Datos Generales":
        st.header("Resumen General")

        st.subheader("Total de Ingresos")
        st.metric(label="Ingresos totales", value=total_ingresos(df))

        st.subheader("Ingresos por Departamento")
        dept_data = ingresos_por_departamento(df)
        st.subheader("Ingresos por Departamento")
        dept_data = ingresos_por_departamento(df)

        fig, ax = plt.subplots(figsize=(12, 6))  # Ajusta el tamaño del gráfico
        ax.bar(dept_data['department'], dept_data['total'], color='skyblue')
        ax.set_xlabel('Departamento')
        ax.set_ylabel('Total de Ingresos')
        ax.set_title('Ingresos por Departamento')
        plt.xticks(rotation=45, ha='right')  # Rota etiquetas para que se vean

        st.pyplot(fig)

        st.subheader("Gráfico de Torta - Departamentos")
        st.pyplot(grafico_torta(dept_data, 'department', 'total'))

        st.subheader("Ingresos por Día")
        dia_data = ingresos_por_tiempo(df, 'day')
        st.line_chart(dia_data.set_index('day'))

        st.subheader("Ingresos por Semana")
        semana_data = ingresos_por_tiempo(df, 'week')
        st.line_chart(semana_data.set_index('week'))

        st.subheader("Ingresos por Mes")
        mes_data = ingresos_por_tiempo(df, 'month')
        st.line_chart(mes_data.set_index('month'))

        st.subheader("Ingresos por Hora")
        hora_data = ingresos_por_tiempo(df, 'hour')
        st.bar_chart(hora_data.set_index('hour'))

        st.subheader("Heatmap de Ingresos por Hora y Departamento")
        st.pyplot(heatmap_por_horas(df))

    elif choice == "Datos por Departamento":
        st.header("Datos por Departamento")
        departamentos = df['department'].dropna().unique()
        selected_depto = st.selectbox("Selecciona un Departamento", sorted(departamentos))

        df_depto = df[df['department'] == selected_depto]

        st.subheader("Total por Profesor")
        prof_data = ingresos_por_profesor(df_depto)
        st.bar_chart(prof_data.set_index('roleteacher'))

        st.subheader("Gráfico de Torta - Profesores")
        st.pyplot(grafico_torta(prof_data, 'roleteacher', 'total'))

        st.subheader("Ingresos por Día")
        st.line_chart(ingresos_por_tiempo(df_depto, 'day').set_index('day'))

        st.subheader("Ingresos por Semana")
        st.line_chart(ingresos_por_tiempo(df_depto, 'week').set_index('week'))

        st.subheader("Ingresos por Mes")
        st.line_chart(ingresos_por_tiempo(df_depto, 'month').set_index('month'))

        st.subheader("Ingresos por Hora")
        st.bar_chart(ingresos_por_tiempo(df_depto, 'hour').set_index('hour'))

        st.subheader("Heatmap de Ingresos por Hora y Departamento")
        st.pyplot(heatmap_por_horas(df_depto))

    elif choice == "Datos por Profesor":
        st.header("Datos por Profesor")
        profesores = df['roleteacher'].dropna().unique()
        selected_prof = st.selectbox("Selecciona un Profesor", sorted(profesores))

        df_prof = df[df['roleteacher'] == selected_prof]

        st.subheader("Total de Ingresos")
        total_prof = total_ingresos(df_prof)
        st.metric(label=f"Ingresos de {selected_prof}", value=total_prof)

        st.subheader("Ingresos por Día")
        st.line_chart(ingresos_por_tiempo(df_prof, 'day').set_index('day'))

        st.subheader("Ingresos por Semana")
        st.line_chart(ingresos_por_tiempo(df_prof, 'week').set_index('week'))

        st.subheader("Ingresos por Mes")
        st.line_chart(ingresos_por_tiempo(df_prof, 'month').set_index('month'))

        st.subheader("Ingresos por Hora")
        st.bar_chart(ingresos_por_tiempo(df_prof, 'hour').set_index('hour'))

        st.subheader("Heatmap de Ingresos por Hora y Departamento")
        st.pyplot(heatmap_por_horas(df_prof))


if __name__ == "__main__":
    app()
