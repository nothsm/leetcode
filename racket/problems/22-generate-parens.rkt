#lang racket

(define (generate-parenthesis n)
  (let loop ([l 0] [r 0] [parens '()] [acc '()])
    (cond
        [(= r n) (cons (list->string (reverse parens)) acc)]
        [(= l n) (loop l (add1 r) (cons #\) parens) acc)]
        [(< r l) (append (loop (add1 l) r (cons #\( parens) acc)
                         (loop l (add1 r) (cons #\) parens) acc))]
        [else (loop (add1 l) r (cons #\( parens) acc)])))