# Pseudorandom Number Generation



### Contents
* [Introduction](https://github.com/greysonDEV/pseudo-rng#introduction)
* [Why Pseudorandom?](https://github.com/greysonDEV/pseudo-rng#why-pseudorandom)
* [Randomness in Computers](https://github.com/greysonDEV/pseudo-rng#randomness-in-computers)
* [Linear Congruential Generator (LCG)](https://github.com/greysonDEV/pseudo-rng#linear-congruential-generator-lcg)



### Introduction

Within this repository, the `prng` package includes a multitude of functions that allow the user to play around and experiment with pseudorandom number generation (PRNG). In this README I aim to investigate the theory and method behind PRNG as well as record my findings and research here. 



### Why Pseudorandom?

Pseudorandom numbers have many applications not only in the world of computer science but also in all of technology. The importance of PRNG is that a sequence of pseudorandom numbers is able to be reproduced, number for number. This is important in debugging computer programs and applications that rely on or deal with random numbers. For example, simulations like the Monte Carlo simulation need random numbers if they are to, well, *simulate*. A very interesting application that can be found on the Monte Carlo [*Wikipedia*](https://en.wikipedia.org/wiki/Monte_Carlo_method) page gives an example of how to calculate π using random numbers. Video games, casinos, and the shuffle feature on Spotify or Apple Music are just some of many applications of pseudorandom numbers. In fact, *all* of today's machine learning models are initialized with random weights so that the model is able to *break the symmetry* and take different paths (essential in gradient descent).



### Randomness in Computers

Computers are *deterministic* systems. In short, deterministic simply just means that the output of an algorithm is determined only by the inputs into that function. Computers are non-biased machines - they always follow a set of instructions to provide an output from some input. Because of this, computers themselves cannot create *truly* random numbers. Mathematician [*John von Neumann*](https://en.wikipedia.org/wiki/John_von_Neumann) once said:

> *Anyone who considers arithmetical methods of producing random digits is, of course, in a state of sin.*

In other words, a random number simply cannot be created via an arithmetic method. How else, if not arithmetic, can computers generate a truly random number? Well... they can't, hence ***pseudo***random.

Computers, however, are able to *receive* truly random data via an external, non-deterministic method. For example, using a Geiger Counter to measure radioactive activity will provide truly random results. 



### Linear Congruential Generator (LCG)

*Source:* [*Wikipedia*](https://en.wikipedia.org/wiki/Linear_congruential_generator)

After reading, consider taking a look at the linked article as this section barely scrapes the surface. 

A *Linear Congruential Generator (LCG)* is an algorithm designed to produce pseudorandom numbers. To find the *nth* term in any linear congruential series:

> *X*<sub>*n+1*</sub> = (*aX*<sub>*n*</sub> + *c*)<sub></sub> (*mod m*)



There are four parameters that are passed to an LCG:

1. `m` - modulus
2. `a` - multiplier
3. `c` - increment
4. `n` - seed

LCGs depend heavily on "good" parameter choice to produce a long period.

A natural question at this point would be...

> *Well, if the quality of the LCG depends on combinations of parameters, how should we choose the parameters?*

According to [*Wikipedia*](https://en.wikipedia.org/wiki/Linear_congruential_generator), there are three main paths to take for LCG parameter choices:

---

#### 1) `m is prime, c = 0`

> *The period is **m−1** if the; multiplier a is chosen to be a primitive element of the integers modulo **m**. The initial state must be chosen between **1** and **m−1**.*

<ins>**Example**</ins>
```python
>>> m = 751
>>> prng = lcg(
        m=m,
        a=577,
        c=0,
        n=331,

    )

>>> seq = [next(prng) for _ in range(m-1)] # length of 750
[233, 12, 165, ..., 431, 106, 331]
```
If you haven't guessed already, the period is going to be `m-1 = 751-1 = 750`. This means that if `next` is called on `prng` a few more times, the repetition becomes apparent:
```python
>>> next(prng)
233

>>> next(prng)
12

>>> next(prng)
165
```
A value for `a` can be achieved with the `primitive_roots()` utility method by passing in `m` (the example above chose 158 for `a`, which is a primitive root of `m`):
```python
>>> primitive_roots(263)
[5, 7, 10, 14, 15, ..., 158, ..., 257, 259, 260, 261]
```
For further examples, the `evaluate_period` utility method is used to return the LCG's period length. Although `evaluate_period()` provides a shortcut for finding the period, the simple, more visual process above may still be utilized.

---
#### 2) `m is a power of 2, c = 0`

> *This form has maximal period **m/4**, achieved if **a ≡ 3** or **a ≡ 5** (**mod 8**). The initial state **X**<sub>**0**</sub> must be odd...*

<ins>**Example**</ins>
```python
>>> prng = lcg(
        m=2**16,
        a=524291,
        c=0,
        n=48923,
    )

>>> evaluate_period(prng)
16384
```
Above the modulus is a power of 2 (`2**16` evaluates to 65536). The multiplier, `a`, mod `m` (`a % m`) evaluates to 3, which also satisfies the constraints. Finally, `c` is zero, and the initial state (`n`) is an odd number. The parameter choices here result in a period of 16384, which is, in fact, one fourth of the modulus.

---

#### 3) `c ≠ 0`

> *When **c ≠ 0**, correctly chosen parameters allow a period equal to **m**, for all seed values.*

"Correctly chosen parameters," as stated in the [*Wikipedia*](https://en.wikipedia.org/wiki/Linear_congruential_generator) article, means that:
```
1.  m and c are relatively prime
2.  a - 1 is divisible by all prime factors of m
3.  a - 1 is divisible by 4 if m is divisible by 4
```
Note that the third condition does not have to be met. It simply states that *if* `m` is divisible by 4, `a-1` must be as well.

<ins>**Example**</ins>
```python
>>> prng = lcg(
        m=2**16, # 65536
        a=14285,
        c=3091,
        n=948,
    )

>>> evaluate_period(prng)
65536
```
This is referred to as the *Hull-Dobell Theorem* and provides a parameter structure to achieve a maximal period of `m`. Two methods are defined in this repository for playing around with some of these parameters.
```python
# 1.  m and c are relatively prime
>>> relatively_prime(2**16, 3091)
True

# 2.  a - 1 is divisible by all prime factors of m
>>> prime_factors(2**16)
[2]
```

---
