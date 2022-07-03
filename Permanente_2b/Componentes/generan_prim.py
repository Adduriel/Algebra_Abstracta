from Componentes.miller_rabin import miller_rabin
from Componentes.comp_rand import comp_rand
from Componentes.BITS_R import BITS_R

configure_s = 40

def generan_prim(b):
    s = configure_s
    n = BITS_R(b)
    while (not miller_rabin(n, s)):
        n += 2
  
    return n