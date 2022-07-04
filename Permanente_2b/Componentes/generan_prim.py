from Componentes.miller_rabin import miller_rabin
from Componentes.comp_rand import comp_rand
from Componentes.BITS_R import BITS_R

def generan_prim(b):
    configure_s = 40
    s = configure_s
    n = BITS_R(b)
    while (not miller_rabin(n, s)):
        n += 2
  
    return n