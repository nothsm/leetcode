#lang racket

(define (daily-temperatures temperatures)
    (let loop ([l temperatures] [s '()] [i 0] [a (make-vector (length temperatures) 0)])
        (match* (l s)
            [('() _) (vector->list a)]
            [((cons x xs) '()) (loop xs (cons (cons x i) s) (add1 i) a)]
            [((cons x xs) (cons (cons t j) ts)) #:when (<= x t) (loop xs (cons (cons x i) s) (add1 i) a)]
            [((cons x xs) (cons (cons t j) ts)) #:when (> x t) (vector-set! a j (- i j)) (loop l ts i a)])))