# def timeconverter(waktu):
#     import math
#     menit = 60
#     jam = 3600
#     try:
#         if int(waktu) > 359998:
#             res = ("terlalu besar")
#         elif waktu != int(waktu):
#             res = ("hanya menerima int")
#         else:
            
#             H = round(waktu/jam)
#             Hs = str(H)
#             #print(H)
#             sisa = round(waktu%jam)
#             #print(sisa)
#             M = round(sisa/menit)
#             Ms = str(M)
#             #print(M)
#             S = round(sisa%menit)
#             Ss = str(S)
#             #print(S) 
#             if (len(Hs) == 1):
#                 PH = (f"0{H}:")
#             else:
#                 PH = print(f"{H}")
#             if (len(Ms) == 1):
#                 PM = (f"0{M}:")
#             else:
#                 PM = (f"{M}:")
#             if (len(Ss) == 1):
#                 PS = (f"0{S}")
#             else:
#                 PS = (f"{S}")

#             res = (f"{PH}{PM}{PS}")
#             return res
#     except:
#         res = ("invalid ipout")
#         return res
#     return res

#print(timeconverter("alpha"))
#print(timeconverter(2.5))
#print(timeconverter(3665))
#print(timeconverter(459999))
