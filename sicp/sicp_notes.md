# Notes on SICP

## Contents:

+ [Chapter 1 - Building Abstractions with Procedures](#Building-Abstractions-with-Procedures)

### 1. Building Abstractions with Procedures

#### Lisp Structure

+ Prefix operators and recursive evaluation. 
+ `()` means evaluate an expression, which can be a primitive expression or another compound expression.
+ Evaluate left to right, starting with operator, evaluating / combining arguments and recursing into another evaluation.
+ I sense a similarity here with reduce, although reduce is iterative.
+ 'Recursion is powerful technique for dealing with hierarchical, tree-like objects.' - p.80

````lisp

(+ 2 3) 
(5)
;result is 5

(* 3 4 5 6 7) 
(* 12 5 6 7) 
(* 60 6 7)
(* 360 7)
(2520)
;result is 2520

````

#### Expression evaluation procedure as 'Tree Accumulation.' 

````
(* (+ 2 (+ 4 (* 1 3)))(+ 5 6))

in tree visualization is:
    
    /|-----------\
  * 9             11
    + 2 7         /|\
       /|\       + 5 6
      + 4 3
         /|\
        * 1 3
````


#### Defining Variables

````scheme

;lets define a variable
(define a 2)
a
;prints 2

(define b (* a a))
(b)
; prints 4


;lets define a procedure
(define square 
````

#### Special Forms

A 'special form' has its own evaluation rule.

````
(define a 2)
; 'define' does not follow the standard evaluation rule of combining 'a' and 2.
; a is a symbol, not a primitive or compound expression.
````

#### Defining Procedures

````scheme
; (define (<name> <formal parameters>)<body>)
(define (square x) (* x x))
(square 5)
; 25

(define (sum-of-squares x y) (+ (square x) (square y) ))

(sum-of-squares 5 5)
;50
````

#### Substitution Model for Procedure Application

````
;example
(define (f a) (sum-of-squares (+ a 1) (* a 2)))
````

#### Evaluation Models: Applicative Order versus Normal Order

In normal order, the operator and operands are evaluated and these are then applied to the resulting arguments. 


````scheme

;1. 
(sum-of-squares (+ 5 1) (* 5 2))

;2.
(sum-of-squares 6 10)

;3
(+ (square 6) (square 10))

4;
(+ 36 100)

5;
136

````

In applicative order, the operands are evaluated once the operands are evaluated instead of directly following the evaluation of the operand. E.g,

````scheme
;1.
(sum-of-squares (+ 5 1) (* 5 2))

;2.
(+ (square (+ 5 1))
    (square(* 5 2)))

;3.
(+ (* (+ 5 1)(+ 5 1))
    (* (* 5 2)(* 5 2)))

;4  
(+ (* 6 6)
    (* 10 10))

5;
(+ ( 36 100))

6;
136
````

**Summary**

Normative-order: apply arguments and then reduce.

Applicative-order: evaluate arguments, then apply.

Note: They don't always yield the same results.


#### Conditionals, Predicates

General conditional form:

````
(cond (<p1><e1>)
    (<p2><e2>)
    (<p><e>))
````

````
(if (<p1>) (<e1>) (<e2>))
````

P and E stand for 'predicate' and 'expression', where the expression is evaluated if the predicate is true.
each predicate is evaluated until one is true, at which point, its corresponding expression is evaluated.

example primitive predicates: =, >, <

`cond` without `else`:

````
(define (abs x)
    (cond ((< x 0) (- x))
    ((= x 0) x)
    ((> x 0) x)))

````

`cond` with `else`:

````
(define (abs x)
    (cond ((< x 0) (- x))
    (else x)))

````

Conditional with just `if`:

````
(define (abs x)
    (if (< x 0)
        (- x)
        x))
````


