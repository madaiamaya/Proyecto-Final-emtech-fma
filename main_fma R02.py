from types import SimpleNamespace
from typing import DefaultDict
from lifestore_file import lifestore_products, lifestore_sales, lifestore_searches
"""
This is the LifeStore_SalesList data:

lifestore_searches = [id_search, id product]
lifestore_sales = [id_sale, id_product, score (from 1 to 5), date, refund (1 for true or 0 to false)]
lifestore_products = [id_product, name, price, category, stock]
"""

#---------------------------------------- INICIO DEL CODIGO -----------------------------------------------#
'''
Lo primero que hare sera descartar los productos devueltos, ya que estos no deben ser tomados en cuenta para
analisis. 

Para esto creare una nueva sublista de sales sin ellos. primero creando una lista vacia, despues con un bucle
for almaceno en esta lista vacia los productos que no hayan sido devueltos.

Posteriormente con un nuevo bucle for auxiliara para contabilizar cuantas ventas hubo de cada producto.

Se puede usar el mismo codigo que se uso para contar cada producto para buscar cuantas veces se busco cada
producto, solo se haran lso ajustes cambiand olos nombres de las variables y/o listas necesarios.

nuevas listas:
venta_por_producto=cantidad de ventas que tuvo cada producto
busqueda_por_producto=cantidad de busquedas que tuvo cada producto


'''
venta_sin_devolucion=[]

for refund in lifestore_sales:
    if refund[-1]==0:
        venta_sin_devolucion.append(refund)


cant_prod=len(lifestore_products)
venta_por_producto=[]
busqueda_por_producto=[]
score_por_producto=[]

for id in range(cant_prod):
    verdadero_id = id + 1
    renglon = [verdadero_id, 0]
    renglon1= [verdadero_id, 0]
    renglon2=[verdadero_id, 0]
    venta_por_producto.append(renglon)
    busqueda_por_producto.append(renglon1)
    score_por_producto.append(renglon2)

for srch in lifestore_searches:
    id_product_seacrh=srch[1]
    busqueda_por_producto[id_product_seacrh-1][1]=busqueda_por_producto[id_product_seacrh-1][1]+1


# Como mi id_producto esta en primera posicion si quiero ordenar la lista por su segundo elemento
# defino la key que me permite hacer esto.

def usesecond(elemento):
    return elemento[1]
busqueda_por_producto.sort(key=usesecond,reverse=True)

top_search_por_producto=busqueda_por_producto[:10]
low_search_por_producto=busqueda_por_producto[-10:]


for venta in venta_sin_devolucion:
    id_prod= venta[1]
    venta_por_producto[id_prod-1][1]=venta_por_producto[id_prod-1][1]+1
    id_score=venta[1]
    if venta_por_producto[id_prod-1][1]==1:
        score_por_producto[id_score-1][1]=venta[2]/venta_por_producto[id_prod-1][1]
    if venta_por_producto[id_prod-1][1]!=1:
        score_por_producto[id_score-1][1]=venta[2]+venta[2]/venta_por_producto[id_prod-1][1]

score_por_producto.sort(key=usesecond,reverse=True)
score_sin_ceros=[]

for null in score_por_producto:
    if null[1]!=0:
        score_sin_ceros.append(null)

productos_no_vendidos=[]
productos_vendidos=[]



for product in venta_por_producto:
    if product[1]==0:
        productos_no_vendidos.append(product)
    else:
        productos_vendidos.append(product)

productos_vendidos.sort(key=usesecond,reverse=True)

# print(score_sin_ceros)
# print(venta_por_producto)

# print(len(productos_vendidos))
# print(len(productos_no_vendidos))

#-----------------------------   FIN DE SECCION    ------------------------------------------#

#-----------------------------   INICIO DE SECCION    ------------------------------------------#

'''
VENTAS POR MES

Para encontrar las ventas por mes se crearon listas vacias para cada mes del año. despues con un bucle for
se encontro y almaceno cada venta en ela variable con el mes deseado y se uso el comando len para obtener
la cantidad

nuevas listas:

mes= registro completo de la venta ese mes
ventas_mes= cantidad de ventas ese mes
ingresos_mes= suma de las ventas de cada producto(ingreso total ($))

'''
meses = ['/01/', '/02/','/03/','/04/','/05/', '/06/', '/07/', '/08/', '/09/', '/10/', '/11/', '/12/']
meses2=['Enero','Febrero','Marzo','Abril','Mayo,','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']
enero=[]
feb=[]
marz=[]
abr=[]
mayo=[]
jun=[]
jul=[]
ago=[]
sep=[]
oct=[]
nov=[]
dic=[]

for venta in venta_sin_devolucion:
    fecha_de_venta=venta[3]
    if meses[0] in fecha_de_venta:
        enero.append(venta)
        ventas_ene=len(enero)
    if meses[1] in fecha_de_venta:
        feb.append(venta)
        ventas_feb=len(feb)
    if meses[2] in fecha_de_venta:
        marz.append(venta)
        ventas_marz=len(marz)
    if meses[3] in fecha_de_venta:
        abr.append(venta)
        ventas_abr=len(abr)
    if meses[4] in fecha_de_venta:
        mayo.append(venta)
        ventas_may=len(mayo)
    if meses[5] in fecha_de_venta:
        jun.append(venta)
        ventas_jun=len(jun)
    if meses[6] in fecha_de_venta:
        jul.append(venta)
        ventas_jul=len(jul)
    if meses[7] in fecha_de_venta:
        ago.append(venta)
        ventas_ago=len(ago)
    if meses[8] in fecha_de_venta:
        sep.append(venta)
        ventas_sep=len(sep)
    if meses[9] in fecha_de_venta:
        oct.append(venta)
        ventas_oct=len(oct)
    if meses[10] in fecha_de_venta:
        nov.append(venta)
        ventas_nov=len(nov)
    if meses[11] in fecha_de_venta:
        dic.append(venta)
        ventas_dic=len(dic)

precio_por_producto=[]

for price in lifestore_products:
    precio=[price[0],price[2]]
    precio_por_producto.append(precio)
# print(precio_por_producto)

id_enero=[]
ingresos_enero=[]
id_feb=[]
ingresos_feb=[]
id_marz=[]
ingresos_marz=[]
id_abr=[]
ingresos_abr=[]
id_may=[]
ingresos_may=[]
id_jun=[]
ingresos_jun=[]
id_jul=[]
ingresos_jul=[]
id_ago=[]
ingresos_ago=[]
id_sep=[]
ingresos_sep=[]
id_oct=[]
ingresos_oct=[]
id_nov=[]
ingresos_nov=[]
id_dic=[]
ingresos_dic=[]
'''
No encontre otra manera de unir el precio de cada producto a su id_prodcut en la lista que cree para cada mes
asi que lo qeu hice fue hacer una lista con solo los precios cada uno en la posicion correspondiente para el 
id_produt que le corresponde. despues con un bucle for cree una lista con solo los id_product que se vendieron
ese mes. despues con otro bucle for y condicionales if a cada id_product se le asigno el precio que correspondia
y con el comando sum se obtendria el total de ingresos por mes. asi se podria crear una nueva lista con el mes y
el ingreso obtenido para es mes.

'''
for product1 in enero:
    id_enero.append(product1[1])
for precio1 in id_enero:
    precio_id=precio_por_producto[precio1]
    ingresos_enero.append(precio_id[1])
ingresos_enero=sum(ingresos_enero)

for product1 in feb:
    id_feb.append(product1[1])
for precio1 in id_feb:
    precio_id=precio_por_producto[precio1]
    ingresos_feb.append(precio_id[1])
ingresos_feb=sum(ingresos_feb)

for product1 in marz:
    id_marz.append(product1[1])
for precio1 in id_marz:
    precio_id=precio_por_producto[precio1]
    ingresos_marz.append(precio_id[1])
ingresos_marz=sum(ingresos_marz)

for product1 in abr:
    id_abr.append(product1[1])
for precio1 in id_abr:
    precio_id=precio_por_producto[precio1]
    ingresos_abr.append(precio_id[1])
ingresos_abr=sum(ingresos_abr)

for product1 in mayo:
    id_may.append(product1[1])
for precio1 in id_may:
    precio_id=precio_por_producto[precio1]
    ingresos_may.append(precio_id[1])
ingresos_may=sum(ingresos_may)

for product1 in jun:
    id_jun.append(product1[1])
for precio1 in id_jun:
    precio_id=precio_por_producto[precio1]
    ingresos_jun.append(precio_id[1])
ingresos_jun=sum(ingresos_jun)

for product1 in jul:
    id_jul.append(product1[1])
for precio1 in id_jul:
    precio_id=precio_por_producto[precio1]
    ingresos_jul.append(precio_id[1])
ingresos_jul=sum(ingresos_jul)

for product1 in ago:
    id_ago.append(product1[1])
for precio1 in id_ago:
    precio_id=precio_por_producto[precio1]
    ingresos_ago.append(precio_id[1])
ingresos_ago=sum(ingresos_ago)

for product1 in sep:
    id_sep.append(product1[1])
for precio1 in id_sep:
    precio_id=precio_por_producto[precio1]
    ingresos_sep.append(precio_id[1])
ingresos_sep=sum(ingresos_sep)

for product1 in oct:
    id_oct.append(product1[1])
for precio1 in id_oct:
    precio_id=precio_por_producto[precio1]
    ingresos_oct.append(precio_id[1])
ingresos_oct=sum(ingresos_oct)

for product1 in nov:
    id_nov.append(product1[1])
for precio1 in id_nov:
    precio_id=precio_por_producto[precio1]
    ingresos_nov.append(precio_id[1])
ingresos_nov=sum(ingresos_nov)

for product1 in dic:
    id_dic.append(product1[1])
for precio1 in id_dic:
    precio_id=precio_por_producto[precio1]
    ingresos_dic.append(precio_id[1])
ingresos_dic=sum(ingresos_dic)

ingresos_mensuales=[[meses2[0],ingresos_enero],[meses2[1],ingresos_feb],[meses2[2],ingresos_marz],[meses2[3],ingresos_abr],
[meses2[4],ingresos_may],[meses2[5],ingresos_jun],[meses2[6],ingresos_jul],[meses2[7],ingresos_ago],[meses2[8],ingresos_sep],
[meses2[-3],ingresos_oct],[meses2[-2],ingresos_nov],[meses2[-1],ingresos_dic],]

ingreso_anual=ingresos_enero+ingresos_feb+ingresos_marz+ingresos_abr+ingresos_may+ingresos_jun+ingresos_jul+ingresos_ago+ingresos_sep
+ingresos_oct+ingresos_nov+ingresos_dic

#-----------------------------   FIN DE SECCION    ------------------------------------------#

#-----------------------------   INICIO DE SECCION    ------------------------------------------#

'''
CATEGORIAS

Para buscar que categorias existian hice una lista imprimiendo la cuarta columna de lifestore_products.

Despues creare listas vacias con cada nombre de categoria para depsues con un bucle for alamcenar que produtos 
pertenecen a esa categoria y asi poder clasificar las ventas y busquedas por categoria.
'''

for categoria in lifestore_products:
    categorias=categoria[3]
    #print(categorias)
# categorias: procesadores, tarjetas de video, tarjetas madre, discos duros, memorias usb, pantallas, bocinas,audifonos

procesador=[]
tarjeta_video=[]
tarjeta_madre=[]
disco_duro=[]
usb=[]
pantallas=[]
bocinas=[]
audifonos=[]
lista_de_productos=[]


for category in lifestore_products:
    if category[3]=='procesadores':
        procesador.append(category[0])
    elif category[3]=='tarjetas de video':
        tarjeta_video.append(category[0])
    elif category[3]=='tarjetas madre':
        tarjeta_madre.append(category[0])
    elif category[3]=='discos duros':
        disco_duro.append(category[0])
    elif category[3]=='memorias usb':
        usb.append(category[0])
    elif category[3]=='pantallas':
        pantallas.append(category[0])
    elif category[3]=='bocinas':
        bocinas.append(category[0])
    elif category[3]=='audifonos':
        audifonos.append(category[0])
    lista_de_productos.append(category[0])

#-----------------------------   FIN DE SECCION    ------------------------------------------#

#-----------------------------   INICIO DE SECCION    ------------------------------------------#
'''
VENTAS POR CATEGORIA

Para encontrar las ventas por categoria cree listas vacias con cada categoria. despues con un bucle for
almacene en cada lista las ventas y con el comando len conte cuantas veces se vendio cada categoria.

listas:
sale_categoria= venta de cada producto por categoria
cant_ventas_categoria= cantidad de ventas por categoria

'''

sale_procesador=[]
sale_tarjeta_video=[]
sale_tarjeta_madre=[]
sale_disco_duro=[]
sale_usb=[]
sale_pantallas=[]
sale_bocinas=[]
sale_audifonos=[]
cant_ventas_procesador=[]
cant_ventas_tarjeta_video=[]
cant_ventas_tarjeta_madre=[]
cant_ventas_disco_duro=[]
cant_ventas_usb=[]
cant_ventas_pantallas=[]
cant_ventas_bocinas=[]
cant_ventas_audifonos=[]

for sale in venta_por_producto:
    if sale[0] in procesador:
        sale_procesador.append(sale)
        sale_procesador.sort(key=usesecond,reverse=True)
    elif sale[0] in tarjeta_video:
        sale_tarjeta_video.append(sale)
        sale_tarjeta_video.sort(key=usesecond,reverse=True)
    elif sale[0] in tarjeta_madre:
        sale_tarjeta_madre.append(sale)
        sale_tarjeta_madre.sort(key=usesecond,reverse=True)
    elif sale[0] in disco_duro:
        sale_disco_duro.append(sale)
        sale_disco_duro.sort(key=usesecond,reverse=True)
    elif sale[0] in usb:
        sale_usb.append(sale)
        sale_usb.sort(key=usesecond,reverse=True)
    elif sale[0] in pantallas:
        sale_pantallas.append(sale)
        sale_pantallas.sort(key=usesecond,reverse=True)
    elif sale[0] in bocinas:
        sale_bocinas.append(sale)
        sale_bocinas.sort(key=usesecond,reverse=True)
    elif sale[0] in audifonos:
        sale_audifonos.append(sale)
        sale_audifonos.sort(key=usesecond,reverse=True)

for i in sale_procesador:
    cant_ventas_procesador.append(i[1])
cant_ventas_procesador=sum(cant_ventas_procesador)

for i in sale_tarjeta_video:
    cant_ventas_tarjeta_video.append(i[1])
cant_ventas_tarjeta_video=sum(cant_ventas_tarjeta_video)

for i in sale_tarjeta_madre:
    cant_ventas_tarjeta_madre.append(i[1])
cant_ventas_tarjeta_madre=sum(cant_ventas_tarjeta_madre)

for i in sale_disco_duro:
    cant_ventas_disco_duro.append(i[1])
cant_ventas_disco_duro=sum(cant_ventas_disco_duro)

for i in sale_usb:
    cant_ventas_usb.append(i[1])
cant_ventas_usb=sum(cant_ventas_usb)

for i in sale_pantallas:
    cant_ventas_pantallas.append(i[1])
cant_ventas_pantallas=sum(cant_ventas_pantallas)

for i in sale_bocinas:
    cant_ventas_bocinas.append(i[1])
cant_ventas_bocinas=sum(cant_ventas_bocinas)

for i in sale_audifonos:
    cant_ventas_audifonos.append(i[1])
cant_ventas_audifonos=sum(cant_ventas_audifonos)

ventas_por_categoria=[['Procesador',cant_ventas_procesador],['Tarjetas de video',cant_ventas_tarjeta_video],['Tarjetas Madre',cant_ventas_tarjeta_madre],['Discos Duros',cant_ventas_disco_duro],
['Memorias USB',cant_ventas_usb],['Pantallas',cant_ventas_pantallas],['Bocinas',cant_ventas_bocinas],['Audifonos',cant_ventas_audifonos]]

# ventas_por_categoria.sort(key=usesecond,reverse=True)
# for ventacateg in ventas_por_categoria:
#     print(ventacateg)

#-----------------------------   FIN DE SECCION    ------------------------------------------#

#-----------------------------   INICIO DE SECCION    ------------------------------------------#
'''
BUSQUEDAS POR CATEGORIA

Para encontrar las ventas por categoria cree listas vacias con cada categoria. despues con un bucle for
y comandos if aisle cada busqeuda en su categoria corresponidente usando la lisat creada de busqeudas por
producto.

srch_categoria= busquedas totales de procutos por categoria

'''
srch_procesador=[]
srch_tarjeta_video=[]
srch_tarjeta_madre=[]
srch_disco_duro=[]
srch_usb=[]
srch_pantallas=[]
srch_bocinas=[]
srch_audifonos=[]

for search in busqueda_por_producto:
    if search[0] in procesador:
        srch_procesador.append(search)
        srch_procesador.sort(key=usesecond,reverse=True)
    elif search[0] in tarjeta_video:
        srch_tarjeta_video.append(search)
        srch_tarjeta_video.sort(key=usesecond,reverse=True)
    elif search[0] in tarjeta_madre:
        srch_tarjeta_madre.append(search)
        srch_tarjeta_madre.sort(key=usesecond,reverse=True)
    elif search[0] in disco_duro:
        srch_disco_duro.append(search)
        srch_disco_duro.sort(key=usesecond,reverse=True)
    elif search[0] in usb:
        srch_usb.append(search)
        srch_usb.sort(key=usesecond,reverse=True)
    elif search[0] in pantallas:
        srch_pantallas.append(search)
        srch_pantallas.sort(key=usesecond,reverse=True)
    elif search[0] in bocinas:
        srch_bocinas.append(search)
        srch_bocinas.sort(key=usesecond,reverse=True)
    elif search[0] in audifonos:
        srch_audifonos.append(search)
        srch_audifonos.sort(key=usesecond,reverse=True) 

low_sale_procesador=sale_procesador[-5:]
low_srch_procesador=srch_procesador[-10:]

low_sale_tarjeta_video=sale_tarjeta_video[-5:]
low_srch_tarjeta_video=srch_tarjeta_video[-10:]

low_sale_tarjeta_madre=sale_tarjeta_madre[-5:]
low_srch_tarjeta_madre=srch_tarjeta_madre[-10:]

low_sale_disco_duro=sale_disco_duro[-5:]
low_srch_disco_duro=srch_disco_duro[-10:]

low_sale_usb=sale_usb[-5:]
low_srch_usb=srch_usb[-10:]

low_sale_pantallas=sale_pantallas[-5:]
low_srch_pantallas=srch_pantallas[-10:]

low_sale_bocinas=sale_bocinas[-5:]
low_srch_bocinas=srch_bocinas[-10:]

low_sale_audifonos=sale_audifonos[-5:]
low_srch_audifonos=srch_audifonos[-10:]

#-----------------------------   FIN DE SECCION    ------------------------------------------#

#----------------------- INICIO DE SECCION: INTERACCION CON USUARIO -------------------------------#
'''
LOG-IN DEL USUARIO ADMINISTRADOR

PRIMERO CREE UN INPUT PARA QEU EL USUARIO DECIDIREA SI QUIERE ENTRAR O NO (ESTA ES UNA VARIABLE QUE DETENDRIA
O NO EL BUCLE) DEPUES CON UN IF en aso de que el usuario dicidiese entrar o no coemnzara el bucle while
mientras el usuario no ponga la contraseña correcta y decida seguir intentando el bucle no se quierba. sin embargo,
este solo cuenta con 3 intentos condicionados con un operador de asignacion en dodne cada iteracion este va
sumando un intento.

credenciales:  usuario: admin01 y contraseña: 1234
'''
limpiarPantalla = '\n' * 10
print(limpiarPantalla)

ingreso=input('Desea ingresar a su cuenta? si/no: ')
intentos=1

if ingreso=='no':
  print('Que tenga un buen dia')
elif ingreso=='si':
  while ingreso=='si':
        usuario=input('Ingrese su ID de empleado: ')
        contraseña=input('Ingrese su contraseña: ')
        if usuario!='admin01' or contraseña!='1234':
            print('Usuario o contraseña incorrecto')
            ingreso=input('Desea intentar entrar a su cuenta de nuevo? si/no: ')
            intentos+=1
        elif usuario=='admin01' or contraseña=='1234':          
            print(f'''

          Acceso concedido.
          Bienvenido {usuario}
          


          ''')
            break
        if intentos>2:
            print('''


        Excediste el numero de intentos, por favor, intenta de nuevo en 15 minutos.

        ''')
            break
else:
    print('''
    
    Input invalido, vuelve a intentarlo
    
    ''')

#-----------------------------   FIN DE SECCION    ------------------------------------------#

#-----------------------   INICIO DE SECCION:DESPLIEGUE DE INFO  ----------------------------#


top_productos_vendidos=productos_vendidos[:5]
low_productos_vendidos=productos_vendidos[-5:]

top_scores=score_sin_ceros[:5]
low_scores=score_sin_ceros[-5:]

# MENU DE INICIO

visualizar=input('''

Que informacion desea visualizar?

1.- Ventas por producto
2.- Ventas por categoria
3.- Busquedas de producto
4.- Score de productos
5.- Ingresos de la tienda
                                
                                >>''')
print(limpiarPantalla)

if visualizar=='1':
    ver=input('''
    
    Seleccione la lista deseada:

    1.- Top 5 productos mas vendidos
    2.- Top 5 productos mas rezagados 
    
                                >>''')
    if ver=='1':
        print('''
        Top 5 productos mas vendidos
        ''')
        for top in top_productos_vendidos:
            print(top)
    if ver=='2':
        print('''
        Top 5 productos mas rezagados
        ''')
        for low in low_productos_vendidos:
            print(low)
if visualizar=='2':
    ver=input('''
    
    Seleccione la categoria deseada:

    1.-Procesadores
    2.-Tarjetas de Video
    3.-Tarjetas Madre
    4.-Disco Duro
    5.-Memorias USB
    6.-Pantallas
    7.-Bocinas
    8.-Audifonos 
    
                                >>''')
    if ver=='1':
        print('''

        ----Procesadores---

        Top 5 procesadores menos vendidos:
        ''')
        for low in low_sale_procesador:
            print(low)

        print('''
        Top 10 procesadores menos buscados
        ''')
        for lowsrch in low_srch_procesador:
            print(lowsrch)
    if ver=='2':
        print('''

        ---Tarjetas de Video---

        Top 5 tarjetas de video menos vendidas:
        ''')
        for low in low_sale_tarjeta_video:
            print(low)

        print('''
        Top 10 tarjetas de video menos buscadas
        ''')
        for lowsrch in low_srch_tarjeta_video:
            print(lowsrch)
    if ver=='3':
        print('''

        ---Tarjetas Madre---

        Top 5 tarjetas madre menos vendidas:
        ''')
        for low in low_sale_tarjeta_madre:
            print(low)

        print('''
        Top 10 tarjetas madre menos buscadas
        ''')
        for lowsrch in low_srch_tarjeta_madre:
            print(lowsrch)
    if ver=='4':
        print('''

        ---Disco Duro---

        Top 5 discos duros menos vendidos:
        ''')
        for low in low_sale_disco_duro:
            print(low)
        
        print('''
        Top 10 discos duros menos buscados
        ''')
        for lowsrch in low_srch_disco_duro:
            print(lowsrch)
    if ver=='5':
        print('''

        ---Memorias USB---

        Top 5 memorias usb menos vendidas:
        ''')
        for low in low_sale_usb:
            print(low)

        print('''
        Top 10 memorias usb menos buscadas
        ''')
        for lowsrch in low_srch_usb:
            print(lowsrch)
    if ver=='6':
        print('''

        ---Pantallas---

        Top 5 pantallas menos vendidas:
        ''')
        for low in low_sale_pantallas:
            print(low)

        print('''
        Top 10 pantallas menos buscadas
        ''')
        for lowsrch in low_srch_pantallas:
            print(lowsrch)
    if ver=='7':
        print('''

        ---Bocinas---

        Top 5 bocinas menos vendidas:
        ''')
        for low in low_sale_bocinas:
            print(low)

        print('''
        Top 10 bocinas menos buscadas
        ''')
        for lowsrch in low_srch_bocinas:
            print(lowsrch)
    if ver=='8':
        print('''

        ---Audifonos---

        Top 5 audifonos menos vendidos:
        ''')
        for low in low_sale_audifonos:
            print(low)

        print('''
        Top 10 audifonos menos buscados
        ''')
        for lowsrch in low_srch_audifonos:
            print(lowsrch)
if visualizar=='3':
    print('''
    Top 10 productos mas buscados
    ''')
    for topsearch in top_search_por_producto:
        print(topsearch)

    print('''
    Top 10 productos menos buscados
    ''')
    for lowsearch in low_search_por_producto:
        print(lowsearch)
if visualizar=='4':
    print('''
    Top 5 productos con mejor score
    ''')
    for top in top_scores:
        print(top)

    print('''
    Top 5 productos con menor score
    ''')
    for low in low_scores:
        print(low)
if visualizar=='5':
    print('''
    ---Ingresos Mensuales---
    ''')
    for mes in ingresos_mensuales:
        print(mes)

    print(f'''
    Ingreso Anual: {ingreso_anual}
    ''')