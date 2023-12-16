#lang racket

(define (vref vec i)
    (vector-ref vec i))

; TODO: refactor w anaphoric macros and higher order functions
(define (max-area height)
  (define hs (list->vector height))
  (define (go left right max-ar)
    (if (>= left right) 
        max-ar
        (let* ([l (vref hs left)]
               [r (vref hs right)])
            (cond
                [(< l r) (go (add1 left) right (max max-ar (* (min l r) (- right left))))]
                [(>= l r) (go left (sub1 right) (max max-ar (* (min l r) (- right left))))]))))  
  (go 0 (sub1 (vector-length hs)) -1))