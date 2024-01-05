#lang racket

(define (product-except-self nums)
    (define right 
        (let loop ([lst (reverse nums)] [a '(1)])
            (match lst
                ['() (cdr a)]
                [(cons x xs) (loop xs (cons (* x (car a)) a))])))
    (let loop ([lst nums] [l 1] [rps right] [a '()])
        (match* (lst rps)
            [('() '()) (reverse a)]
            [((cons x xs) (cons r rs)) (loop xs (* l x) rs (cons (* l r) a))])))