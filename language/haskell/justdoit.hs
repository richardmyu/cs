import Data.Char(digitToInt)

data DoIt = DoIt

instance Show DoIt where
  show DoIt = decode $ "1\n5 6▮3 6▮6 2▮1 8▮1\n5 2▮3 2▮1 2▮4 2▮5 2▮4 2▮1\n5 2▮3 2▮1" ++
                       "2▮4 2▮5 2▮4 2▮1\n5 2▮3 2▮1 2▮4 2▮5 2▮4 2▮1\n5 6▮3 6▮6 2▮4 2▮"

decode [] = []
decode (n:s:xs) = (take (digitToInt n) $ repeat s) ++ decode xs

main = print $ Just DoIt
