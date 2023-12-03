#lang racket

(define (sorted-dict dict)
    (sort (hash->list dict) (lambda (p1 p2) (>= (cdr p1) (cdr p2)))))

(define (top-k-frequent nums k)
    (define (top-k-frequent-acc nums counts)
        (match nums
            ['() (take (dict-keys (sorted-dict counts)) k)]
            [(cons x xs) (top-k-frequent-acc xs (hash-update counts x add1 0))] ))
    (if (= k (length nums)) nums
        (top-k-frequent-acc nums #hash())))