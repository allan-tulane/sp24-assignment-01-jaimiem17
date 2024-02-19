

# CMPS 2200 Assignment 1

**Name:**_________________________


In this assignment, you will learn more about asymptotic notation, parallelism, functional languages, and algorithmic cost models. As in the recitation, some of your answer will go here and some will go in `main.py`. You are welcome to edit this `assignment-01.md` file directly, or print and fill in by hand. If you do the latter, please scan to a file `assignment-01.pdf` and push to your github repository. 
  
  

1. (2 pts ea) **Asymptotic notation** (12 pts)

  - 1a. Is $2^{n+1} \in O(2^n)$? Why or why not? 
.  Yes
  $2^{n+1} \in O(2^n)$ because $2^{n+1} = $2^{1} * $2^{n} = O(2^n)$
.  You can also  pull out constant C to see that it is true 
.  
. 
  - 1b. Is $2^{2^n} \in O(2^n)$? Why or why not?     
.  No. In this case there is no constant C such that $2^{2^n} <= C(2^n)$ for all n that is big enough because $2^{2^n}$ will always increase at exponentially faster than $2^{n}$
.  
.  
.  
.  
  - 1c. Is $n^{1.01} \in O(\mathrm{log}^2 n)$?    
.
$n^{1.01}$ grows faster than ${log}^2$ n and it tends to infinity instead of a finite positive number, so $n^{1.01} !\in O(\mathrm{log}^2 n)$
    
.  

  - 1d. Is $n^{1.01} \in \Omega(\mathrm{log}^2 n)$?  
.  Yes. in the lower bound, $cf(n)<=g(n)$ when $n>=n_0$. $n^{1.01}$ needs to grow at least as fast as ${log}^2 n for \in O(\mathrm{log}^2 n)$, and $n^{1.01}$ grows faster.
.  
.  
.  
  - 1e. Is $\sqrt{n} \in O((\mathrm{log} n)^3)$?  
.  No, $\sqrt{n} !\in O((\mathrm{log} n)^3)$
.  as n becomes very large, $\sqrt{n}$ grows much faster than the cubic log of n and $cf(n)>=g(n)$ when $n>=n_0$ for $g(n) \in O(f(n))$
.  
.  
  - 1f. Is $\sqrt{n} \in \Omega((\mathrm{log} n)^3)$?  
.  Yes. Like said earlier $\sqrt{n}$ grows much faster than the cubic log of n. This means $g(n)$ asymptotically dominates $f(n)$, so $g(n) \in f(n)$, $\sqrt{n} \in \Omega((\mathrm{log} n)^3)$


2. **SPARC to Python** (12 pts)

Consider the following SPARC code of the Fibonacci sequence, which is the series of numbers where each number is the sum of the two preceding numbers. For example, 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610 ... 
$$
\begin{array}{l}
\mathit{foo}~x =   \\
~~~~\texttt{if}{}~~x \le 1~~\texttt{then}{}\\
~~~~~~~~x\\   
~~~~\texttt{else}\\
~~~~~~~~\texttt{let}{}~~(ra, rb) = (\mathit{foo}~(x-1))~~,~~(\mathit{foo}~(x-2))~~\texttt{in}{}\\  
~~~~~~~~~~~~ra + rb\\  
~~~~~~~~\texttt{end}{}.\\
\end{array}
$$ 

  - 2a. (6 pts) Translate this to Python code -- fill in the `def foo` method in `main.py`  

  - 2b. (6 pts) What does this function do, in your own words?  

.  This function takes in an integer, x, and if x is greater than 1, it wil repeatedly call itself with the parameters of its two preceding values until it finally is less than of equal to 1, which will then recursively return the product of all its preceding values.
.  
.  
.  
.  
  

3. **Parallelism and recursion** (26 pts)

Consider the following function:  

```python
def longest_run(myarray, key)
   """
    Input:
      `myarray`: a list of ints
      `key`: an int
    Return:
      the longest continuous sequence of `key` in `myarray`
   """
```
E.g., `longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3`  
 
  - 3a. (7 pts) First, implement an iterative, sequential version of `longest_run` in `main.py`.  

  - 3b. (4 pts) What is the Work and Span of this implementation?  

.  
.  
.  
.  
.  
.  
.  
.  
.  


  - 3c. (7 pts) Next, implement a `longest_run_recursive`, a recursive, divide and conquer implementation. This is analogous to our implementation of `sum_list_recursive`. To do so, you will need to think about how to combine partial solutions from each recursive call. Make use of the provided class `Result`.   

  - 3d. (4 pts) What is the Work and Span of this sequential algorithm?  
.  
.  
.  
.  
.  
.  
.  
.  
.  
.  
.  


  - 3e. (4 pts) Assume that we parallelize in a similar way we did with `sum_list_recursive`. That is, each recursive call spawns a new thread. What is the Work and Span of this algorithm?  

.  
.  
.  
.  
.  
.  
.  
.  

