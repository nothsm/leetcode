#lang racket

(define (search nums target)
  (define (search-helper left right) ; sublist is given by '(nums[left] nums[left + 1] ... nums[right - 1])
    (if (<= right left) -1 ; if sublist is empty, then target is not contained in nums
      (let* 
        ([mid (+ left (quotient (- right left) 2))]
         [nums-mid (list-ref nums mid)]) 
          (cond
            [(= target nums-mid) mid]
            [(< target nums-mid) (search-helper left mid)]
            [(> target nums-mid) (search-helper (add1 mid) right)]))))
  (search-helper 0 (length nums)))


(define ns1 '(-1 0 3 5 9 12))
(define ns2 '(-1 0 3 4 5 9 12))
(define ns3 '(4 5 6 7 0 1 2))
