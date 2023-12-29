#lang racket

(define (replace-elements arr)
    (define (go lst max-right acc)
        (match lst
            ['() acc]
            [(cons x xs) (go xs (max max-right x) (cons max-right acc))]))
    (go (reverse arr) -1 '()))