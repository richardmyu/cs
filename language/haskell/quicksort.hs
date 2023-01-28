import System.Environment(getArgs)

quicksort :: Ord a => [a] -> [a]
quicksort []     = []
quicksort (x:xs) = quicksort left ++ [x] ++ quicksort right
  where
    left  = filter (< x) xs
    right = filter (>= x) xs

formatList :: Show a => [a] -> String
formatList []     = []
formatList (x:xs) = show x ++ " " ++ formatList xs

main :: IO ()
main = do
  numbers <- fmap (fmap read) getArgs :: IO [Integer]
  putStrLn . formatList . quicksort $ numbers
