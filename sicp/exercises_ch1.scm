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
; In an applicative evaluation model, (test 0 (p)) returns 0 because test's local x binding is 0, so y is never examined.  
; In a normative applicative evaluation model, it will never return, because p is a non-terminating recursive function, and this model
; evaluates the arguments before applying the operators to them.



