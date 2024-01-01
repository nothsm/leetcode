#lang racket

(define (two-sum nums target)
  (define idx (for/hash ([x nums] [i (in-naturals)])
                (values x i)))

  (let loop ([lst nums] [left 0])
    (let* ([want (- target (car lst))] 
           [right (hash-ref idx want #f)])
        (cond [(and right (< left right)) (list left right)]
              [else (loop (cdr lst) (add1 left))]))))
