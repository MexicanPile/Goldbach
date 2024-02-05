#Conjecture : Tout nombre entier pair supérieur à 3 peut s’écrire comme la somme de deux nombres premiers.
#Film intéressant : le théorème de marguerite (Récompensé au festival de Cannes)

import math

#Recuperer tous les nombres premiers inferieurs a n

def premier(n):
  if n % 2 != 0 or n <= 2:
        return False
  
  l=[2]
  for i in range(3,n,2): #seulement nombre entiers impairs pour augmenter performances
    j=1
    k=0
    while(math.gcd(j,i)==1 and k<len(l)-1):
      j=l[k]
      k+=1
    if(k==len(l)-1):
      l.append(i)
  return l

#trouve deux entiers premiers qui vérifie conjecture de Goldbach

def goldbach(n, liste_premiers):
  if n%2 != 0:
    print("Il faut que n soit paire")

  for j in liste_premiers:
    if (n-j) in liste_premiers:
      print(f"{n} = {j} + {n - j}")
      return True 
  return False 


#teste la conjecture de goldbach pour tout entier pair inférieur à n 

def test(n):
  primes=premier(n)
  for i in range(4,n+1,2):
    if not(goldbach(i, primes)):
      return False 
  return True 



print(test(800000))
