
def main():
    vec1 = []
    x = input("Skriv inn kordinatene til vektoren")
    vec1 = x.split(",")
    for i in range (len(vec1)):
        vec1[i] = float(vec1[i])
    skalar = float(input("Skriv inn en skalar: "))

    vec3 = []
    x = input("Skriv inn kordinatene til din andre vektor")
    vec3 = x.split(",")
    for i in range (len(vec3)):
        vec3[i] = float(vec3[i])
    skalar2 = float(input("Skriv inn en skalar til vektor 2: "))

    vektor_math(vec1,vec3,skalar,skalar2)


def vektor_math(vec1,vec3,skalar,skalar2):
    print("Din vektor =",vec1, "\nDin skalar =",skalar)
    vec2 = []
    vec2.extend(vec1)
    for i in range(len(vec1)):
        vec2 [i] *= skalar
    print("Din skalarmultiplikasjon er =", vec2)

    if vec3:
        print("Din vektor nr2 =",vec3, "\nDin skalar nr2 =",skalar2)
        vec4 = []
        vec4.extend(vec3)
        for i in range(len(vec4)):
            vec4 [i] *= skalar2
        print("Din skalarmultiplikasjon nr2 er =", vec4)
    vektor_lengde(vec1,vec2,vec3,vec4)





def vektor_lengde (vec1,vec2,vec3,vec4):

    vec5 = []
    vec5.extend(vec1)

    for i in range (len(vec5)):
        vec5[i] *= vec3[i]
    print("\nDotproduktet ditt er =", vec5)

    for i in range(len(vec1)):
        vec1 [i] *= vec1[i]
    lengde_vec1 = sum(vec1)**(1/2)


    for i in range (len(vec2)):
        vec2 [i] *= vec2[i]
    lengde_vec2 = sum(vec2)**(1/2)

    for i in range(len(vec3)):
        vec3 [i] *= vec3[i]
    lengde_vec3 = sum(vec3)**(1/2)


    for i in range (len(vec4)):
        vec4 [i] *= vec4[i]
    lengde_vec4 = sum(vec4)**(1/2)




    print("\nVector 1:")
    print("Din vektorlengde var =",'%.2f'%lengde_vec1 ,"Din vektorlengde er nå =",'%.2f'%lengde_vec2)
    print("Forholder mellom vektorene er =",int(abs(lengde_vec1-lengde_vec2)))
    print("Vector 2:")
    print("Din vektorlengde var =",'%.2f'%lengde_vec3 ,"Din vektorlengde er nå =",'%.2f'%lengde_vec4)
    print("Forholder mellom vektorene er =",int(abs(lengde_vec3-lengde_vec4)),"\n"*6)
    main()
main()

