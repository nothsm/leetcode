#lang racket

(define (is-subsequence s t)
  (define (go is it)
    (cond [(= is (string-length s)) #t]
          [(= it (string-length t)) #f]
          [(equal? (string-ref s is) (string-ref t it)) (go (add1 is) (add1 it))]
          [else (go is (add1 it))]))
    (go 0 0))