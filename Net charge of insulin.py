# Python 3.10.4
# Coding: utf-8

# Use lists, for and while loops, and basic math to calculate the net charge
#  of insulin from pH 0 to pH 14

# Store the human preproinsulin sequence in a variable called preproinsulin
preproInsulin="malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktr" \
"reaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn"

# Store the remaining sequence elements of human insulin in variables:
lsInsulin="malwmrllpllallalwgpdpaaa"
bInsulin="fvnqhlcgshlvealylvcgergffytpkt"
cInsulin="rreaedlqvgqvelgggpgagslqplalegslqkr"
aInsulin="giveqcctsicslyqlenycn"

insulin=bInsulin+cInsulin
print(insulin)

# Y, C, K, H, R, D, and E are the only amino acids that contribute to the net-charge calculation
pKR={}
#print(pKR)
pKR = {'c': 8.18,'k':10.53,'h':6.00,'r':12.48,'d':3.65,'e':4.25}
#print(pKR)
pKR['y']=10.07
print(pKR)

# Count number of each amino acid in 'insulin'
# insulin=fvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkr
seqCount = ({x: float(insulin.count(x)) for x in ['y','c','k','h','r','d','e']})
print(seqCount)

# Calculate net charge
pH=0
while(pH<=14):
    netCharge = (
    +(sum({x: ((seqCount[x]*(10**pKR[x]))/((10**pH)+(10**pKR[x]))) \
    for x in ['k','h','r']}.values()))
    -(sum({x: ((seqCount[x]*(10**pH))/((10**pH)+(10**pKR[x]))) \
    for x in ['y','c','d','e']}.values())))
    print('{0:.2f}'.format(pH), netCharge)
    pH=pH+1





