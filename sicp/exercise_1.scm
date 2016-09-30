; translate this into prefix form
;
; 5 + 4 + (2 - (3 - (6 + 4/5)))
; -----------------------------
; 3(6-2)(2-7)
;

(/ 
  (+ 5 4 (- 2 (- 3 (+ 6 (/ 4 5))))) 
  (* 3 (- 6 2) (- 2 7)))

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
