bInsulin="fvnqhlcgshlvealylvcgergffytpkt"
cInsulin="rreaedlqvgqvelgggpgagslqplalegslqkr"

insulin=bInsulin+cInsulin


aminoAcidsList=['A', 'C','D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T',
'V', 'W', 'Y']

aaWeights = {'A': 89.09, 'C': 121.16, 'D': 133.10, 'E': 147.13, 'F': 165.19,
'G': 75.07, 'H': 155.16, 'I': 131.17, 'K': 146.19, 'L': 131.17, 'M': 149.21,
'N': 132.12, 'P': 115.13, 'Q': 146.15, 'R': 174.20, 'S': 105.09, 'T': 119.12,
'V': 117.15, 'W': 204.23, 'Y': 181.19}


# FVNQHLCGSHLVEALYLVCGERGFFYTPKTRREAEDLQVGQVELGGGPGAGSLQPLALEGSLQKR

aaCount={}

for x in aminoAcidsList:
    print(" Amino acid {} appears {} times".format(x,insulin.upper().count(x)))
    aaCount[x]=insulin.upper().count(x)

print(aaCount)

myInsulinWeight={}

for y in aminoAcidsList:
    print("Weight of amino acid {} in my insulin is {}".format(y,aaCount[y]*aaWeights[y]))
    myInsulinWeight[y]=aaCount[y]*aaWeights[y]

print(myInsulinWeight)

molecularWeightInsulin=0
for z in myInsulinWeight:
    molecularWeightInsulin+=myInsulinWeight[z]

print(molecularWeightInsulin)

