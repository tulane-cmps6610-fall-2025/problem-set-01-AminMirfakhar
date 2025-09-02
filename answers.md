  # CMPS 6610 Problem Set 01
## Answers

**Name:** Seyed Amin Mir Fakhar


1. **Asymptotic notation**

  - 1a. Is $2^{n+1} \in O(2^n)$? Why or why not?
    - Base on definition: \: $g(n) \in O(f(n))$ \: if  \: $g(n) \leq c*f(n)$ \: exists such  \: $c > 0$ \: for all \: $n \geq n_0$

    - So we should prove that:
     
      $2^{n+1} \leq c*2^n \to  \lim_ {n\to\infty} \frac{2^{n+1}}{2^n} = 2 \leq c$ ✅,
      
    - so the equation holds and the statement is ***TRUE***.



  - 1b. Is $2^{2^n} \in O(2^n)$? Why or why not?
     - We should prove that:
     
      $2^{2^{n}} \leq c*2^n \to  \lim_ {n\to\infty} \frac{2^{2^{n}}}{2^n} \to ^{log}   \lim_ {n\to\infty} \frac{{2^{n}}}{n}  \lim_ {n\to\infty} \frac{\infty}{\infty}$
    , l'hopital's rule
    $\to \lim_ {n\to\infty} \frac{2^{n}*log{2}}{1} \to \infty $
    ❌, 

    - so the equation doesn't hold and the statement is ***False***.


 
  - 1c. Is $n^{1.01} \in O(\mathrm{\log}^2 n)$?
    - We should prove that:
     
      $n^{1.01} \leq c*log^2{n} \to  \lim_ {n\to\infty} \frac{n^{1.01}}{log^2{n}} \leq c \to  \lim_ {n\to\infty} \(\frac{n^{1.01/2}}{log{n}})^2 \to  \lim_ {n\to\infty} \frac{\infty}{\infty}$
    , l'hopital's rule
    $\to \lim_ {n\to\infty} \frac{(\frac{1.01}{2}) * n ^ {\frac{1.01}{2} - 1}}{\frac{1}{n}} \to \lim_ {n\to\infty} \{(\frac{1.01}{2}) * n ^ {\frac{1.01}{2} }} \to \infty $
    ❌, 

    - so the equation doesn't hold and the statement is ***False***.


  - 1d. Is $n^{1.01} \in \Omega(\mathrm{\log}^2 n)$?
    - In general form $c * n^{k} \geq  log^b{n}$ for any k > 0
    - $log^b{n} \leq c*n^{k} \to  \lim_ {n\to\infty} \frac{log^b{n}}{n^{k}} \leq c \to  \lim_ {n\to\infty} (\frac{log{n}}{n^{k/b}})^b \to  \lim_ {n\to\infty} \frac{\infty}{\infty}$
    , l'hopital's rule
    $\to \lim_ {n\to\infty} (\frac{\frac{1}{n}}{(\frac{k}{b}) * n ^ {\frac{k}{b} - 1}})^{b} \to \lim_ {n\to\infty} (\{(\frac{k}{b}) ^ {b} * n ^ {{-k}}}) \leq c $
 ✅,

    - so the equation holds (for k = 1.01 and b = 2) and the statement is ***TRUE***.
  

  - 1e. Is $\sqrt{n} \in O(\mathrm{\log}^3 n)$?
    - Just based on previous section we showed that this statement is ***False***.
    - $\lim_ {n\to\infty} \{(\frac{1.01}{3}) * n ^ {\frac{1.01}{3} }} \to \infty $
    - ❌, 


  - 1f. Is $\sqrt{n} \in \Omega(\mathrm{\log}^3 n)$?
    - Based on the general form, this statement it ***TRUE***.
    -  $\lim_ {n\to\infty} (\{(\frac{0.5}{3}) ^ {3} * n ^ {{-0.5}}}) \leq c $
   ✅,


  - 1g **Prove** that $o(g(n)) \cap \omega(g(n))$ is the empty set.
  
     - Base on definition:
       $g(n) \in o(f(n)) \to g(n) < c * f(n) $
       and
        $g(n) \in w(f(n)) \to g(n) > c * f(n)$
     - By considering the first assumption (g(n) < c * f(n)) the second one couldn't be for all n greater or equal to n_0 and viceversa so basically:
     - The conditions cantradict each other so the intersection is empty!

2. **SPARC to Python**

Consider the following SPARC specification:  

  - 2a Translate this to Python code
  
  ```python

      def foo(a, b):
          if a == 0:
              return b
          elif b == 0:
              return a
          else:
              x, y = min(a, b), max(a, b)
              return foo(y, y%x)
  ``` 

  - 2b What does this function do, in your own words?
    - It returns the max number! It takas the maximum number (y = max(a, b)) at each iteration and the mod of this number to the minimum of two inputs (y%x, x = min(a, b)), Then recursively calls itself untill the y%x reaches the zero and the function returns the other value which is y = max(a, b).
    - so if we run foo(18, 7) it will run foo(18, 4) then foo(18, 2) then foo(18, 0) which returns 18.
   
  - 2c. What is the work and span of `foo`?
    - Since each step is order of 1, then W(n) = O(log(min(a, b)). Also we don't use any parallelism so the span = work. S(n) = O(log(min(a, b)).

3. **Parallelism and recursion**

  - 3b since we search trough all list to check the key then W(n) = O(n), also, becasue there is no parallelism then S(n) = W(n) = O(n)

  - 3d W(n) = O(n.log(n)) and S(n) = (log(n))

  - 3e
  
4. **GCD**
