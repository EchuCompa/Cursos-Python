# hipoteca.py
# Archivo de ejemplo
# Ejercicio de hipoteca

saldo = 500000
tasa = 0.05
pago_mensual = 2684.11
total_pagado = 0
pago_extra_mes_comienzo = 60    
pago_extra_mes_fin = 108
pago_extra = 1000
mes = 0


print( "|| Mes ||", "||Total Pagado||", "||Saldo Restante||")

while saldo > 0:
    mes += 1
    saldo = saldo * (1+tasa/12) - pago_mensual
    total_pagado = total_pagado + pago_mensual
# Ejercicios 1.20 y 1.10    
#    print ( "|| ", mes, " || ||  ", round(total_pagado,1), "  || ||", round(saldo,1), "    ||")
#    print ( f"|| { mes}  || ||   {round(total_pagado,1)}  || || {round(saldo,1)}    ||") 

    # if saldo < pago_mensual :         Ejercicio 1.11
    #     saldo = 0               Lo que hace es fijarse cuándo llegó al último
    #     total_pagado += saldo   pago


    # if mes < pago_extra_mes_fin and mes > pago_extra_mes_comienzo :   Ejercicio 1.9
    #     saldo -= pago_extra
    #     total_pagado += pago_extra
        
    # if mes < 12:              Ejercicio 1.8
    #     saldo -= 1000
    #     total_pagado += 1000

print('Total pagado', round(total_pagado, 2))

# Ejercicio 1.12 bool("False") te devuelve True pues convierte cuál string no vacío a True.









