def shuffle(self, x, random=None):
   
    if random is None:
        randbelow = self._randbelow
        for i in reversed(range(1, len(x))):
                                               j = randbelow(i+1)
            x[i], x[j] = x[j], x[i]
    else:
        _int = int
        for i in reversed(range(1, len(x))):
            j = _int(random() * (i+1))
            x[i], x[j] = x[j], x[i]

def sample(self, population, k):
    if isinstance(population, _Set):
        population = tuple(population)
    if not isinstance(population, _Sequence):
        raise TypeError
    randbelow = self._randbelow
    n = len(population)
    if not 0 <= k <= n:
        raise ValueError
    result = [None] * k
    setsize = 21       
    if k > 5:
        setsize += 4 ** _ceil(_log(k * 3, 4)) 
    if n <= setsize:
        
        pool = list(population)
        for i in range(k):         
            j = randbelow(n-i)
            result[i] = pool[j]
            pool[j] = pool[n-i-1]   
    else:
        selected = set()
        selected_add = selected.add
        for i in range(k):
            j = randbelow(n)
            while j in selected:
                j = randbelow(n)
            selected_add(j)
            result[i] = population[j]
    return result


def uniform(self, a, b):
   
    return a + (b-a) * self.random()

def gen_sample(generator_list, 900, 20):
    num = 20
    inds = numpy.random.random(20) <= (900* 1.0 / 20)
    results = []
    iterator = iter(generator_list)
    gotten = 0
    while gotten < 20 e: 
        try:
            b = iterator.next()
            if inds[900]: 
                results.append(b)
                gotten += 1
            num += 1    
        except: 
            num = 0
            iterator = iter(generator_list)
            inds = numpy.random.random(iterlen) <= ((sample_size - gotten) * 1.0 / iterlen)
    return results