
# import re
# text="iPhone 16e	iPhone 16 Pro Max	iPhone 16 Pro	iPhone 16 Plus	iPhone 16	iPhone 15 Pro Max	iPhone 15 Pro	iPhone 15 Plus	iPhone 15   iPhone 14 Pro Max	iPhone 14 Pro	iPhone 14 Plus	iPhone 14	iPhone SE	iPhone 13 Pro Max	iPhone 13 Pro	iPhone 13	iPhone 13 Mini	iPhone 12 Pro Max	iPhone 12 Pro	iPhone 12	iPhone 12 Mini	iPhone SE	iPhone 11 Pro Max	iPhone 11 Pro	iPhone 11	iPhone XR	iPhone XS Max	iPhone XS"
# new= text.replace("\u00a0"," ")
# # print(new)
# new1 = re.sub(r'\s+', ' ', text)
# # txt="Heloo , wsf  ."
# # new0=txt
# # print (new1)
# new2=new1.replace(" iPhone",", iPhone")
# print(new2)

# list_models=[]
# list_models= new2.split(", ")
# print(list_models)




import re
text="iPhone 16e	iPhone 16 Pro Max	iPhone 16 Pro	iPhone 16 Plus	iPhone 16	iPhone 15 Pro Max	iPhone 15 Pro	iPhone 15 Plus	iPhone 15   iPhone 14 Pro Max	iPhone 14 Pro	iPhone 14 Plus	iPhone 14	iPhone SE	iPhone 13 Pro Max	iPhone 13 Pro	iPhone 13	iPhone 13 Mini	iPhone 12 Pro Max	iPhone 12 Pro	iPhone 12	iPhone 12 Mini	iPhone SE	iPhone 11 Pro Max	iPhone 11 Pro	iPhone 11	iPhone XR	iPhone XS Max	iPhone XS"
# new= text.replace("\u00a0"," ")

# new1 = re.sub(r'\s+', ' ', text)
# new2=new1.replace(" iPhone",", iPhone")
# list_models=[]

# list_models= new2.split(", ")
# print (len(list_models))
# print (list_models)

# list_models_trial =list_models[:5]
# print(list_models_trial)
###########################################################################################

text2= "Samsung Galaxy S25 5G	Samsung Galaxy S25 Plus 5G	Samsung Galaxy S25 Ultra 5G	Samsung Galaxy S24 Plus 5G	Samsung Galaxy A35 5G	Samsung Galaxy S22 5G	SAMSUNG Galaxy S24 Ultra 5G	Samsung Galaxy F16	Samsung Galaxy Z Flip 5	Samsung Galaxy Z Fold 5	Samsung Galaxy F22	Samsung Galaxy F41	Samsung Galaxy F62	Samsung A21s	Samsung Galaxy F02s	Samsung Galaxy A31	Samsung Galaxy A32	Samsung Galaxy A52	Samsung Galaxy A72	Samsung Galaxy S20 FE 5G"
# new= text2.replace("\u00a0"," ")

# new1 = re.sub(r'\s+', ' ',text2)
# new2=new1.replace(" Samsung",", Samsung")
# list_models=[]
# list_models= new2.split(", ")

# print (len(list_models))
# print (list_models)

###########################################################################################

text3= "Motorola Moto G96	Motorola g22	Motorola g32	Motorola g72	Motorola g53	Motorola g24	Motorola Edge 60	Motorola Edge 60 Pro	Motorola Edge 60 Stylus	Motorola one power	Motorola Edge 60 Fusion	Motorola Moto E7 power	Motorola Moto G8 power	Motorola Moto G05	Motorola Edge 50 Neo	Motorola Moto G35	Motorola Moto G31	Motorola Moto G45	Motorola Moto G64	Motorola Edge 50	Motorola Moto G54 Power 5G	Motorola Moto G85 5G	Motorola Moto G84 5G	Motorola Moto G14	Motorola Edge 40	Motorola Edge 30	Motorola Moto G13	Motorola Edge 30 Fusion	Motorola Edge 30 Ultra	Motorola Moto G73	Motorola Moto G62 5G	Motorola Moto G82"
# new = re.sub(r'\s+', ' ',text3)
# new1=new.replace(" Motorola",", Motorola")
# list_models=[]
# list_models= new1.split(", ")

# print (len(list_models))
# print (list_models)


#Vivo
text4="Vivo IQOO Neo 10 (Global)	Vivo Y300 GT	Vivo iQOO Z9s	Vivo iQOO Z10x	Vivo iQOO Z10	Vivo T3 Lite 5G	Vivo T4x 5G	Vivo V50 5G	Vivo Y200 4G	Vivo iQOO Z9	Vivo X200 Pro	Vivo v50e	Vivo v40e  Vivo iQOO Z9  Vivo iQOO Z9 lite	Vivo T3 Ultra	Vivo T3 Pro 5G	Vivo iQOO Z9s	Vivo iQOO Z9s Pro	Vivo V40 Pro	Vivo V40	Vivo X100s	Vivo x100 Pro	Vivo Y18	Vivo iQOO Z9x	Vivo T3x	Vivo T3 5G	Vivo V30 Pro	Vivo V29 Pro	Vivo V29	Vivo V27 Pro	Vivo X90 Pro Vivo V27"
# new = re.sub(r'\s+', ' ',text4)
# new1=new.replace(" Vivo",", Vivo")
# list_models=[]
# list_models= new1.split(", ")

# print (len(list_models))
# print (list_models)


#Boat
text5="boAt Airdopes 181 Pro	boAt Airdopes 161	boAt Rockerz 255 Pro+	boAt Rockerz 109	boAt Rockerz 111	boAt Airdopes Prime 701 ANC	boAt Nirvana Ion ANC	boAt Airdopes 148	Bassheads 110	boAt Rockerz 110	boAt Airdopes 161 (Metallic)	boAt Rockerz 413	boAt Bassheads 104	boAt Airdopes 163	boAt Airdopes 141 ANC	boAt Airdopes 138	boAt Rockerz 425	boAt Rockerz 333 Pro	boAt Rockerz 333	boAt Rockerz Trinity	TRebel Airdopes 141	boAt Rockerz 421	boAt Nirvana Iris	boAt Airdopes 141 Gen 2	boAt Rockerz 150 Pro	boAt Nirvana Ivy Pro	boAt Airdopes 213	boAt Rockerz 650 Pro	Bassheads 162v2	boAt Rockerz 551 ANC Pro	boAt Rockerz 411	boAt Airdopes 207	boAt Rockerz 245 V2 Pro	boAt Airdopes 138 PRO	boAt Rockerz 412	boAt Airdopes 141 Elite ANC	boAt Nirvana Ion	boAt Nirvana Ion ANC Pro	boAt Airdopes 393 ANC	boAt Nirvana Crystl	boAt Rockerz 202	boAt Nirvana X TWS	boAt Airdopes Plus 318	boAt Rockerz 460	boAt Rockerz 203	boAt Nirvana Zenith Pro"
# new = re.sub(r'\s+', ' ',text5)
# new1=new.replace(" boAt",", boAt")
# list_models=[]
# list_models= new1.split(", ")

# print (len(list_models))
# print (list_models)


#Fire-boult
text6="Boult Ammo earbuds	Boult Curve Buds Pro	Boult Curve Max earphone	Boult probass EQCharge	Boult Ember Bluetooth	Boult Escape	Boult probass fcharge neckband	Boult ProBass EQCharge neckband	Boult ProBass Xcharge neckband	Boult boult k10  50H	Boult X45	Boult y1 with zen earbuds	Boult y1 pro zen earbuds	Boult w20 zen enc mic earbuds	Boult Ycharge with Pro+ calling earphone	Boult z60 	Boult Z40	Boult Rcharge 30H playtime neckband	Boult klarity 1	Boult w35 bluetooth	Boult astra earbuds	Boult X1 pro	Boult X10 earbuds	Boult X45 earbuds	Boult X50 earbuds	Boult X60 earbuds	Boult z40 pro earbuds	Boult Z35 earbuds	Boult Z60 earbuds"
new = re.sub(r'\s+', ' ',text6)
new1=new.replace(" Boult",", Boult")
list_models=[]
list_models= new1.split(", ")

print (len(list_models))
print (list_models)
