#lang racket

(define (count s)
  (foldl (lambda (c cts) (hash-update cts c add1 0))
         (hash)
         (string->list s)))

(define (hash-sub1 ht k)
    (let ([ht-new (hash-update ht k sub1)])
        (if (= (hash-ref ht-new k) 0)
            (hash-remove ht-new k)
            ht-new)))

(define (check-inclusion s1 s2)
  (define (go left right window cts)
    (cond [(equal? window cts) #t]
          [(= right (string-length s2)) #f]
          [else (let* ([c-left (string-ref s2 left)]
                       [c-right (string-ref s2 right)]
                       [sub (hash-update window c-right add1 0)])
                 (go (add1 left) 
                     (add1 right) 
                     (hash-sub1 sub c-left)
                     cts))]))
  (if (> (string-length s1) (string-length s2)) #f
  (go 0 
    (string-length s1) 
    (count (substring s2 0 (string-length s1))) 
    (count s1))))