#lang racket

(define (sublist lst l r)
    (let loop ([ns lst] [i 0] [a '()])
        (match ns
            ['() (reverse a)]
            [(cons x xs) #:when (< r i) (reverse a)]
            [(cons x xs) #:when (< i l) (loop xs (add1 i) a)]
            [(cons x xs) #:when (<= l i) (loop xs (add1 i) (cons x a))])))

(define num-array%
  (class object%
    (super-new)
    
    ; nums : (listof exact-integer?)
    (init-field
      nums)
    
    ; sum-range : exact-integer? exact-integer? -> exact-integer?
    (define/public (sum-range left right)
      (apply + (sublist nums left right)))))

;; Your num-array% object will be instantiated and called as such:
;; (define obj (new num-array% [nums nums]))
;; (define param_1 (send obj sum-range left right))