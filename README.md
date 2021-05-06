# Pseudorandom Number Generation


### Contents
* [Introduction]()
* [Randomness in Computers]()
* [Linear Congruential Generator (LCG)]()
* [Truly Random Numbers]()



### Introduction

In this GitHub repository I aim to investigate pseudorandom number generation (PRNG) and write my findings and research here. Multiple directories in this repository are included, all of which contain Python code relating to my investigation into PRNG.



### Randomness in Computers

Computers are *deterministic* systems. In short, deterministic simply just means that the output of an algorithm is determined only by the inputs into that function. Computers are non-biased machines, always following a set of instructions to provide an output from some input. Because of this, computers themselves cannot create *truly* random numbers. Mathematician [*John von Neumann*](https://en.wikipedia.org/wiki/John_von_Neumann) once said:

> *Anyone who considers arithmetical methods of producing random digits is, of course, in a state of sin.*

In other words, a random number simply cannot be created via an arithmetic method. How else, if not arithmetic, can computers generate a truly random number? Well... they can't, hence ***pseudo***random.

Computers, however, are able to *receive* truly random data via an external, non-deterministic method. For example, using a Geiger Counter to measure radioactive activity will provide truly random results. 

### Linear Congruential Generator (LCG)

[*Wikipedia*](https://en.wikipedia.org/wiki/Linear_congruential_generator)

A *Linear Congruential Generator (LCG)* is an algorithm designed to produce pseudorandom numbers. LCGs take in four parameters:

1. `m` - modulus
2. `a` - multiplier
3. `c` - increment
4. `n` - seed

LCG's depend heavily on "good" parameter choice to produce a long period.

A natural question at this point would be...

> *Well, if the quality of the LCG depends on combinations of parameters, how should we chooose the parameters?*

According to [*Wikipedia*](https://en.wikipedia.org/wiki/Linear_congruential_generator), there are three main paths to take for LCG parameter choices:

---

#### `m is prime, c = 0`
> *The period is **m−1** if the multiplier a is chosen to be a primitive element of the integers modulo **m**. The initial state must be chosen between **1** and **m−1**.*

<ins>**Example**</ins>
```python
>>> m = 263
>>> prng = lcg(
        m=m,
        a=158,
        c=0,
        n=3,

    )

>>> seq = [next(prng) for _ in range(m-1)] # length of 262
[211, 200, 40, 8, ..., 75, 15, 3]
```
If you haven't guessed already, the period *is* going to be `m-1 = 263-1 = 262`. This means that if we call `next` on `prng` a few more times, the repetition becomes obvious:
```python
>>> next(prng)
211

>>> next(prng)
200

>>> next(prng)
40
```
A value for `a` can be achieved with the `primitive_roots()` utility method by passing in `m` (the example above chose 158 for `a`, which is a primitive root of `m`):
```python
>>> primitive_roots(263)
[5, 7, 10, 14, 15, ..., 158, ..., 257, 259, 260, 261]
```
For further examples, the `evaluate_period` utility method is used to return the LCG's period length. Although `evaluate_period()` provides a shortcut for finding the period, the simple, more visual process above may still be utilized.

---
#### `m is a power of 2, c = 0`
> *This form has maximal period m/4, achieved if a ≡ 3 or a ≡ 5 (mod 8). The initial state X0 must be odd...*

<ins>**Example**</ins>
```python
>>> prng = lcg(
        m=2**8, # m is a power of 2
        a=163,  # a (mod m), or a%m, is 3
        c=0,
        n=13,
    )

>>> evaluate_period(prng)
64
```
Above, the modulus is a power of 2 (256). `a` is also 163, which satisfies the condition that `a` mod 8 is either 3 or 5 (it's 3).

---

#### `c ≠ 0`
> *When c ≠ 0, correctly chosen parameters allow a period equal to m, for all seed values.*

"Correctly chosen parameters," as stated in the [*Wikipedia*](https://en.wikipedia.org/wiki/Linear_congruential_generator) article, means that:
```
1.  m and c are relatively prime
2.  a - 1 is divisible by all prime factors of m
3.  a - 1 is divisible by 4 if m is divisible by 4
```

<ins>**Example**</ins>
```python
>>> prng = lcg(
        m=8,
        a=21,
        c=5,
        n=20,
    )

>>> evaluate_period(prng)
8
```

This path of parameter choice is a little bit more restrictive than the other common paths. For that, two methods are defined in this repository for testing:
```python
# m and c are relatively prime
>>> relatively_prime(8, 5)
True

>>> relatively_prime(25, 168)
True
```
```python
# a - 1 is divisible by all prime factors of m
>>> pfactors = prime_factors(8)

```
```python
# a - 1 is divisible by 4 if m is divisible by 4

```


### Truly Random Numbers

It has already been established that computers cannot create true random numbers; however, they can still *receive* them. A Geiger counter, a device that measures radioactive activity, *will* produce truly random numbers. Contrary to popular belief, something like a dice roll is *not* truly random. This is because it is still bounded by the laws of physics, and therefore could be predicted. 
