"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no memso if (ruim)
    <- Contagem de complexidade (ruim)
"""
velocidade = 62 # velocidade atual do carro
local_carro = 101 # local em que o carro está na estrada

RADAR_1 = 60 # velocidade máxima de radas 1
LOCAL_1 = 100 # local onde o radas 1 está
RADAR_RANGE = 1 # A distancia onde o radas pega

# Abaixo uma forma de um codigo limpo, sem muitos 'ifs'.

vel_carro_pass_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar_1 = carro_passou_radar_1 and vel_carro_pass_radar_1

if vel_carro_pass_radar_1:
    print('Velocidade carro passou do radar 1')
    
if carro_passou_radar_1:
    print('Carro passou radar 1')
    
if carro_multado_radar_1:
    print('Carro Multado em radar 1')