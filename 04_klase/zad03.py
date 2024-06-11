# 3. Definisati klasu UnionSet koja ima konstruktor sa jednim parametrom n (ceo broj) i koji inicijalizuje n skupova A_i tako da je A_i = {i}.
# Implementirati metode get_set(k) koja vraca indeks skupa A_i u kome se nalazi broj k, kao i operaciju union(k,l) koja formira uniju Au skupova A_i i A_j
# u kojima se nalaze brojevi k i l. Pritom ako je i<j, onda A_i:=Au dok se A_j brise. Ukoliko k i l pripadaju istom skupu, funkcija ne radi nista.

class UnionSet:
    def __init__(self, n):
        self.sets = [{i} for i in range(n)]
        self.parent = list(range(n))

    def find(self, k):
        if self.parent[k] != k:
            self.parent[k] = self.find(self.parent[k])
        return self.parent[k]

    def get_set(self, k):
        return self.find(k)

    def union(self, k, l):
        root_k = self.find(k)
        root_l = self.find(l)
        if root_k < root_l:
            self.sets[root_k].update(self.sets[root_l])
            self.sets[root_l] = set()
            self.parent[root_l] = root_k
        else:
            self.sets[root_l].update(self.sets[root_k])
            self.sets[root_k] = set()
            self.parent[root_k] = root_l

    def __str__(self):
        return str([s for s in self.sets if s])


n = 5
u = UnionSet(n)
print(u)
u.union(2, 3)
print(u)
