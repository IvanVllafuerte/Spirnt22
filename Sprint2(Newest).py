
# Sprint 2 basic computation
# Ivan Villafuerte
# Program will help people figure out what cpu goes with motherboard
# Inetl, AMD
# 12th gen Intel-Z690,H6770,B660,H610
# 11th gen Intel-Z590,H470,B460,H410
# Amd gen 5000- X570,B550, from X570-x370
# Amd gen 3000-X370,B340 from X570-X370

# Cpu-intel

intelCpu_12_9 = ("Intel i9 12900k")
intelCpu_12_7 = ("Intel i7 12700k")
intelCpu_12_5 = ("Intel i5 12400")
intelCpu_12_3 = ("Intel i3 12100f")

intelCpu_11_9 = ("Intel i9 11900k")
intelCpu_11_7 = ("Intel i7 11700k")
intelCpu_11_5 = ("Intel i5 11500k")
intelCpu_11_3 = ("Intel i3 11400f")

# Cpu AMD
amdCpu_5000_9 = ("Ryzen 9 5900x")
amdCpu_5000_7 = ("Ryzen 7 5800x")
amdCpu_5000_5 = ("Ryzen 5 5600x")

amdCpu_3000_9 = ("Ryzen 9 3900x")
amdCpu_3000_7 = ("Ryzen 7 3700x")
amdCpu_3000_5 = ("Ryzen 5 3600x")
amdCpu_3000_3 = ("Ryzen 3 3100")

# Motherboard
# intel
intel_motherboard_12 = ("Motherboard to get: Z690,H670,B660,H610 ")
intel_motherboard_11 = ("Motherboard to get: Z590,H470,B460,H410 ")
intel_motherboard_10 = ("Motherboard to get: Z590,Z490,B460,H410 ")

# AMD
amd_motherboard_5000 = ("Motherboard to get:  B550-B340,X570-X370 ")
amd_motherboard_3000 = ("Motherboard to get:  B550-B340,X570-X370 ")

# which brand the cpu is?
on = True
while on:
    cpu_type = input("Which brand cpu is being used? ")

    try:
        on = False

    except:
        print("Error")
        pass

cpu_type_amd = ("AMD")
cpu_type_intel = ("Intel")

# intel cpu and if statement with motherboard
for x in range(1):
    if cpu_type == cpu_type_intel:
        print("""              Options 1:Intel i9 12900k 
              Options 2:Intel i7 12700k
              Options 3:Intel i5 12400
              Options 4:Intel i3 12100f
              Options 5:Intel i9 11900k
              Options 6:Intel i7 11700K
              options 7:Intel i5 11500k
              Options 8:Intel i3 11400f""")
        cpu_type_intel=input("Which Options would you like?: ")

    else:
        print("""                    Options 1:Ryzen 9 5900x
                    Options 2:Ryzen 7 5800x
                    Options 3:Ryzen 5 5600x
                    Options 4:Ryzen 9 3900x
                    Options 5:Ryzen 7 3700x
                    Options 6:Rzyen 5 3600x
                    Options 7:Ryzen 3 3100 """)
        cpu_type_amd = input("Which options would you like?: ")
###Amd cpu- COmpatiability
##12th gen

    if cpu_type_intel == intelCpu_12_9:
        print(intel_motherboard_12)

    if cpu_type_intel == intelCpu_12_7:
        print(intel_motherboard_12)
    if cpu_type_intel == intelCpu_12_5:
        print(intel_motherboard_12)
    if cpu_type_intel == intelCpu_12_3:
        print(intel_motherboard_12)
    ##11th gen
    if cpu_type_intel == intelCpu_11_9:
        print(intel_motherboard_11)
    if cpu_type_intel == intelCpu_11_7:
        print(intel_motherboard_11)
    if cpu_type_intel == intelCpu_11_5:
        print(intel_motherboard_11, sep=".")
    if cpu_type_intel == intelCpu_11_3:
        print(intel_motherboard_11, end = ".")

#5000 series

    if   cpu_type_amd==amdCpu_5000_9:
       print(amd_motherboard_5000)
    if  cpu_type_amd==amdCpu_5000_7:
        print(amd_motherboard_5000)
    if  cpu_type_amd==amdCpu_5000_5:
        print(amd_motherboard_5000)
    #3000 series
    if  cpu_type_amd==amdCpu_3000_9:
        print(amd_motherboard_3000)
    if cpu_type_amd == amdCpu_3000_7:
        print(amd_motherboard_3000)
    if cpu_type_amd == amdCpu_3000_5:
         print(amd_motherboard_3000)
    if cpu_type_amd == amdCpu_3000_3:
        print(amd_motherboard_3000)

# if cpu_type_amd != cpu_type_intel
# This is a not statement or not equal

# number = (4*4)
# Multiplication

#number = (4/2)
#Dividing
#
#number = (4+2)
#Adding
#
#number = (4-1)
#Subtracting
#
#









