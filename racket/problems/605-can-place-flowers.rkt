#lang racket

(define (can-place-flowers flowerbed n)
    (let loop ([lst (cons 0 flowerbed)] [k n])
        (match lst
            ; base cases
            ['() (= k 0)]
            [(list 0) (<= k 1)]
            [(list 0 0) (<= k 1)]
            [(list x1) (= k 0)]
            [(list x1 x2) (= k 0)]
            ; recursive cases
            [(list 0 0 0 xs ...) (or (<= k 1) (loop (append '(1 0) xs) (sub1 k)))]
            [(cons x xs) (loop xs k)])))