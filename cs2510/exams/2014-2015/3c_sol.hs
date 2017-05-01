howManyEqual :: Int -> Int -> Int -> Int
howManyEqual x y z
  | x == y && y == z = 3
  | x /= y && x /= z && y /= z = 0
  | otherwise = 2
