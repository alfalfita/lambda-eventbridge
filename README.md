# lambda-eventbridge
Queremos iniciar y detener las instancias EC2 en función de las etiquetas (tags) para ahorrar costos de hasta un 70% en instancias que solo son necesarias durante el horario laboral (LUN-VIE de 9 am a 6 pm) (utilización semanal reducida de 168 horas a ~50 horas).

Para lograr vamos a hacer uso de funciones lambda para programarlo en función de las horas de trabajo.

