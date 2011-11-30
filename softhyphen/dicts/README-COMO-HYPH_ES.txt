--- Nueva versión 0.6 ---

1. Dónde Descargar 
2. Cómo instalarlo
3. Cómo verificar la configuración de OOo
4. Cómo testear el separador silábico
5. Reglas de separación silábica
 
1. Dónde Descargar
https://sourceforge.net/projects/openoffice-es/
 
2. Cómo instalarlo
Ir a las siguentes carpetas:
-En Linux-
[OpenOffice.orgxx]\share\dict\ooo\
-En Windows-
c:\[OpenOffice.orgxx]\share\dict\ooo\
Si ya tienes instalado el antigúo HYPH tienes que renombrarlo por
seguridad:
hyph_es_ES.dic > hyph_es_ES2.dic
Copiar los archivos ya descomprimidos de hyph_es_ES.zip en la 
ubicación arriba mencionada.

3. Cómo verificar la configuración de OOo
Después de reiniciar el OOo, si es que lo tenía abierto, inclusive
si está en WIN32 reiniciar el iniciador rápido de OOo en la bandeja
del sistema. Abierto el OOo vaya al menú:
Herramientas -> Opciones -> Configuración del Idioma -> Lingüística 
Cuando haya llegado a "Lingüística" haga clic en "Editar"
En "Español(España)" seleccioe[x] "separador silábico" (AltLinux ...)
 
4. Cómo testear el separador silábico
Se me han ocurrido dos maneras:
1.
 a. Abrir un documento largo.
 b. Verificar que la separación silábica esté activado para el texto
 (formato -> parrafo -> flujo de texto
 ó también en estilista ->  predeterminado -> flujo de texto).
 c. Pasear por el documento verificando si hay alguna separación mal
 hecha.
2.
 a. los mismo que 1.b.
 b. Reducir los márgenes a 3 o 4 centímetros.
 c. comenzar a ingresar palabras y forzar su separación silábica
 agregando espacios al comienzo de la palabra.
 
5. Reglas de separación silábica
(En OOo no separa una letra tanto a la izquierda como a la derecha: 
por ejemplo: no "á-baco" ni "Marí-a", y parece también ocurren algo 
parecido con las palabras de cuatro letras como "para" "foca" etc)
VOCALES
 * abiertas      "a"
 * semiabertas   "e,o"
 * cerradas      "i,y,u"
CONSONANTES
 * compuestas    "ch,ll,rr"
 * simples       "v,c,d,f,g,h,j,k,l,m,n,ñ,p,q,r,s,t,v,w,x,z"
REGLAS
1. 
En las sílabas, por lo menos, siempre tiene que haber una vocal. 
Sin vocal no hay sílaba.
2.
Cada elemento del grupo de consonantes inseparables no puede ser 
separado al dividir una palabra en sílaba:
"bl,br,ch,cl,cr,dr,fl,fr,gl,gr,kr,ll,pl,pr,rr,tr"
3.
Cuando una consonante se encuentra entre dos vocales, se une a la 
segunda vocal.
4.
Cuando hay dos consonantes entre dos vocales, cada vocal se une a una
consonante.
*Excepción: Esto no ocurre en el grupo de consonantes inseparables
(regla 2).
5.
Si son tres las consonantes colocadas entre dos vocales, las dos 
primeras consonantes se asociarán con la primera vocal y la tercer 
consonante con la segunda vocal.
*Excepción.- Esta regla no se cumple cuando la segunda y tercera 
consonante forman parte del grupo de consonantes inseparables.
6.
Las palabras que contienen una h precedida o seguida de otra 
consonante, se dividen separando ambas letras.
7.
El diptongo es la unión inseparable de dos vocales. Se pueden 
presentar tres tipos de diptongos posibles:
(abierta + cerrada)|(cerrada + abierta)|(cerrada + cerrada)
Son diptongos sólo las siguientes parejas de vocales:
"ai,au,ei,eu,io,ou,ia,ua,ie,ue,oi,uo,ui,iu,ay,ey,oy"
La unión de dos vocales abiertas o semiabiertas no forman diptongo,
es decir, deben separarse en la segmentación silábica. Pueden quedar
solas o unidas a una consonante.
8.
La h entre dos vocales, no destruye un diptongo.
9.
La acentuación sobre la vocal cerrada de un diptongo provoca su 
destrucción.
10.
La unión de tres vocales forma un triptongo. La única disposición
posible para la formación de triptongos es la que indica el esquema:
Vocal cerrada + (abierta | semiabierta) + cerrada
Sólo las siguientes combinaciones de vocales, forman un triptongo:
"iai,iei,uai,uei,uau,iau,uay,uey"