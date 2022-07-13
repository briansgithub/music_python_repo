import sys
sys.setrecursionlimit(1000000)  # long type, 32bit OS 4B, 64bit OS 8B (1bit for sign)

def multiple_solutions(a, b, n):

    x = []
     
    a = a % n
    b = b % n
    s = 0
    t = 0
     
    # Function Call to find
    # the value of d and u
    d, s, t = extended_gcd(a, n)
     
    # Else, initialize the value of x0
    x0 = (s * (b // d)) % n
    if (x0 < 0):
        x0 += n
    
    for i in range(d):
        x.append((x0 + i * (n // d)) % n)

    return x

#Tonic to accidentals
def solve_linear_congruence(a, b, n):
    """Returns the number of sharps/flats in a given major key signature. 
    a*x = b (mod n)
    a = generating interval. Default 7 (Perfect 5th).
    #ignored a*x + offset, offset (pick a remainder from a unique additive cycle. Always 0 if a and n are relatively prime (gcd(a,n)=1)
    b = root note representative
    n = divisions in octave. Default 12."""
    
    d = gcd(a,n)
    solvable = True if b%d == 0 else False

    # Unique solution because all solutions for x are in the same residue class
    single_solution = True if d == 1 else False

#    print(f"solvable?: {solvable}, single_solution?: {single_solution}") 

    x = []
    
    #case 1
    if(not solvable):
        pass
    #case 2
    elif(single_solution):
        solution = (modular_inverse(a,n)*b) % n
        x.append(solution)

    #case 3: multiple solutions
    else:
        #divide a, b, and n by gcd(a,n). This is the least residue system.
        x = multiple_solutions(a, b, n)

    return x

def gcd(a, b):
  
    if(b==0):
        return a
    else: 
        return gcd(b, int(a)%int(b))


def rel_prime(a,b):
    """Determines if a and b are relatively prime"""
    if(gcd(a,b) == 1):
        return True
    else:
        return False

def modular_inverse(a, n):
    """returns x such that (x * a) % n == 1
        Note: modular inverse exists iff a and n are relatively prime (gcd(a,n) == 1)
    """

    gcd, x, _ = extended_gcd(a, n) #finds x*a + _*n = gcd. That is, x*a + _*n = 1 (mod n)
    if gcd != 1:
        return None
        #raise Exception('gcd(a,n) must be 1 for a to have an inverse (mod n)')
    return x % n

def extended_gcd(a, b):
    """Solve for s and t in Bezout's Theorem: a*s+b*t = gcd(a,b)"""

    if a == 0:
        return b, 0, 1
    else:
        gcd, s, t = extended_gcd(b % a, a)
        return gcd, t - (b // a) * s, s

def main():
    '''
    a = int(input("Arg a: \n\t"))
    b = int(input("Arg c: \n\t"))
    print("GCD: (gcd,s,t) = {} \n".format(extended_gcd(a,b)))
    '''
    a = int(input("Arg a: \n\t"))
    b = int(input("Arg b: \n\t"))
    n = int(input("Arg n: \n\t"))
#    b = int(input("Arg b: \n\t"))
#    print(f"gcd(18, 45): {gcd(18,45)}\n")
#    solve_linear_congruence()
    print(f"(gcd,s,t) = {extended_gcd(a,n)}")
    print(f"Solutions = {solve_linear_congruence(a,b,n)}")
    print(f"For a = 7, root note b is at index {solve_linear_congruence(a,b,n)} in the circle of fifths")
 
    return

main()
print("Done")
input()
