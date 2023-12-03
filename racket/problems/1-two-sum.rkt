#lang racket

(define (zip lst1 lst2)
    (map cons lst1 lst2))

(define (indices nums)
    (make-hash (zip nums (range (length nums)))))

(define (two-sum nums target)
    (define i-rights (indices nums))
    
    (define (two-sum-acc nums target i-left)
            (define i-right (hash-ref i-rights (- target (first nums)) #f))
            (if (and i-right (not (= i-left i-right))) 
                (list i-left i-right) 
                (two-sum-acc (rest nums) target (add1 i-left))))
    (two-sum-acc nums target 0))
