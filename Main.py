from ViajeroFrecuente import ViajeroFrecuente
if __name__== '__main__':
    viajero1=ViajeroFrecuente(14,33555555,'Luis','Gonzalez',1000)
    viajero2=ViajeroFrecuente(122,39883123,'Miguel','Sanders',1000)
    viajero3=ViajeroFrecuente(144,40222222,'Emilia','Fernandez',3500)
    print('Viajeros:')
    print(viajero1)
    print(viajero2)
    print(viajero3)
    print('---Acumular Millas---')
    viajeroNuevo=viajero1+500
    viajeroNuevo2=viajero2+600
    viajeroNuevo3=500+viajero3
    print(viajeroNuevo)
    print(viajeroNuevo2)
    print(viajeroNuevo3)
    print('---Canjear Millas---')
    viajeroNuevo4=viajeroNuevo-300
    viajeroNuevo5=400-viajeroNuevo2
    viajeroNuevo6=800-viajeroNuevo3
    print(viajeroNuevo4)
    print(viajeroNuevo5)
    print(viajeroNuevo6)
    print('--- Comparar Millas---')
    if viajeroNuevo4==1000:
        print('Tiene 1000 millas el viajero')
    else:
        print('No tiene 1000 millas el viajero')
    if 1200==viajeroNuevo4:
        print('Tiene 1200 millas el viajero')
    else:
        print('No tiene 1200 millas el viajero')
    viajero1.test()