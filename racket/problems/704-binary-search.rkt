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