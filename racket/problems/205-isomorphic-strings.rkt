#lang racket

(define (is-isomorphic s t)
  (let loop ([ss (string->list s)] [ts (string->list t)] [s->t (hash)] [t->s (hash)])
    (match (cons ss ts)
        [(cons '() '()) #t]
        [(cons (cons x xs) (cons y ys)) 
            (let* ([f (hash-ref s->t x #f)]
                   [g (hash-ref t->s y #f)])
                (cond [(and f (not (equal? f y))) #f]
                      [(and g (not (equal? g x))) #f]
                      [else (loop xs ys (hash-set s->t x y) (hash-set t->s y x))]))])))