#lang racket

(struct tree-node (val left right))

(define (invert-tree root)
  (match root
    [#f root]
    [(tree-node val left right) (tree-node val (invert-tree right) (invert-tree left))]))