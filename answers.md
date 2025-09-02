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

  - 2a Translate this to Python code -- fill in the `foo` method in `main.py`  
  
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
    - Since each operation at every step is order of 1 (O(1)), then the total work is equal to number of iteration * O(1). which means W(n) = O(number of devisions for any (a, b)) so we can say W(n) = O(log(min(a, b)). Also we don't use any parallelism so the span = work. S(n) = O(log(min(a, b)).

3. **Parallelism and recursion**
  - 3a. First, implement an iterative, sequential version of `longest_run` in `main.py`.

``` python
    def longest_run(mylist, key):
        counter = 0
        longest = 0
        for element in mylist:
            if element == key:
                counter += 1
                longest = max(counter, longest)
            else:
                counter = 0
    
        return longest

```


  - 3b What is the Work and Span of this implementation?
    - since we have to search trough entier list to check the key then W(n) = O(n), also, becasue there is no parallelism then S(n) = W(n) = O(n)

  
  - 3c. Next, implement a `longest_run_recursive`, a recursive, divide and conquer implementation. This is analogous to our implementation of `sum_list_recursive`. To do so, you will need to think about how to combine partial solutions from each recursive call. Make use of the provided class `Result`.   


``` python

class Result:
    def __init__(self, longest_size , left_size , right_size , is_entire_range ):
        self.longest_size  = longest_size 
        self.left_size  = left_size 
        self.right_size  = right_size 
        self.is_entire_range  = is_entire_range 

def longest_run_recursive(arr, key):
    if len(arr) == 0:
        return Result(0, 0, 0, 0)
    if len(arr) == 1:
        if arr[0] == key:
            return Result(1, 1, 1, 1)
        else:
            return Result(0, 0, 0, 0)

    mid = len(arr) // 2
    left = longest_run_recursive(arr[:mid], key)
    right = longest_run_recursive(arr[mid:], key)

    is_entire_range = left.is_entire_range + right.is_entire_range if left.is_entire_range == mid and right.is_entire_range == len(arr) - mid else 0
    left_size = left.left_size if left.left_size != mid else left.left_size + right.left_size
    right_size = right.right_size if right.right_size != (len(arr) - mid) else right.right_size + left.right_size
    longest_size = max(left.longest_size, right.longest_size, left.right_size + right.left_size)

    return Result(longest_size, left_size, right_size, is_entire_range)

def get_longest_run(arr, key):
    return longest_run_recursive(arr, key).longest_size

## Feel free to add your own tests here.
def test_longest_run():
    assert get_longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3

## Tests
test_longest_run()

```
  
  - 3d   What is the Work and Span of this recursive algorithm?
    - since we divide the input size into two sublist (left, right) recursively we to have log(n) level from root to leaves and then we sum them up with o(1) conditions with same amount of nodes and edges so we can say the longest path is O(log(n)). But if we do all the process sequencly then we have to iterate over all element and then W(n) = S(n) = O(n), in recursive defination:
    -  W(n) = 2W(n/2) + c and S(n) = 2S(n/2) + c


  - 3e  Assume that we parallelize in a similar way we did with `sum_list_recursive`. That is, each recursive call spawns a new thread. What is the Work and Span of this algorithm?
    - base on previous part span is (log(n)) and since we have access to infinite core (threat) base on defination of parallelism then the S(n) = O(log(n)) but the work is as same as before.
    -  W(n) = O(n) and S(n) = (log(n))

  
