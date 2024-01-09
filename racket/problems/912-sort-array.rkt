#lang racket

(define (merge as bs)
  (match* (as bs)
    [('() bs) bs]
    [(as '()) as]
    [((cons x xs) (cons y ys)) #:when (< x y) (cons x (merge xs bs))]
    [((cons x xs) (cons y ys)) #:when (>= x y) (cons y (merge as ys))]))

(define (sort-array nums)
  (match nums
    ['() nums]
    [(list x) nums]
    [_ #:do [(define-values (ls rs) (split-at nums (quotient (length nums) 2)))] (merge (sort-array ls) (sort-array rs))]))