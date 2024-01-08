#lang racket

(define (two-sum nums target)
  (define idx (make-immutable-hash (map cons nums (range (length nums)))))
  (let loop ([l nums] [i 0])
    (match l
      [(cons x xs) #:do [(define c (- target x))] #:when (and (hash-has-key? idx c) (< i (hash-ref idx c))) (list i (hash-ref idx c))]
      [(cons x xs) (loop xs (add1 i))])))