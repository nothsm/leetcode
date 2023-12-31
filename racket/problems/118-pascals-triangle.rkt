#lang racket

(define (generate rows)
  (define (row last acc)
      (match last
          ['() acc]
          [(list x) (cons 1 acc)]
          [(cons x xs) (row xs (cons (+ x (car xs)) acc))]))

(define (go i acc)
  (cond [(> i rows) (reverse acc)]
        [(= i 1) (go (add1 i) (cons '(1) acc))]
        [else (go (add1 i) (cons (row (car acc) '(1)) acc))]))
  (go 1 '()))