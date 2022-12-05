#Código trabalho fmcc2 - Matemática do QRCODe

import qrcode

dado = "http://4.bp.blogspot.com/_LsUvt-LCfJI/SuI_qi1VHMI/AAAAAAAAA4w/_A6ddNMF4s0/s320/selo%5B1%5D.jpg"
img = qrcode.make(dado)
img.save("meu_qrcode.jpg")
