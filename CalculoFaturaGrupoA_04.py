#Calculo de faturao do Grupo - Mercado Livre

#Imagem da fatura
# Fatura_GrupoA_Calculo_02.jpg
# Fatura tipo = Mercado Livre

#Variaveis
#Consumo
MesFatura 				= 82022
ConsumoKwhPonta 		= 32279
ConsumoKwhFPonta 		= 281084
ConsumoReativoPonta 	= 22
ConsumoReativoFPonta 	= 395

ConsumoDemandaDISUltraTUSD 	= 165.80
ConsumoDemandaDISTUSD 		= 1055.80

Energia_ACL_Com_ICMS_P = 32279
Energia_ACL_Com_ICMS_F = 281084
Subsidio_Tarifa_Liquido=1.047888

#Tarifa
Tarifa_ConsumoKwhPonta 		= 0.597266
Tarifa_ConsumoKwhFPonta 	= 0.116158
Tarifa_ConsumoReativoPonta 	= 0.330455
Tarifa_ConsumoReativoFPonta = 0.330886

Tarifa_ConsumoDemandaDISUltraTUSD = 36.843727
Tarifa_ConsumoDemandaDISTUSD = 9.227335

Tarifa_Energia_ACL_Com_ICMS_P = 0.359439
Tarifa_Energia_ACL_Com_ICMS_F = 0.359439
Tarifa_Subsidio_Tarifa_Liquido= 24102.56



#Calculo
Energia_Kwh_Ponta 		= ConsumoKwhPonta * Tarifa_ConsumoKwhPonta
Energia_Kwh_FPonta 		= ConsumoKwhFPonta * Tarifa_ConsumoKwhFPonta
Energia_ReativoPonta 	= ConsumoReativoPonta * Tarifa_ConsumoReativoPonta
Energia_ReativoFPonta 	= ConsumoReativoFPonta * Tarifa_ConsumoReativoFPonta

Energia_ConsumoDemandaDISUltraTUSD = ConsumoDemandaDISUltraTUSD * Tarifa_ConsumoDemandaDISUltraTUSD
Energia_ConsumoDemandaDISTUSD 	= ConsumoDemandaDISTUSD * Tarifa_ConsumoDemandaDISTUSD
Energia_Energia_ACL_Com_ICMS_P 	= Energia_ACL_Com_ICMS_P * Tarifa_Energia_ACL_Com_ICMS_P 
Energia_Energia_ACL_Com_ICMS_F 	= Energia_ACL_Com_ICMS_F * Tarifa_Energia_ACL_Com_ICMS_F 
Energia_Subsidio_Tarifa_Liquido = Subsidio_Tarifa_Liquido * Tarifa_Subsidio_Tarifa_Liquido 

Contr_Iluminacao_Publica 	= 80.02
Deducao_Energia_AC_Sem_ICMS = -92360.60
Subsidio_Tarifa_Liquido 	= -24031.25


ValorTotal = Energia_Kwh_Ponta + Energia_Kwh_FPonta + Energia_ReativoPonta + Energia_ReativoFPonta + Energia_ConsumoDemandaDISUltraTUSD + Energia_ConsumoDemandaDISTUSD +Energia_Energia_ACL_Com_ICMS_P + Energia_Energia_ACL_Com_ICMS_F + Energia_Subsidio_Tarifa_Liquido + Contr_Iluminacao_Publica + Deducao_Energia_AC_Sem_ICMS + Subsidio_Tarifa_Liquido


print(f'MesFatura : {MesFatura}')
print(f'Energia Elet Consumo Pta      kwh : {Energia_Kwh_Ponta:>8,.2f}')
print(f'Energia Elet Consumo F Pta    kwh : {Energia_Kwh_FPonta:>8,.2f}')
print(f'Energia Reat Exc Pota         kwh : {Energia_ReativoPonta:>8,.2f}')
print(f'Energia Reat Exc F Pota       kwh : {Energia_ReativoFPonta:>8,.2f}')
print(f'Demanda Ultra Dis TUSD        kw  : {Energia_ConsumoDemandaDISUltraTUSD:>8,.2f}')
print(f'Demanda Dis TUSD       		  kw  : {Energia_ConsumoDemandaDISTUSD:>8,.2f}')
print(f'Energia Elet ACL com ICMS_P   kwh : {Energia_Energia_ACL_Com_ICMS_P:>8,.2f}')
print(f'Energia Elet ACL com ICMS_F   kwh : {Energia_Energia_ACL_Com_ICMS_F:>8,.2f}')
print(f'Subsidio Tarifa TUSD          kwh : {Energia_Subsidio_Tarifa_Liquido:>8,.2f}')
print('.')


print(f'Valor Total da fatura : {ValorTotal:>21,.2f}')


# '{:>13,.2f}'.format(100000)
#'   100,000.00'

print('================================================================')

#Variaveis
#Consumo
MesFatura 				= 92022
ConsumoKwhPonta 		= 37693
ConsumoKwhFPonta 		= 300321
ConsumoReativoPonta 	= 824
ConsumoReativoFPonta 	= 9632

ConsumoDemandaDISUltraTUSD 	= 218.51
ConsumoDemandaDISTUSD 		= 1108.51

Energia_ACL_Com_ICMS_P = 37693
Energia_ACL_Com_ICMS_F = 300321
Subsidio_Tarifa_Liquido= 1.057865

#Tarifa
Tarifa_ConsumoKwhPonta 		= 0.604056
Tarifa_ConsumoKwhFPonta 	= 0.117264
Tarifa_ConsumoReativoPonta 	= 0.334029
Tarifa_ConsumoReativoFPonta = 0.334054

Tarifa_ConsumoDemandaDISUltraTUSD = 37.194545
Tarifa_ConsumoDemandaDISTUSD = 9.336352

Tarifa_Energia_ACL_Com_ICMS_P = 0.350524
Tarifa_Energia_ACL_Com_ICMS_F = 0.350524
Tarifa_Subsidio_Tarifa_Liquido= 26909.07



#Calculo
Energia_Kwh_Ponta 		= ConsumoKwhPonta * Tarifa_ConsumoKwhPonta
Energia_Kwh_FPonta 		= ConsumoKwhFPonta * Tarifa_ConsumoKwhFPonta
Energia_ReativoPonta 	= ConsumoReativoPonta * Tarifa_ConsumoReativoPonta
Energia_ReativoFPonta 	= ConsumoReativoFPonta * Tarifa_ConsumoReativoFPonta

Energia_ConsumoDemandaDISUltraTUSD = ConsumoDemandaDISUltraTUSD * Tarifa_ConsumoDemandaDISUltraTUSD
Energia_ConsumoDemandaDISTUSD 	= ConsumoDemandaDISTUSD * Tarifa_ConsumoDemandaDISTUSD
Energia_Energia_ACL_Com_ICMS_P 	= Energia_ACL_Com_ICMS_P * Tarifa_Energia_ACL_Com_ICMS_P 
Energia_Energia_ACL_Com_ICMS_F 	= Energia_ACL_Com_ICMS_F * Tarifa_Energia_ACL_Com_ICMS_F 
Energia_Subsidio_Tarifa_Liquido = Subsidio_Tarifa_Liquido * Tarifa_Subsidio_Tarifa_Liquido 

Contr_Iluminacao_Publica 	= 80.02
Deducao_Energia_AC_Sem_ICMS = -97155.35
Subsidio_Tarifa_Liquido 	= -26909.07


ValorTotal = Energia_Kwh_Ponta + Energia_Kwh_FPonta + Energia_ReativoPonta + Energia_ReativoFPonta + Energia_ConsumoDemandaDISUltraTUSD + Energia_ConsumoDemandaDISTUSD +Energia_Energia_ACL_Com_ICMS_P + Energia_Energia_ACL_Com_ICMS_F + Energia_Subsidio_Tarifa_Liquido + Contr_Iluminacao_Publica + Deducao_Energia_AC_Sem_ICMS + Subsidio_Tarifa_Liquido


print(f'MesFatura : {MesFatura}')
print(f'Energia Elet Consumo Pta      kwh : {Energia_Kwh_Ponta:>8,.2f}')
print(f'Energia Elet Consumo F Pta    kwh : {Energia_Kwh_FPonta:>8,.2f}')
print(f'Energia Reat Exc Pota         kwh : {Energia_ReativoPonta:>8,.2f}')
print(f'Energia Reat Exc F Pota       kwh : {Energia_ReativoFPonta:>8,.2f}')
print(f'Demanda Ultra Dis TUSD        kw  : {Energia_ConsumoDemandaDISUltraTUSD:>8,.2f}')
print(f'Demanda Dis TUSD       		  kw  : {Energia_ConsumoDemandaDISTUSD:>8,.2f}')
print(f'Energia Elet ACL com ICMS_P   kwh : {Energia_Energia_ACL_Com_ICMS_P:>8,.2f}')
print(f'Energia Elet ACL com ICMS_F   kwh : {Energia_Energia_ACL_Com_ICMS_F:>8,.2f}')
print(f'Subsidio Tarifa TUSD          kwh : {Energia_Subsidio_Tarifa_Liquido:>8,.2f}')
print('.')


print(f'Valor Total da fatura : {ValorTotal:>21,.2f}')


# '{:>13,.2f}'.format(100000)
#'   100,000.00'

