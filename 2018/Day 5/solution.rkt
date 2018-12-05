#lang racket
(define alphabet (string->list "abcdefghijklmnopqrstuvwxyz"))
(define (list-substitutes)
  (define substitutes '())
  (for-each (lambda (char)
    (set! substitutes
      (append substitutes
        (list
          (string-append
            (string char)
            (string (char-upcase char))))))
    (set! substitutes
      (append substitutes
        (list
          (string-append
            (string (char-upcase char))
            (string char))))))
    alphabet)
  substitutes)
(define polymer (read-line (current-input-port) 'linefeed))
(define (synthisize polymer)
  (define poly polymer)
  (define length 0)
  (for/list ([i (in-naturals)]
           #:break (= length (string-length poly)))
          (set! length (string-length poly))
          (for-each (lambda (sub)
            (set! poly (string-replace poly sub "")))
            (list-substitutes)))
  length)
(define (optimized-synthisize polymer)
  (define results '())
  (for-each (lambda (char)
    (define poly (string-replace polymer (string char) ""))
    (set! results
      (append results
        (list
          (synthisize
            (string-replace poly (string (char-upcase char)) ""))))))
    alphabet)
  (foldl min (first results) (rest results)))
(printf "length: ~a\n"
    (synthisize polymer))
(printf "best length: ~a\n"
    (optimized-synthisize polymer))
