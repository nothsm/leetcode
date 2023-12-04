#lang racket

(define (longest-consecutive nums) ; nums = (x1 x2 ... xn)
    (define ns (list->set nums))  ; for constant time lookups for if x is the start of a sequence
    
    (define (seq x) ; (seq x) = 0 if x is not the start of a sequence, (seq x) = length of sequence starting at x otherwise
        (define (seq-acc x acc)  ; count up until x is no longer in nums
            (if (not (set-member? ns x))
                acc
                (seq-acc (add1 x) (add1 acc))))
    (if (set-member? ns (sub1 x)) 0 (seq-acc x 0)))  ; (set-member? ns (sub1 x)) = #t if x is not the start of the sequence, #f otherwise

    (foldl (lambda (x M) (max M (seq x))) 0 (remove-duplicates nums)))  ; equivalent to (max (seq x1) (seq x2) ... (seq xn))

(define ex1 '(100 4 200 1 3 2))
(define ex2 '(0 3 7 2 5 8 4 6 0 1))
(longest-consecutive ex1)
(longest-consecutive ex2)

