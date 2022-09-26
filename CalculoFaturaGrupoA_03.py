#Calculo de faturao do Grupo

#Imagem da fatura
# Fatura_GrupoA_Calculo_02.jpg
# Fatura tipo = Série B

#Variaveis
#Consumo
ConsumoKwhPonta = 66
ConsumoKwhFPonta = 431
ConsumoReativoPonta = 3
ConsumoReativoFPonta = 69
ConsumoDemanda = 4.13
ConsumoDemandaIsenta = 25.87

#Tarifa
TarifaKwhPonta = 1.995152
TarifaKwhFPonta = 0.509722
TarifaReativaPonta = 0.396667
TarifaReativaFPonta = 0.401304
TarifaDemanda = 24.474576
TarifaDemandaIsenta= 18.023966


#Calculo
Energia_Kwh_Ponta = ConsumoKwhPonta * TarifaKwhPonta
Energia_Kwh_FPonta = ConsumoKwhFPonta * TarifaKwhFPonta
Energia_ReativoPonta = ConsumoReativoPonta * TarifaReativaPonta
Energia_ReativoFPonta = ConsumoReativoFPonta * TarifaReativaFPonta
Demanda = ConsumoDemanda * TarifaDemanda
DemandaIsenta = ConsumoDemandaIsenta * TarifaDemandaIsenta
ValorTotal = Energia_Kwh_Ponta + Energia_Kwh_FPonta + Energia_ReativoPonta + Energia_ReativoFPonta + Demanda + DemandaIsenta


print(f'Energia Elet Consumo Pta      kwh : {Energia_Kwh_Ponta:>8,.2f}')
print(f'Energia Elet Consumo F Pta    kwh : {Energia_Kwh_FPonta:>8,.2f}')
print(f'Energia Reat Exc Pota         kwh : {Energia_ReativoPonta:>8,.2f}')
print(f'Energia Reat Exc F Pota       kwh : {Energia_ReativoFPonta:>8,.2f}')
print(f'Demanda                       kw  : {Demanda:>8,.2f}')
print(f'Demanda isenta ICMS           kw  : {DemandaIsenta:>8,.2f}')

print(f'Valor Total da fatura : {ValorTotal:>13,.2f}')


# '{:>13,.2f}'.format(100000)
#'   100,000.00'

