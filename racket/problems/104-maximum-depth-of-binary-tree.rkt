#lang racket

(struct tree-node (val left right))

(define (max-depth root)
  (match root
    [#f 0]
    [(tree-node val left right) (add1 (max (max-depth left) (max-depth right)))]))