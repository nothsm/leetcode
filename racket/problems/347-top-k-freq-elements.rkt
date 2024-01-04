#lang racket

(define (top-k-frequent nums k)
    (define cts (foldl (lambda (x a) (hash-update a x add1 0))
                       (hash)
                       nums))
    (define buckets (foldl (lambda (x a) (hash-update a (hash-ref cts x) (curry cons x) '()))
                           (hash)
                           (remove-duplicates nums)))
    (define sorted (foldl (lambda (ct a) (let ([ns (hash-ref buckets ct #f)])
                                       (if ns (append a ns) a)))
                          '()
                          (inclusive-range (length nums) 1 -1)))
    (take sorted k))