# Vue 3 + Vite

### Consultas

1. Que hacer con creador, creador es una vista de un usuario cliente que quiere hacer su rutina personalizada en la app. 
Permitir que vea la informacion de otros usuarios?
Dejar que pueda asignar rutinas a otros usuarios?
No deberia... pero la solucion que se me ocurre es agregar ifs en el template o vistas dependiendo que este logeado
Existe otra solucion mas generica?
Porque si el rol algun dia es cambiado o eliminado hay que ir al template y cambiar el codigo de los ifs... no me gusta esa solucion, esta buena pero solo para algunas cosas.

2. Los errores de la base de datos los controlo en el plugin de axios y envio la notificacion por el toad. Cuando un entrenador o creador NO tiene permisos para modificar o eliminar, los botones en las tablas suelen aparecer igual. Volvemos a lo mismo agregar ifs para que no se vea, pero prefiero una solucion que valide el rol que tiene y muestre ciertas acciones. 
Existe algun tipo de validator o podria hacer alguno manual? como seria la logica?

3. El mapeo de datos o filtros que se realizan en el frontend esta bien? intente que sea lo menos pesado posible y trayendo la menor cantidad de datos de la bd. Pero a veces en la inforoutine se hacian mucho, fue la parte que mas me costo, tuve que cambiar varias veces el modelo de la base de datos para poder llegar a un resultado final... no me termina de convencer pero esta ahi.

4. funciones a implementar en un futuro, compartir rutinas o copiar rutinas. Para que un entrenador no tenga que empezar una rutina desde 0 y pueda copiar una rutina similar y solo cambiar ciertos ejercicios.

5. Los ejercicios tienen series, repeticiones y pesos que son solo recomendado o informacion. Esos pesos se suelen mostrar como recomendacion en las rutinas, en TODAS las rutinas. Y en info routine se almacena las marcas personales de cada persona. Esta bien planteado?

6. Si borro una rutina en backend, deberia borrar en cascada todas las filas que tenga routine_id en info_routines?
