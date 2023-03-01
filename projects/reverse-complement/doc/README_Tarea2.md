# Jose Antonio Sanchez Villicana

## Git y GitHub
****
### Metodologia

#### Agregamos secuencia de araB, guardamos cambios
```
code sequence.faa
git add sequence.faa
git commit sequence.faa
```
#### Introducimos mutaciones y comparamos versiones
```
 code sequence.faa
 git add sequence.faa
 git commit sequence.faa
 git log --oneline
 git diff 989b121 902a0f8
 git diff 989b121 c1589bd
```
#### Restauramos a version sin mutaciones y comparamos versiones para asegurarnos de que son iguales
```
git checkout 902a0f8 sequence.faa
git status
git commit sequence.faa
git log --oneline
git diff f7b6e1c 902a0f8
```
#### Guardamos cambios en GitHub
```
git push origin master
```
****
### Resultados
![61c798d6d2907863d990bbbd979d5912.png](../_resources/61c798d6d2907863d990bbbd979d5912.png)
****
### Conclusiones
> Git te permite trabajar con archivos que cambian con el tiempo y gracias al comando diff podemos ver aexactamente los cambios en las versiones.
> Después además podemos restaurar un archivo que ha sufrido cambios a una versión anterior identificable gracias a los mensajes de cada commit, de ahí la importancia de agregarlos y que sean significativos.