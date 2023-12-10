#lang racket

; Approach 1
(define (plus-one-recursive digits)
  (define (go digits)
    (match digits
      ['() '(1)]
      [(cons 9 xs) (cons 0 (go xs))]
      [(cons x xs) (cons (add1 x) xs)]))
  (reverse (go (reverse digits))))


; Approach 2
(define (list->number lst)
  (foldl 
    (lambda (x acc)
      (+ (* 10 acc) x))
    0
    lst))

(define (number->list n)
  (define (go n acc)
    (cond
      [(< n 10) (cons n acc)]
      [else (go (quotient n 10) (cons (modulo n 10) acc))]))
  (go n '()))

(define (plus-one digits)
  (number->list (add1 (list->number digits))))