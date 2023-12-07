#lang racket

(define (two-sum numbers target)
  (define (two-sum-helper left right)
    (let* ([sum (+ (list-ref numbers left) (list-ref numbers right))])
        (cond
            [(= sum target) (list (add1 left) (add1 right))]
            [(< sum target) (two-sum-helper (add1 left) right)]
            [(> sum target) (two-sum-helper left (sub1 right))])))
  (two-sum-helper 0 (sub1 (length numbers))))