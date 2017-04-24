g :: Float -> Float -> Float -> Float
g x y z 
   | z == 2 = x/z
   | otherwise = y*y/x
main = print (g 5 2 3)
