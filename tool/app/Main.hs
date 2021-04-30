{--
Generates templated HTML pages based on reading a project file
--}

module Main where

import Data.List (intercalate)
import Data.List.Split (splitOn, chunksOf)
import System.IO

replaceString :: Eq a => [a] -> [a] -> [a] -> [a]
replaceString old new = intercalate new . splitOn old

generateHTMLTag :: (String, String) -> String
generateHTMLTag (k, v) = "<li><a href=\"" ++ v ++ "\">" ++ k ++ "</a></li>"

unlinesIndent :: Int -> [String] -> String
unlinesIndent sp l = unlines $ map (\x -> concat (replicate sp " ") ++ x) l

main :: IO ()
main = do
  content <- fmap lines . readFile $ "../projects.txt"
  templateContent <- readFile "template.html"

  let pairs = map ((\[k,v] -> (k,v)) . splitOn "=") $ content
  let tags' = unlinesIndent 12 . map generateHTMLTag $ pairs

  let templateContent' = replaceString "$PROJ" tags' templateContent

  putStrLn "Generating HTML file from template!"
  writeFile "../pages/proj.html" templateContent'