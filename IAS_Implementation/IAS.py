def opcode(str):                    #this is a function which takes in instructions in english
    if (str=="LOAD MQ"):            #and returns their 8-bit opcode as shown
        return "00001010"
    elif(str =="LOAD MQ,M(X)"):
        return "00001001"
    elif(str=="STOR M(X)"):
        return "00100001"
    elif(str=="LOAD M(X)"):
        return "00000001"
    elif(str=="LOAD -M(X)"):
        return "00000010"
    elif(str=="LOAD |M(X)|"):
        return "00000011"
    elif(str=="LOAD -|M(X)|"):
        return "00000100"
    elif(str=="ADD M(X)"):
        return "00000101"
    elif(str=="ADD|M(X)|"):
        return "00000111"
    elif(str=="SUB M(X)"):
        return "00000110"
    elif(str=="SUB |M(X)|"):
        return "00001000"
    elif(str=="MUL M(X)"):
        return "00001011"
    elif(str=="DIV M(X)"):
        return "00001100"
    elif(str=="LSH"):
        return "00010100"
    elif(str=="RSH"):
        return "00010101"
    else:
        return "00000000"
def numtobinary(n):                         #this is a function which takes numbers upto 2000
    if(n<=2000):                            #and returns theeir 12-bit equivalent binary number
        i= bin(n).replace("0b", "")
        if len(i)<12:
            j="0"*(12-len(i))+i
    return j
def ntob80(n):                              #this is a function which takes a number and outputs 
    i= bin(n).replace("0b", "")             #its 80-bit binary equivalent binary number with leading zeros 
    if len(i)<80:                           
        j="0"*(80-len(i))+i
    return j
def ntob40(n):                              #this is a function which takes in a number and returns
    i= bin(n).replace("0b", "")             #its 40-bit equivalent binary number with leading zeros
    if len(i)<40:
        j="0"*(40-len(i))+i
    return j
def assembler(instr):                       #this is the assembler of the machine
    instr=instr+"e"                         #this breaks the assembly language codes into separate instructions
    lstr=""                                 #after converting, it returns 40-bit binary instruction of a line
    j=0
    if (instr[0]=="J"):                     #for jump statement
        return "0000000000000000000000001101000000000000"
    else:
        if (len(instr)>20):                 #for checking if there are two instructions or one in a line
            for i in range (0,len(instr)):
                if instr[i].isdigit():
                    j=i
                    break
            lstr=instr[0:j-1]               #lstr gives left operation
            k=0
            for i in range(j,len(instr)):
                if ((instr[i].isdigit()!=True)):
                    k=i
                    break
            n1=int(instr[j:k])              #n1 gives left operand
            m=0
            for i in range (k,len(instr)):
                if instr[i].isdigit():
                    m=i
                    break
            rstr=instr[k+1:m-1]             #rstr gives right operation
            n=0
            for i in range(m,len(instr)):
                if ((instr[i].isdigit()!=True)):
                    n=i
                    break
            n2=int(instr[m:n])              #n2 gives right operand
            instruction=opcode(lstr)+numtobinary(n1)+opcode(rstr)+numtobinary(n2)
            return instruction              #40-bit binary instruction
        elif (len(instr)<=20):              #condition when only a single operation is present
            for i in range (0,len(instr)):
                if instr[i].isdigit():
                    j=i
                    break
            lstr=instr[0:j-1]               #lstr now gives the right operation
            k=0
            for i in range(j,len(instr)):
                if ((instr[i].isdigit()!=True)):
                    k=i
                    break
            n1=int(instr[j:k])              #n1 now gives the right operand
            instruction='0'*20+opcode(lstr)+numtobinary(n1) #first 20-bits are zeros
            return instruction              #40-bit binary instruction


def decode(ins):                            #this the decoder
    global ctr,memory,PC,MAR,AC,MQ,MBR,instruction                             
    print("Instruction ", ctr,"------------>",ins)                   #the decoder takes the 40-bit instructions passed by the assembler
    LHS=ins[0:20]                                                    #and performs the necessary operations as guided by the assembler
    RHS=ins[20:40]
    op=LHS[0:8]
    ad=LHS[8:20]
    IBR=ins[20:40]
    MAR=PC
    MBR=ins
    print("PC--->",PC)
    print("MAR--->",MAR)
    print("MBR--->",ins)
    PC=PC+1
    print("LEFT INSTRUCTION CYCLE----------->")
    IR=op
    print("IR----------->",IR)
    MAR=ad
    print("MAR---------->",MAR)
    print("IBR---------->",IBR)

    #left instruction cycle begins


    if (op=="00000000"):
        print("")
    elif (op=="00100001"):          #STOR M(X) stores the contents of the accumulator in the desired memory location
        #STOR M(X)
        memory[int(ad,2)]=AC
        print("AC---->",ntob40(AC))
        print("MQ---->",ntob40(MQ))
    elif (op=="00001010"):
        #LOAD MQ                    #LOAD MQ transfers the contents of MQ register
        AC=MQ                       #to the accumulator after performing necessary operations
        print("AC---->",ntob40(AC))
        print("MQ---->",ntob40(MQ))
    elif(op=="00001001"):
        #LOAD MQ,M(X)               #LOAD MQ,M(X) transfers the contents of a desired memory
        MQ=memory[int(ad,2)]        #location to the MQ register for multiplication
        print("AC---->",ntob40(AC))
        print("MQ---->",ntob40(MQ))
    elif (op=="00001011"):
        #MUL M(X)
        MQ=MQ*memory[int(ad,2)]                     #MUL M(X) multiplies the MQ register by the 
        print("AC---->",(ntob80(MQ)[0:40]))         #desired memory location and keeps it in MQ
        print("MQ---->",(ntob80(MQ)[40:80]))
    elif (op=="00000001"):
        #LOAD M(X)                  #LOAD M(X) loads the contents of the desired memory location
        AC=memory[int(ad,2)]        #onto the accumulator
        print("AC---->",ntob40(AC))
    elif (op=="00000101"):
        #ADD M(X)                   #ADD M(X) adds the content of a particular memory location
        AC=AC+memory[int(ad,2)]     #to the Accumulator and keeps it there
        print("AC---->",ntob40(AC))
    elif (op=="00010100"):
        #LSH                        #LSH left shifts the value in AC by one bit
        AC=AC<<1
        print("AC---->",ntob40(AC))
    elif(op=="00010101"):
        #RSH                        #RSH right shifts the value in AC by one bit
        AC=AC>>1
        print("AC---->",ntob40(AC))
    elif (op=="00001101"):          #jump
        print(" ")

    print("-----------------------------------------")
    op=RHS[0:8]
    ad=RHS[8:20]
    print("PC--->",PC)

    #right instruction cycle begins


    print("RIGHT INSTRUCTION CYCLE---------->")
    IR=op
    MAR=ad
    print("IR----------->",IR)
    print("MAR---------->",MAR)
    if (op=="00000000"):
        print("")
    elif (op=="00100001"):
        #STOR M(X)                   #STOR M(X) stores the contents of the accumulator in the desired memory location
        memory[int(ad,2)]=AC
        print("AC---->",ntob40(AC))
        print("MQ---->",ntob40(MQ))
    elif (op=="00001010"):
        #LOAD MQ                    #LOAD MQ transfers the contents of MQ register
        AC=MQ                       #to the accumulator after performing necessary operations
        print("AC---->",ntob40(AC))
        print("MQ---->",ntob40(MQ))
    elif(op=="00001001"):
        #LOAD MQ,M(X)               #LOAD MQ,M(X) transfers the contents of a desired memory
        MQ=memory[int(ad,2)]        #location to the MQ register for multiplication
        print("AC---->",ntob40(AC))
        print("MQ---->",ntob40(MQ))
    elif (op=="00001011"):
        #MUL M(X)                               #MUL M(X) multiplies the MQ register by the
        MQ=MQ*memory[int(ad,2)]                 #desired memory location and keeps it in MQ
        print("AC---->",(ntob80(MQ)[0:40]))
        print("MQ---->",(ntob80(MQ)[40:80]))
    elif (op=="00000001"):
        #LOAD M(X)                  #LOAD M(X) loads the contents of the desired memory location
        AC=memory[int(ad,2)]        #onto the accumulator
        print("AC---->",ntob40(AC))
    elif (op=="00000101"):
        #ADD M(X)                   #ADD M(X) adds the content of a particular memory location
        AC=AC+memory[int(ad,2)]     #to the Accumulator and keeps it there
        print("AC---->",ntob40(AC))
    elif (op=="00010100"):
        #LSH                        #LSH left shifts the value in AC by one bit
        AC=AC<<1
        print("AC---->",ntob40(AC))
    elif(op=="00010101"):
        #RSH                        #RSH right shifts the value in AC by one bit
        AC=AC>>1
        print("AC---->",ntob40(AC))
    elif (op=="00001101"):          #jump
        print(" ")

    print("\n")

#driver code--------------


global memory                       #main memory array
global instruction
memory=[None]*1000
instruction=[]
print ("Enter (1->Volume of Cuboid, 2-> Surface area of Cuboid, 3->Power(a,b)) :::")
ch=int(input())
if (ch==1 or ch==2):                #choices for volume or surface area of cuboid
    print("Enter Values of l,b and h:")
    s=input()
    l=[i for i in s.split(" ")]
    memory[500]=int(l[0])
    memory[501]=int(l[1])
    memory[502]=int(l[2])
    memory[900]=2
elif (ch==3):
    print("Enter values of a and b:")       #choice for power(a,b) function
    s=input()
    l=[i for i in s.split(" ")]
    memory[500]=int(l[0])
    memory[501]=1
    memory[502]=int(l[1])
else:
    print("Invalid Choice.")


AC=0
PC=0
arr=[]
instr=input()
ins=assembler(instr)
instruction.append(ins)         #instruction array which stores the 40-bit binary instructions
while (instr!="HALT"):
    ins=assembler(instr)
    instruction.append(ins)
    instr=input()
ctr=0
i=0
j=memory[502]                   #for power(a,b) jump counter must be b
while i<len(instruction):   
    ctr+=1
    if (instruction[i][20:28]=="00001101" and j>1):         #executes jump instruction j no of times
        decode (instruction[0])
        i=0
        j-=1
    else:
        decode (instruction[i])
    i+=1

#output


if (ch==1):
    print("Volume is",memory[503])
elif (ch==2):
    print("Surface Area is",memory[506])
elif (ch==3):
    print(f'{memory[500]} to the power {memory[502]} is',memory[507])
else:
    print("None")
