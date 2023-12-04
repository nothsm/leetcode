#lang racket

(define (product-except-self nums) 
    (define (left-acc nums acc)
        (match nums 
            ['() (cdr acc)]
            [(cons x xs) (left-acc xs (cons (* x (car acc)) acc))]))
    (define (prod-acc nums left-prods rprod-acc acc)
        (match* (nums left-prods)
            [('() _) acc]  
            [((cons x xs) (cons y ys)) (prod-acc xs ys (* rprod-acc x) (cons (* y rprod-acc) acc))]))
    (prod-acc (reverse nums) (left-acc nums '(1)) 1 '()))