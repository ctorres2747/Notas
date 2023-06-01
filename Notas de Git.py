#Configuración de Git

'''Nos paramos en la carpeta que queremos crear el repositorio 
#git config --global user.name "aqui va el nombre de usuario" (si ya está creado devuelve el nombre)
#git config --global user.email "aqui va el correo del usuario'''

#Para crear una carpeta nueva en la terminal
'''git mkdir "aqui va el nombre de la carpeta'''

#Funciones de Git
'''
git init   -> crea el repositorio en la carpeta
git status   -> me da el status de los ficheros que están aderidos y los que no
git add ____  -> en el espacio va el nommbre del fichero que debemos añadir al control de versiones
git commit -m "aquí va un comentario"  -> crea una foto de las modificaciones hechas hasta ese momento se debe añadir un comentario
git log    -> devuelve las fotos realizadas y el usuario que las ejecutó
git checkout _____ -> en el espacio va el nombre del fichero que queremos devolver a la commit anterior
git log --graph --pretty --oneline   -> mejora y resupe el aspecto del log
git config --global alias.____ "log --graph --pretty --oneline"   -> crea un alias para resumir la instrucción y le llama ___
git diff   -> informa los cambios del fichero con respecto al último commit
git reset --hard ____   -> en el espacio se pone el ID del commit a donde me quiero devolver
git reset --hard
git reflog   -> devuelve el historial completo de los commit que hemos hecho
git tag ____  -> en el espacio en blanco el nombre del tag (todo en miniscula) es una marca importante en el proyecto
git tag   -> devuelve la lista de tags que tenemos 
git checkout tags/(nombre del tag)    -> devuelve la cabeza al tag seleccionado
git branch ____  -> en el espacio en blanco se pone el nombre de la nueva rama que queremos crear
git switch _____   _> en el espacio se pone el nombre de la rama para cambiar 

probando Github hola Cristhian 

'''