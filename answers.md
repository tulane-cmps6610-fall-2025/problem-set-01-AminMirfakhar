  # CMPS 6610 Problem Set 01
## Answers

**Name:** Seyed Amin Mir Fakhar


Place all written answers from `assignment-01.md` here for easier grading.

1. **Asymptotic notation**

  - 1a. Is $2^{n+1} \in O(2^n)$? Why or why not?

    Base on definition: \: $g(n) \in O(f(n))$ \: if  \: $g(n) \leq c*f(n)$ \: exists such  \: $c > 0$ \: for all \: $n \geq n_0$

    So we should prove that $2^{n+1} \leq c*2^n to \[ \lim_{n\to\infty} \frac{2^{n+1}}{2^n} \] \leq c$:

  - 1b False
 
  - 1c False

  - 1d True

  - 1e False

  - 1f True

  - 1g The conditions cantradict each other so the intersection must be empty.

2. **SPARC to Python**

  - 2b It returns the max number

3. **Parallelism and recursion**

  - 3b since we search trough all list to check the key then W(n) = O(n), also, becasue there is no parallelism then S(n) = W(n) = O(n)

  - 3d W(n) = O(n.log(n)) and S(n) = (log(n))

  - 3e
  
4. **GCD**
