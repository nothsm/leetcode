#lang racket

(define (my-remove st x)
    (if (set-member? st x) (set-remove st x) st))

(define (find-disappeared-numbers nums)
    (let loop ([lst nums] [res (list->set (inclusive-range 1 (length nums)))])
        (match nums
            ['() (set->list res)]
            [(cons x xs) (loop xs (my-remove res x))])))
