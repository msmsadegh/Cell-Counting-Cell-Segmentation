Cellpose
Report:

### Day One:

#### Steps:

0) Handle the error about generating HTML and write it to PDF.
1) Try to run the previous code and create a model based on the previous dataset
2) Commit and Push the codes to GitHub in a new organization and new branches
3) Upload the new dataset for the test section and try to measure the model on a new data set


#### Results:
1) First try and first result with just 3 images:
   
|   | Image           | Prediction v. GT IoU | FP | TP | FN | Precision | Recall | Accuracy | F1 |
|---|------------------|------------------------|----|----|----|-----------|--------|----------|----|
| 0 | cb13cb5f85.png   | 0                      | 0  | 0  | 2  | 0         | 0      | 0        | 0  |
| 1 | cc9540d282.png   | 0                      | 0  | 0  | 3  | 0         | 0      | 0        | 0  |
| 2 | cc87926397.png   | 0.53515                | 3  | 16 | 1  | 0.842105  | 0.941176 | 0.8      | 0.888889  |

2) Second Try with the whole new data set, Here is random 10 lines of result:
   
|     | Image           | Prediction v. GT IoU | FP | TP | FN | Precision | Recall   | Accuracy | F1        |
|-----|------------------|------------------------|----|----|----|-----------|----------|----------|-----------|
|   0 | 0a55e7c93f.png | 0.00710279             | 0  | 1  | 23 | 1         | 0.0416667| 0.0416667| 0.08      |
|   1 | 2ee0518d7a.png | 0.0241282              | 0  | 2  | 90 | 1         | 0.0217391| 0.0217391| 0.0425532 |
|   2 | 2daa27a6df.png | 0.0202851              | 7  | 0  | 24 | 0         | 0        | 0        | 0         |
|   3 | 2fb8fe344c.png | 0                      | 2  | 0  | 1  | 0         | 0        | 0        | 0         |
|   4 | 2e4a3ab627.png | 0.0638492              | 2  | 6  | 24 | 0.75      | 0.2      | 0.1875   | 0.315789  |
|   5 | 2e5dab1969.png | 0.285906               | 1  | 1  | 2  | 0.5       | 0.333333 | 0.25     | 0.4       |
|   6 | 2d6f268052.png | 0.281005               | 0  | 4  | 10 | 1         | 0.285714 | 0.285714 | 0.444444  |
|   7 | 2dadb1ced1.png | 0.0257604              | 2  | 0  | 1  | 0         | 0        | 0        | 0         |
|   8 | 2d1a6c5ce4.png | 0.14307                | 2  | 1  | 11 | 0.333333  | 0.0833333| 0.0714286| 0.133333  |
|   9 | 2cd773d930.png | 0                      | 1  | 0  | 94 | 0         | 0        | 0        | 0         |
|  10 | 2c6c108b4d.png | 0.361266               | 0  | 17 | 32 | 1         | 0.346939 | 0.346939 | 0.515152  |
|  11 | 2bf4aa0195.png | 0                      | 0  | 0  | 2  | 0         | 0        | 0        | 0         |
|  12 | 1ff313314c.png | 0                      | 0  | 0  | 1  | 0         | 0        | 0        | 0         |
|  13 | 2bc87a8698.png | 0                      | 0  | 0  | 6  | 0         | 0        | 0        | 0         |
|  14 | 2b9ccd5679.png | 0                      | 2  | 0  | 6  | 0         | 0        | 0        | 0         |
|  15 | 1e011bd992.png | 0.019655               | 4  | 0  | 4  | 0         | 0        | 0        | 0         |
|  16 | 1ecd5c901c.png | 0.606994               | 0  | 47 | 21 | 1         | 0.691176 | 0.691176 | 0.817391  |
|  17 | 1e0f5d817e.png | 0.875022               | 0  | 7  | 0  | 1         | 1        | 1        | 1         |
|  18 | 1d67fb3321.png | 0.908822               | 0  | 6  | 0  | 1         | 1        | 1        | 1         |
|  19 | 1cb46bfdd5.png | 0                      | 4  | 0  | 4  | 0         | 0        | 0        | 0         |
|  20 | 1bf56ce626.png | 0                      | 2  | 0  | 19 | 0         | 0        | 0        | 0         |
|  21 | 1bed563906.png | 0                      | 1  | 0  | 2  | 0         | 0        | 0        | 0         |
|  22 | 0fa38de2c7.png | 0                      | 0  | 0  | 8  | 0         | 0        | 0        | 0         |
|  23 | 1b935635dd.png | 0                      | 0  | 0  | 4  | 0         | 0        | 0        | 0         |
|  24 | 1b3c6536a3.png | 0.135576               | 0  | 10 | 14 | 1         | 0.416667 | 0.416667 | 0.588235  |
|  25 | 1a29c5b84f.png | 0                      | 0  | 0  | 20 | 0         | 0        | 0        | 0         |
|  26 | 01ac659240.png | 0.813457               | 0  | 6  | 0  | 1         | 1        | 1        | 1         |
|  27 | 0ca41ed5b8.png | 0.171889               | 5  | 1  | 3  | 0.166667  | 0.25     | 0.111111 | 0.2       |
|  28 | 0e41d62d5d.png | 0.0293024              | 4  | 0  | 1  | 0         | 0        | 0        | 0         |
|  29 | 0a30487a4e.png | 0.514967               | 1  | 15 | 5  | 0.9375    | 0.75     | 0.714286 | 0.833333  |
|  30 | 8e68b05e0e.png | 0.36636                | 4  | 3  | 2  | 0.428571  | 0.6      | 0.333333 | 0.5       |
|  31 | 8dffc01cc2.png | 0.015861               | 0  | 2  | 64 | 1         | 0.030303 | 0.030303 | 0.0588235 |
|  32 | 8d7fc4c578.png | 0.879287               | 3  | 39 | 4  | 0.928571  | 0.906977 | 0.847826 | 0.917647  |
|  33 | 8cee575b39.png | 0                      | 0  | 0  | 16 | 0         | 0        | 0        | 0         |
|  34 | 8c22d1acd5.png | 0.697842               | 0  | 9  | 1  | 1         | 0.9      | 0.9      | 0.947368  |
|  35 | 8bf3782470.png | 0                      | 3  | 0  | 8  | 0         | 0        | 0        | 0         |
|  36 | 8b40ed2a82.png | 0                      | 0  | 0  | 1  | 0         | 0        | 0        | 0         |
|  37 | 8b7ce99d43.png | 0                      | 2  | 0  | 7  | 0         | 0        | 0        | 0         |
|  38 | 7fabcfe23f.png | 0.0359587              | 0  | 1  | 17 | 1         | 0.0555556| 0.0555556| 0.105263  |
|  39 | 7f94f4bdab.png | 1.40793e-05            | 1  | 0  | 21 | 0         | 0        | 0        | 0         |
|  40 | 7f1a5b0782.png | 0                      | 2  | 0  | 2  | 0         | 0        | 0        | 0         |
|  41 | 7f50b86c4b.png | 0.257578               | 5  | 47 | 171| 0.903846  | 0.215596 | 0.210762 | 0.348148  |
|  42 | 7ecd3c2ab9.png | 0                      | 0  | 0  | 3  | 0         | 0        | 0        | 0         |
|  43 | 7e85b64066.png | 0.795215               | 1  | 10 | 4  | 0.909091  | 0.714286 | 0.666667 | 0.8       |
|  44 | 7d54a1c5b3.png | 0                      | 0  | 0  | 3  | 0         | 0        | 0        | 0         |
|  45 | 7ab1f4b7ba.png | 0                      | 0  | 0  | 39 | 0         | 0        | 0        | 0         |
|  46 | 7ea28e7e54.png | 0.196869               | 6  | 10 | 32 | 0.625     | 0.238095 | 0.208333 | 0.344828  |
|  47 | 7e0c56c44b.png | 0                      | 2  | 0  | 6  | 0         | 0        | 0        | 0         |
|  48 | 7b76562318.png | 0                      | 0  | 0  | 13 | 0         | 0        | 0        | 0         |
|  49 | 7c5501d292.png | 0                      | 1  | 0  | 9  | 0         | 0        | 0        | 0         |


3) Here is 3 random images with different results and evaluations
![alt 1](https://github.com/msmsadegh/cellpose/blob/main/images/download%20(2).png)
![alt 2](https://github.com/msmsadegh/cellpose/blob/main/images/download%20(1).png)
![alt 3](https://github.com/msmsadegh/cellpose/blob/main/images/download.png)


## Bugs:
1) 




