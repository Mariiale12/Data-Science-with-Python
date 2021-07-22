#!/usr/bin/env python
# coding: utf-8

# # Listado de Ejercicios a realizar

# ## 1. Sin usar el computador, evalúe las siguientes expresiones, y para cada una de ellas indique el resultado y su tipo (si la expresión es válida) o qué error ocurre:
# 
# ### Ejemplo
# - 2 + 3      # Respuesta: tipo int, valor 5
# - 4 / 0      # Respuesta: error de división por cero
# 
# ### Ejercicio
# 
# - 5 + 3 * 4 / Tipo -> entero / Resultado -> 17
# - '5' + '3' * 2 / Tipo -> string / Resultado -> 533
# - 2 ** 11 == 1000 or 2 ** 9 == 100 / Tipo -> booleano / Resultado -> FALSE
# - int("cincuenta") # Error está asignando a un objeto tipo entero un objeto tipo caracter
# - 16/16 + 384/24 / Tipo -> float / Resultado -> 17
# - 600 + 18% / Tipo -> float / Resultado -> 600.18
# - 0 < (4096 % 10) < 6 / Tipo -> booleano / Resultado -> False
# - 'Max' + 'Min' / Tipo -> string / Resultado -> 'MaxMin'
# - ABC() * DEF() # Error 
# - float(-int('7') + int('90')) / Tipo -> float / Resultado -> 83 # función de conversión de formato
# - abs(len('seis') - len('tres')) # Aqui lo que hace es que resta la cantidad de caracteres que tiene 'seis' (en este caso serian cuatro, porque tiene cuatro letras) y la cantidad de caracteres del string 'tres' (en este caso serian cuatro tambien) entonces 4-4 = 0
# - bool(1210) or bool(-3465) / Tipo -> booleano / Resultado -> True
# - float(str(int('8' * 3) / 3)[3]) # Error no se puede convertir un objeto tipo string a float

# # 2. Imprima su nombre y fecha
# - Imprime: Jorge Alvarez - 20-04-2020

# In[1]:


# Respuesta:
print("María Alejandra Millán - 19/ 07/ 2021")


# # 3. Solicite un nombre y que el programa salude
# ### Ejemplo:
# - ingreso: 'Andres'
# - imprime: 'Hola Andres'

# In[2]:


print('¿Cómo te llamas?')


# In[3]:


Nombre = input()


# In[4]:


print('Es un placer conocerte, ' + Nombre)


# # 4. Solicite el radio (un numero) de un círculo e imprima como salida su diámetro, perímetro y su área
# ### Ejemplo
# - ingreso: 3 
# - imprime - Diametro: 6
# - imprime - Perimetro: 18.84
# - imprime - Area: 28.27

# In[5]:


# Respuesta:
print('Ingresa el radio del circulo')

Radio = float(input())


# In[6]:


Diametro = 2*Radio
Perimetro = 2*3.14*Radio
Area = 3.14*(Radio**2)


# In[7]:


print('El diametro del circulo es ' + str(Diametro))
print('El perimetro del circulo es ' + str(Perimetro))
print('El area del circulo es ' + str(Area))


# # 5. Solicite 6 notas y calcule el promedio de ellas
# ### Ejemplo
# - ingreso: 1 2 3 4 5 6
# - imprime: 3.5

# In[8]:


lasseis = []
for i in range(6):
    nota = float(input(" Escriba su nota "))
    lasseis.append(nota)
    mean = sum(lasseis)/len(lasseis)
print(mean)


# # 6. Solicite un valor e imprima que tipo de dato es
# ### Ejemplo
# - ingreso: 'A'
# - imprime: str
# - ingreso: 1
# - imprime: int

# In[9]:


# Respuesta:
valor = input( "Ingresa un valor ")
type(valor)


# # 7. Escriba en código la siguiente ecuación
# $$ \left(\frac{5+3}{3-2}\right)^2$$

# In[10]:


# Respuesta


# # 8. Solicite número de horas trabajadas y coste por horas e imprima el valor
# ### Ejemplo:
# - Ingreso: 4 (horas)
# - ingreso: 80.000 (precio x hora)
# - imprime: 320.000

# In[20]:


# Respuesta
horas = float(input("Cuantas horas trabajó? "))
precio = float(input("Cuanto vale una hora de trabajo? "))
print("Deben pagarle un total de: " + str(horas*precio))


# # 9. Solicite la temperatura en grados Celsius e imprima en grados Kelvin y Fahrenheit 
# ### Ejemplo:
# - ingreso: 38 (°C)
# - imprime: 311.15 °K
# - imprime: 100.4 °F

# In[27]:


# Respuesta
temperatura = float(input("Ingrese la temperatura en grados Celsius: "))
Kelvin = temperatura + 273.15
Fahrenheit = (temperatura * 9/5) + 32 
print("Es lo mismo que: " + str(Kelvin)+ " Kelvin y " + str(Fahrenheit) + " Fahrenheit" )


# # 10. Solicite 2 numeros e imprima si el segundo es mayor  
# ### Ejemplo:
# - ingreso: 2
# - ingreso: 3
# - impmrime: True

# In[31]:


# Respuesta
num1 = float(input(" Escriba un numero: "))
num2= float(input( " Escriba otro numero "))
if num2>num1:
    print("El segundo número es mayor")


# # 11. Solicite 2 numeros e imprima si el segundo es menor  
# ### Ejemplo:
# - ingreso: 2
# - ingreso: 3
# - impmrime: False

# In[33]:


# Respuesta
num3 = float(input(" Escriba un numero: "))
num4= float(input( " Escriba otro numero "))
if num4<num3:
    print("El segundo número es menor")


# # 12. Solicite una distancia (metros) y la velocidad (metros/segundos) e imprima el tiempo que se demora el recorrido
# ### Ejemplo:
# - ingreso: 150 (metros)
# - ingreso: 15 (metros/segundo)
# - Imprime: 10 segundos

# In[35]:


# Respuesta
distancia = float(input(" Escriba la distancia en metros "))
velocidad = float(input(" Escriba la velocidad en segundos por cada metro "))
print(" El tiempo que tarda en el recorrido es de: " + str(distancia/velocidad))


# # 13. Solicite al usuario tres valores y escriba en código la siguiente ecuación
# $$ \left(\frac{a+b}{c}\right) ^2 + \left(\frac{a-b}{c}\right) ^ 2 $$

# In[53]:


# Respuesta
nom1 = float(input(" Digite el valor de a "))
nom2 = float(input(" Digite el valor de b "))
nom3 = float(input(" Digite el valor de c "))
operacion = ((nom1+nom2)/nom3)**2 + ((nom1-nom2)/nom3)**2
print(operacion)


# # 14. Investigue como se saca la raíz cuadrada de un número en Python y escriba la solución en el cuadro de abajo

# In[52]:


# Respuesta
numero = float(input(" Escriba el numero al que desea sacarle raiz cuadrada "))

print("La raiz cuadrada es " + str(numero**(1/2)))


# # 15.  Con lo anterior solicite 2 numeros (Cateto a y Cateto b) e imprima la hipotenusa.
# ### Ejemplo:
# - ingreso: 3 (Cateto a)
# - ingreso: 4 (Cateto b)
# - imprime: Hipotenusa = 5

# In[60]:


# Respuesta
catetoa = float(input( " Ingrese el valor del cateto a: "))
catetob = float(input( " Ingrese el valor del cateto b: "))
hipotenusa = (catetoa**2 + catetob**2)**(1/2) 
print(" La hipotenusa es : " + str(hipotenusa))


# In[ ]:




