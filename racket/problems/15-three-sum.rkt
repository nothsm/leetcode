#lang racket

(define (indices nums)
    (foldl 
        (lambda (x i acc) (hash-set acc x i))
        #hash()
        nums
        (range (length nums))))

(define (three-sum nums)
    (define rights (indices nums))

     (define (two-sum-acc nums target i j acc)
        (match nums
            ['() acc]
            [(cons x xs) 
                (let* ([k-found (hash-ref rights (- target x) #f)])
                        (if (and k-found (> k-found j))
                            (two-sum-acc xs target i (add1 j) (cons (sort (list (- target) x (- target x)) <) acc))
                            (two-sum-acc xs target i (add1 j) acc)))]))

    (define (three-sum-acc nums i acc)
        (match nums
            ['() acc]
            [(cons y ys) (three-sum-acc ys (add1 i) (two-sum-acc ys (- y) i (add1 i) acc))]))
  (remove-duplicates (three-sum-acc nums 0 '())))