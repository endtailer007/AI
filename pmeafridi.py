import math
bp=float(input("Insert brake power(kW): "))
rpm=float(input("Insert speed of engine in rpm: "))
m=float(input("Enter the speed of reciprocating parts(kg):  "))
def clearance(x):
    if x in range(75,100):
        return 1.5
    elif x in range(100,150):
        return 2.4
    elif x in range(150,200):
        return 4.0
    elif x in range(200,250):
        return 6.3
    elif x in range(250,300):
        return 8.0
    elif x in range(300,350):
        return 9.5
    elif x in range(350,500):
        return 12.5
N=rpm*1.1
p=1000000
engineOfType=input("""Press 1-for petrol engines and 
2-for diesel engines.: """)
if engineOfType=="1":
    print("Assuming stroke length by bore diameter ratio (l/d)=1")
    print("Assuming mechanical efficiency=80%")
    noOfStroke=input("""Enter 1 for two stroke and 
    2 for four stroke engine: """)
    mecheff=0.8
    strokeByBore=1
    if noOfStroke=="1":
        n=N
        print("Power cycle per min(N)(rpm)=%3.3f"%(n))
        typeofcooling=input("Press 1 for water cooled and press 2 for air cooled: ")
        ip=float(bp/mecheff)
        print("indicated power = (brake power/mechanical efficiency)=%3.3f"%(ip))
        print("""Since we know 
                                            IP = p*A*l*n*(no of power stroke)/60""")
        D=float(((ip*60*1000*4)/(p*n*3.14)))
        d=(D**0.33333)
        print("             Bore diameter(mm)(d)=%3.3f"%(d))
        c=int(d*1000)
        print("""               Length of Stroke (l)= %3.3f"""%(c*1.5))
        r=c/2
        le=c*2
        print("Radius of crank(m) =l/2=%3.3f"%(r))
        print("Length of connecting rod (mm)=2*l= %3.3f"%(le))
        print('Length of cylinder=%3.3f'%(c*1.5*1.15))
        print("""                   Finding thickness of cylinder wall:  \n """)
        pmax=p*10
        C = clearance(int(d * 1000))
        Sc = float(input("Enter circumferencial stresses induced in the cylinder in N/mm^2(between 35 and 100):  "))
        print("""                     Thickness of the cylinder wall can be calculated from the below formula 
                                          t=((pmax*d)/(2*Si))+C      """)
        t =( ((pmax * d) / (2 * Sc) + float(C)))/1000
        print("Thickness of the cylinder wall is %3.3f mm\n" % (t))
        k=0.162
        print("""                               Thickness of cylinder head can be calculated as follows:
                                                            th=d*sqrt((k*pmax)/Sc)""")
        th=d*math.sqrt((k*pmax)/Sc)
        print("Thickness of the cylinder head is %3.3f mm\n" % (th))
    elif noOfStroke=="2":
        n = N/2
        print("Power cycle per min(N)(rpm)=%3.3f" % (n))
        typeofcooling = input("Press 1 for water cooled and press 2 for air cooled: ")
        ip = float(bp / mecheff)
        print("indicated power = (brake power/mechanical efficiency)=%3.3f" % (ip))
        print("""Since we know 
                                                    IP = p*A*l*n*(no of power stroke)/60""")
        D = float(((ip * 60 * 1000 * 4) / (p * n * 3.14)))
        d = (D ** 0.33333)
        print("             Bore diameter(mm)(d)=%3.3f" % (d))
        c = int(d * 1000)
        print("""               Length of Stroke (l)= %3.3f""" % (c * 1.5))
        r = c / 2
        le = c * 2
        print("Radius of crank(m) =l/2=%3.3f" % (r))
        print("Lenth of connecting rod (mm)=2*l= %3.3f" % (le))
        print('Length of cylinder=%3.3f' % (c * 1.5 * 1.15))
        print("""                   Finding thickness of cylinder wall:  \n """)
        pmax=p*10
        C=clearance(int(d*1000))
        Sc = float(input("Enter circumferencial stresses induced in the cylinder in N/mm^2(between 35 and 100):  "))
        print("""                     Thickness of the cylinder wall can be calculated from the below formula 
                                          t=((pmax*d)/(2*Si))+C      """)
        t =( ((pmax * d) / (2 * Sc) + float(C)))/1000
        print("Thickness of the cylinder wall is %3.3f mm\n" % (t))
        k=0.162
        print("""                               Thickness of cylinder head can be calculated as follows:
                                                            th=d*sqrt((k*pmax)/Sc)""")
        th=d*math.sqrt((k*pmax)/Sc)
        print("Thickness of the cylinder head is %3.3f mm\n" % (th))
elif engineOfType=="2":
    print("Assuming stroke length by bore diameter ratio l/d = 1.1")
    print("Assuming mechanical efficiency =76%")
    noOfStroke=input("""Press 1 for two stroke 
    press 2 for four stroke: """)
    mecheff=0.76
    strokeByBore=1.1
    if noOfStroke == "1":
        n = N
        print("Power cycle per min(N)(rpm)=%3.3f" % (n))
        typeofcooling = input("Press 1 for water cooled and press 2 for air cooled: ")
        ip = float(bp / mecheff)
        print("indicated power = (brake power/mechanical efficiency)=%3.3f" % (ip))
        print("""Since we know 
                                                    IP = p*A*l*n*(no of power stroke)/60""")
        D = float(((ip * 60 * 1000 * 4) / (p * n * 3.14)))
        d = (D ** 0.33333)
        print("             Bore diameter(mm)(d)=%3.3f" % (d))
        c = int(d * 1000)
        print("""               Length of Stroke (l)= %3.3f""" % (c * 1.5))
        r = c / 2
        le = c * 2
        print("Radius of crank(m) =l/2=%3.3f" % (r))
        print("Lenth of connecting rod (mm)=2*l= %3.3f" % (le))
        print('Length of cylinder=%3.3f' % (c * 1.5 * 1.15))
        print("""                   Finding thickness of cylinder wall:  \n """)
        pmax=p*10
        C = clearance(int(d * 1000))
        Sc = float(input("Enter circumferencial stresses induced in the cylinder in N/mm^2(between 35 and 100):  "))
        print("""                     Thickness of the cylinder wall can be calculated from the below formula 
                                          t=((pmax*d)/(2*Si))+C      """)
        t = (((pmax * d) / (2 * Sc) + float(C))) / 1000
        print("Thickness of the cylinder wall is %3.3f mm\n" % (t))
        k=0.162
        print("""                               Thickness of cylinder head can be calculated as follows:
                                                            th=d*sqrt((k*pmax)/Sc)""")
        th=d*math.sqrt((k*pmax)/Sc)
        print("Thickness of the cylinder head is %3.3f mm\n" % (th))
    elif noOfStroke=="2":
        n = N/2
        print("Power cycle per min(N)(rpm)=%3.3f" % (n))
        typeofcooling = input("Press 1 for water cooled and press 2 for air cooled: ")
        ip = float(bp / mecheff)
        print("indicated power = (brake power/mechanical efficiency)=%3.3f" % (ip))
        print("""Since we know 
                                                    IP = p*A*l*n*(no of power stroke)/60""")
        D = float(((ip * 60 * 1000 * 4) / (p * n * 3.14)))
        d = (D ** 0.33333)
        print("             Bore diameter(mm)(d)=%3.3f" % (d))
        c = int(d * 1000)
        print("""               Length of Stroke (l)= %3.3f""" % (c * 1.5))
        r = c / 2
        le = c * 2
        print("Radius of crank(m) =l/2=%3.3f" % (r))
        print("Lenth of connecting rod (mm)=2*l= %3.3f" % (le))
        print('Length of cylinder=%3.3f' % (c * 1.5 * 1.15))
        print("""                   Finding thickness of cylinder wall:  \n """)
        pmax=p*10
        C = clearance(int(d * 1000))
        Sc=float(input("Enter circumferencial stresses induced in the cylinder in N/mm^2(between 35 and 100):  "))
        print("""                     Thickness of the cylinder wall can be calculated from the below formula 
                                          t=((pmax*d)/(2*Si))+C      """)
        t =( ((pmax * d) / (2 * Sc) + float(C)))/1000
        print("Thickness of the cylinder wall is %3.3f mm\n"%(t))
        k=0.162
        print("""                               Thickness of cylinder head can be calculated as follows:
                                                            th=d*sqrt((k*pmax)/Sc)""")
        th=d*math.sqrt((k*pmax)/Sc)
        print("Thickness of the cylinder head is %3.3f mm\n"%(th))
else:
    print("invalid input")


