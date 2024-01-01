#lang racket

(define (suffix-max lst)
  (foldl
    (lambda (x acc)
      (cons (max x (car acc)) acc))
    (list (car lst))
    (cdr lst)))

(define (max-profit prices)
  (if (= (length prices) 1) 0
  (max 0 (argmax identity (map - (suffix-max (reverse (cdr prices))) (drop-right prices 1))))))