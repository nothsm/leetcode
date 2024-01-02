#lang racket

(define (next-greater-element nums1 nums2)
    (define (put ht mon cutoff)
        (match mon
            ['() (values (cons cutoff mon) ht)]
            [(cons x xs) #:when (>= x cutoff) (values (cons cutoff mon) ht)]
            [(cons x xs) (put (hash-set ht x cutoff) xs cutoff)]))

    (define greaters 
        (let loop ([lst nums2] [mon '()] [res (hash)])
            (match lst
                ['() res]
                [(cons x xs) #:when (empty? mon) (loop xs (cons x mon) res)]
                [(cons x xs) #:when (<= x (car mon)) (loop xs (cons x mon) res)]
                [(cons x xs) (call-with-values (lambda () (put res mon x)) (curry loop xs))])))
  (map (lambda (x) (hash-ref greaters x -1)) nums1))