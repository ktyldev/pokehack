{-# LANGUAGE OverloadedStrings #-}
import Network.Wreq
import Control.Lens
import Data.Text.Encoding
import System.IO
import Data.Aeson (ToJSON)
import Data.Aeson.Lens (key, nth)
import Data.ByteString
import GHC.Generics
import Data.Text

data StartData = StartData {
      name :: Text
    , level :: Int
    , pkmn :: String
    , moves :: String
    } deriving (Generic, Show)

instance ToJSON StartData where toEncoding = genericToEncoding defaultOptions

main = do
  let path = "http://localhost:42069"
      join = path ++ "/join"
  --r <- post "http://localhost:42069/joinson" (toJson ["name":=("yelow rat"::String),"pkmn":=("pikachu"::String),"moves":=("[1]"::String),"level":=("1"::String)])
  r <- post "http://localhost:42069/joinson" (encode (StartData {name = "yp", level=1, pkmn="pikachu", moves="[1]"}))

  print r
  let readLoop = do
        System.IO.putStr "Enter input: "
        hFlush stdout
        line <- System.IO.getLine
        if line == "q"
          then return ()
          else do
            readLoop
  readLoop
  return ()
