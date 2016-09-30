; CHAPTER 1 EXERCISES

; [1.1] translate this into prefix form
;
; 5 + 4 + (2 - (3 - (6 + 4/5)))
; -----------------------------
; 3(6-2)(2-7)
;

(/ 
  (+ 5 4 (- 2 (- 3 (+ 6 (/ 4 5))))) 
  (* 3 (- 6 2) (- 2 7)))

; [1.3]
; Define a procedure that takes 3 numbers as args and returns the sum of the squares of the two larger numbers.
; 2 3 -1, that's an edge case. the middle number is compared twice.
;
; 

(define (square x) (* x x))
(define (max x y) (if (>= x y) x y)) 
(define (largest)
(define (f x y z)
  (if (> x y) 
    (+ (square x) (square (max y z)))
    (+ (square y) (square (max x z)))
  ))

; [1.5]
; What happens if the following code is run in an applicative evaluation model versus a normative model?
;
; (define (p) (p))
; (define(test x y)
;   (if(= x 0)
;     0
;     y))
;
; (test 0 (p))
;
;
; Answer:
; In an applicative evaluation model, (test 0 (p)) never finishes because p is evaluated in every case, regardless of the value of x.  
; In a normal-order evaluation model, it will return 0 because x is 0. Y will never get evaluated.

; Why does writing a 'new-if' function in terms of 'cond' pose a problem when calculating square roots recursively via Netwon's method?
; Answer: the standard 'if' is normal-order evaluation, and only ever evaluates one of its operands, but 'cond', which is applicative order, evaluates them all, so the recursive call will be evaluated in every case.
