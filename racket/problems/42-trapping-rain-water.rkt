#lang racket

(define (trap height)
    (define H (list->vector height))
    
    (define (go water left right L R)
        (cond [(>= left right) water]
              [else 
                (cond [(<= L R) (go (+ water 
                                       (max (- (min L R)
                                               (vector-ref H (add1 left)))
                                            0))
                                    (add1 left) 
                                    right
                                    (max L (vector-ref H (add1 left)))
                                    R)]
                      [else (go (+ water 
                                   (max (- (min L R) 
                                           (vector-ref H (sub1 right)))
                                        0))
                                   left 
                                   (sub1 right)
                                   L
                                   (max R (vector-ref H (sub1 right))))])]))
    (go 0 
        0 
        (sub1 (length height)) 
        (vector-ref H 0) 
        (vector-ref H (sub1 (length height)))))