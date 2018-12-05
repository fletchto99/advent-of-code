#lang racket
(define alphabet (string->list "abcdefghijklmnopqrstuvwxyz"))
(define forward-substitutes (list "aA" "bB" "cC" "dD" "eE" "fF" "gG" "hH" "iI" "jJ" "kK" "lL" "mM" "nN" "oO" "pP" "qQ" "rR" "sS" "tT" "uU" "vV" "wW" "xX" "yY" "zZ"))
(define reverse-substitutes (list "Aa" "Bb" "Cc" "Dd" "Ee" "Ff" "Gg" "Hh" "Ii" "Jj" "Kk" "Ll" "Mm" "Nn" "Oo" "Pp" "Qq" "Rr" "Ss" "Tt" "Uu" "Vv" "Ww" "Xx" "Yy" "Zz"))
(define polymer (read-line (current-input-port) 'linefeed))
(define (synthisize polymer)
  (define poly polymer)
  (define length 0)
  (for/list ([i (in-naturals)]
           #:break (= length (string-length poly)))
          (set! length (string-length poly))
          (for-each (lambda (sub)
            (set! poly (string-replace poly sub "")))
            forward-substitutes)
          (for-each (lambda (sub)
            (set! poly (string-replace poly sub "")))
            reverse-substitutes))
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
