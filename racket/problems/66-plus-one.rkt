#lang racket

(define (list-add1 lst)
  (match lst
    [(cons x xs) (cons (add1 x) xs)]))

(define (plus-one digits)
  (define (plus-one-helper digits acc) 
    (match digits
      [(list x) 
        (match x
          [10 (append (list 1 0) acc)]
          [_ (cons x acc)])]
      [(cons x xs) 
        (match x
          [10 (plus-one-helper (list-add1 xs) (cons 0 acc))]
          [_ (append (reverse digits) acc)])]))
  (match (car (reverse digits))
    [9 (plus-one-helper (list-add1 (reverse digits)) '())]
    [_ (reverse (list-add1 (reverse digits)))]))