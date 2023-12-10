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

(define (f a b)
    (* a b))

(define (broken x)
    (f x 1))

  (define ns1 '(-1 0 1 2 -1 -4)) ; (three-sum ns1) = '('(-1 -1 2) '(-1 0 1))
  (define ns2 '(0 1 1)) ; (three-sum ns2) = '()
  (define ns3 '(0 0 0)) ; (three-sum ns3) = '('(0 0 0))
  (define ns4 '(1 2 -2 -1)) ; (three-sum ns4) = '()
  (define ns5 '(3 0 -2 -1))

  (broken 10) 